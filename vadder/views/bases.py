import os
import datetime
import psycopg2
from psycopg2 import Error
from sshtunnel import SSHTunnelForwarder
from collections import Counter
from dotenv import load_dotenv

load_dotenv()

class DataBaseHandler:
    ssh_host = os.getenv("SSH_HOST")
    ssh_port = 22
    ssh_username = os.getenv("SSH_USERNAME")
    ssh_password = os.getenv("SSH_PASSWORD")

    db_host = os.getenv("DB_HOST")
    db_port = int(os.getenv("DB_PORT"))
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    local_host = os.getenv("LOC_HOST")
    local_port = int(os.getenv("LOC_PORT"))

    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    def get_connect(self):
        tunnel = SSHTunnelForwarder(
            (self.ssh_host, self.ssh_port),
            ssh_username=self.ssh_username,
            ssh_password=self.ssh_password,
            local_bind_address=(self.local_host, self.local_port),
            remote_bind_address=(self.db_host, self.db_port)
        )
        tunnel.start()

        conn = psycopg2.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host='localhost',
            port=tunnel.local_bind_port
        )

        return conn

    def get_channels(self):
        conn = self.get_connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT chat_name "
                       f"FROM postgres.public.vacancy_stock "
                       f"WHERE created_at >= '{self.today}'"
                       f"order by created_at DESC"
                       )
        items = cursor.fetchall()
        conn.close()
        counter = Counter(items)
        for chat_name, number in counter.items():
            print(chat_name[0], number)

    def insert_vacancy(self, vacancy_keys, vacancy_values):
        conn = self.get_connect()
        cursor = conn.cursor()
        for database_table in ("admin_last_session", "vacancy_stock"):
            sql = f"""
            INSERT INTO
            postgres.public.{database_table}
            ({vacancy_keys})
            VALUES
            ('{vacancy_values}')
            """
            try:
                cursor.execute(sql)
            except Error as err:
                print("Ошибка выполнения запроса: %s" % err)
            else:
                conn.commit()
                print("Запись успешно добавлена.")
        cursor.close()
        conn.close()


if __name__ == "__main__":
    data_handler = DataBaseHandler()
    data_handler.get_channels()

