

def prepare_vacancy_items(dirty_items):
    clear_items = {key: val for key, val in dirty_items.items() if val}
    vacancy_items = clear_items.items()
    keys, values = (zip(*vacancy_items))
    keys = ", ".join(keys)
    values = "', '".join(values)
    return keys, values
