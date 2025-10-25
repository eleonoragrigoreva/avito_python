from json_dict_processing import process_one_item
from prizes_configs import process_prizes

# Функция для извлечения года из даты
def get_year_from_date(date_str):
    if date_str and len(date_str) >= 4:
        return int(date_str[:4])
    return None


# Конфиг для человека
CONFIG_PERSON = {
    'id': ['id'],
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_date': ['birth', 'date'],
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes': ['nobelPrizes']
}

# Конфиг для организации
CONFIG_ORG = {
    'id': ['id'],
    'name': ['orgName', 'en'],
    'founded_date': ['founded', 'date'],
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes': ['nobelPrizes']
}


# Обработка человека
def process_persons(person):
    result = process_one_item(person, CONFIG_PERSON)
    result['birth_year'] = get_year_from_date(result['birth_date'])
    result['prizes'] = process_prizes(result['prizes'] or [])
    return result


# Обработка организации
def process_orgs(org):
    result = process_one_item(org, CONFIG_ORG)
    result['founded_year'] = get_year_from_date(result['founded_date'])
    result['prizes'] = process_prizes(result['prizes'] or [])
    return result
