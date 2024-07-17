from django.apps import AppConfig
from project.settings import BASE_DIR

class VadderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "vadder"
    path = BASE_DIR / "vadder"
