import statistics

# Функции для подсчета среднего, медианы, максимума и вывода топ-N
def mean(values):
    """Среднее значение"""
    return statistics.mean(values) if values else None

def median(values):
    """Медианное значение"""
    return statistics.median(values) if values else None

def maximum(values):
    """Максимальное значение"""
    return max(values) if values else None

def top_n(records, metric_field, n=5, reverse=True):
    """
    Берет топ-N записей по значению metric_field
    reverse=True -> от большего к меньшему
    """
    records_sorted = sorted(
        [r for r in records if r.get(metric_field) is not None],
        key=lambda x: x[metric_field],
        reverse=reverse
    )
    return records_sorted[:n]