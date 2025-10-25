from laureates_configs import process_persons, process_orgs

# Определяем, человек или организация
def process_laureate(data):
    if 'knownName' in data:
        person = process_persons(data)
        person['type_'] = 'person'
        return person
    elif 'orgName' in data:
        org = process_orgs(data)
        org['type_'] = 'organization'
        return org
    else:
        return {'type_': 'unknown'}
