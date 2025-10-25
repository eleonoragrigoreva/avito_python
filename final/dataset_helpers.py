from collections import defaultdict


# Функции для работы со списками словарей: фильтрация, группировка и агрегация
def filter_by_field(data, field_name, value):
    return [d for d in data if d.get(field_name) == value]


def filter_by_predicate(data, predicate):
    return [d for d in data if predicate(d)]


def group_by_attributes(data, attr_list):
    """
    Группирует записи по комбинации полей
    Возвращает словарь, ключ - кортеж значений атрибутов,
    значение - список записей
    """
    grouped = defaultdict(list)
    for record in data:
        key = tuple(record.get(attr) for attr in attr_list)
        grouped[key].append(record)
    return dict(grouped)


def apply_aggregation(records, metric_field, agg_func):
    """
    Применяет функцию агрегации к полю
    """
    values = [r[metric_field] for r in records if r.get(metric_field) is not None]
    if not values:
        return None
    return agg_func(values)
