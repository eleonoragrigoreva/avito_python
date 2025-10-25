# Функция для получения значения из вложенного словаря
def get_value(data, keys):
    value = data
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    return value


# Обрабатывает один словарь по конфигу
def process_one_item(data, config):
    result = {}
    for new_key, path in config.items():
        result[new_key] = get_value(data, path)
    return result


# Обрабатывает список словарей
def process_list(data_list, config):
    return [process_one_item(item, config) for item in data_list]
