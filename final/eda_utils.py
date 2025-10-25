from collections import defaultdict, Counter


def count_missing(data):
    """
    Количество пропусков в каждом поле и какую долю они составляют

    Args:
        data: список словарей с лауреатами

    Returns:
        missing_counts: словарь {название поля: количество пропусков}
        missing_ratio: словарь {название поля: доля пропусков,
        округлённая до 4 знаков}
    """
    total_records = len(data)
    missing_counts = defaultdict(int)

    for record in data:
        for key, value in record.items():
            if value is None:
                missing_counts[key] += 1

    missing_counts = dict(missing_counts)
    missing_ratio = {k: round(v / total_records, 4) for k, v in missing_counts.items()}

    return missing_counts, missing_ratio


def get_min_max_id_year(data):
    """
    Минимальный и максимальный id и к каким годам вручения они относятся

    Args:
        data: список словарей с лауреатами

    Returns:
        min_id_pair, max_id_pair: кортежи (id, award_year)
    """
    id_year_pairs = []

    for l in data:
        id_ = int(l['id'])
        for prize in l.get('prizes', []):
            year = prize.get('award_year')
            if year is not None:
                id_year_pairs.append((id_, year))

    min_id_pair = min(id_year_pairs, key=lambda x: x[0])
    max_id_pair = max(id_year_pairs, key=lambda x: x[0])

    return min_id_pair, max_id_pair


def find_duplicate_ids(data):
    """
    Проверка повторяющихся id среди лауреатов

    Args:
        data: список словарей с лауреатами

    Returns:
        список id, которые встречаются более одного раза
    """
    all_ids = [int(l['id']) for l in data]
    id_counts = Counter(all_ids)
    duplicate_ids = [i for i, count in id_counts.items() if count > 1]
    return duplicate_ids


def find_id_gaps(data):
    """
    Пары id, между которыми есть разрыв больше 1

    Args:
        data: список словарей с лауреатами

    Returns:
        список кортежей (id1, id2),
        где id2 - следующий за id1, а разрыв больше 1
    """
    all_ids = sorted([int(l['id']) for l in data])
    gaps = []

    for i in range(1, len(all_ids)):
        if all_ids[i] - all_ids[i-1] > 1:
            gaps.append((all_ids[i-1], all_ids[i]))

    return gaps
