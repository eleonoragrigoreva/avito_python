# Функции для добавления или удаления полей у списка словарей


def add_field(records, field_name, func):
    # добавление поля
    for r in records:
        r[field_name] = func(r)
    return records


def remove_field(records, field_name):
    # удаление поля
    for r in records:
        if field_name in r:
            del r[field_name]
    return records
