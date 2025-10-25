from json_dict_processing import process_list


# Функция для извлечения года из строки
def get_year(text):
    if text and len(text) >= 4:
        return int(text[:4])
    return None


# Конфиг для данных о призах
CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': ['awardYear'],
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus']
}


# Обработчик для списка наград
def process_prizes(prizes):
    result = process_list(prizes, CONFIG_PRIZE)
    for r in result:
        r['award_year'] = get_year(r['award_year'])
    return result
