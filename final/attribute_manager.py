# Функции для добавления или удаления полей у списка словарей

def add_field(records, field_name, func):
    """
    Добавляет новое поле field_name к каждому словарю
    Значение поля вычисляется функцией func(record)
    """
    for r in records:
        r[field_name] = func(r)
    return records

def remove_field(records, field_name):
    """
    Удаляет поле field_name из всех словарей
    """
    for r in records:
        if field_name in r:
            del r[field_name]
    return records