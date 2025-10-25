import statistics


# Функции для подсчета среднего, медианы, максимума и вывода топ значений
def mean(values):
    # минимальное
    return statistics.mean(values) if values else None


def median(values):
    # медиана
    return statistics.median(values) if values else None


def maximum(values):
    # максимальное
    return max(values) if values else None


def top_n(records, metric_field, n=5, reverse=True):
    # топ значений
    records_sorted = sorted(
        [r for r in records if r.get(metric_field) is not None],
        key=lambda x: x[metric_field],
        reverse=reverse
    )
    return records_sorted[:n]
