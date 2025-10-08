import csv 

"""
Функция считывания файла
Получает на вход адрес файла, формирует список словарей с информацией о сотрудниках  
"""
def read_csv(path: str) -> list[dict[str, str]]:
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter=';'))

"""
Функция, которая выводит иерархию департаментов и отделов внутри них
Получает на вход инфу о сотрудниках
Пробегаем по каждой строке, проверяем, добавлен ли департамент в словарь, если нет, то добавляем, 
затем добавляем команду в множество команд департамента 
В конце всё выводим с отступами и черточками для наглядности
"""
def show_hierarchy(data:list[dict[str, str]]) -> None:
    hierarchy = {}
    for row in data:
        dep = row['Департамент']
        team = row['Отдел']
        if dep not in hierarchy:
                hierarchy[dep] = set()  
        hierarchy[dep].add(team)

    for dep, teams in hierarchy.items():
        print(f'- {dep}')
        for team in sorted(teams):
            print(f'  - {team}')

"""
Функция, которая строит отчет по департаментам
Сначала создаем словарь, чтобы хранить данные с зарплатой по департаментам
Потом создаем словарь с итогами, где считаем показатели по каждому отделу на основе зарплат
Численность также считаем по зарплатам, потому что добавляли все записи, а не уникальные 
"""
def make_report(data) -> dict:
    report = {}
    for row in data:
        dep = row['Департамент']
        salary = float(row['Оклад'])
        if dep not in report:
            report[dep] = []
        report[dep].append(salary)

    summary = {}
    for dep in report:
        salaries = report[dep]
        summary[dep] = {
            'count': len(salaries),
            'min': min(salaries),
            'max': max(salaries),
            'avg': round(sum(salaries)/len(salaries), 2)
        }
    return summary

"""
Функция, которая строит отчет по департаментам
Сначала создаем словарь, чтобы хранить данные с зарплатой по департаментам
Потом создаем словарь с итогами, где считаем показатели по каждому отделу на основе зарплат
Численность также считаем по зарплатам, потому что добавляли все записи, а не уникальные 
Вилку выводим, заранее формируя ее в отдельной строке
"""
def print_report(report) -> None:
    print(f"{'Департамент':<15} {'Численность':<12} {'Вилка зарплат':<15} {'Средняя':<10}") # добавила форматирование, чтобы выводилось ровно
    print("-" * 65) # тоже для красоты
    for dep in report:
        stats = report[dep]
        salary_range = f"{int(stats['min'])} - {int(stats['max'])}"
        print(f"{dep:<15} {stats['count']:<12} {salary_range:<15} {stats['avg']:<10.2f}")

"""
Функция, которая сохраняет отчет в файлик
открываем файл для чтения, записываем первую строку с заголовками, записываем по строкам данные о сотрудниках
"""
def save_report(report, path) -> None:
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, delimiter=';') # записываю через точку с запятой как было в исходном файле
        w.writerow(['Департамент', 'Численность', 'Вилка зарплат', 'Средняя'])
        for dep in report:
            stats = report[dep]
            salary_range = f"{int(stats['min'])} - {int(stats['max'])}"
            w.writerow([dep, stats['count'], salary_range, stats['avg']])
    print('Отчёт сохранён в', path)

"""
Основная функция
"""
def main():
    file_path = input('Введите путь до файла: ') # путь считываем с клавиатуры
    data = read_csv(file_path) 

    while True:
        print('Меню:')
        print('1 - Вывести иерархию команд')
        print('2 - Вывести сводный отчёт по департаментам')
        print('3 - Сохранить сводный отчёт по департаментам в файл')
        print('0 - Выход')
        choice = input('Выберите пункт: ') # выводим варианты и ожидаем ввод с одним из них

        if choice == '1':
            show_hierarchy(data) # 1 - показываем иерархию
        elif choice == '2':
            report = make_report(data) # строим ответ 
            print_report(report) # построенный отчет выводим
        elif choice == '3':
            report = make_report(data) # строим отчет
            save_path = input('Введите имя файла для сохранения: ') # спрашиваем путь
            save_report(report, save_path) # записываем в файлик
        elif choice == '0':
            break
        else:
            print('Нет такого варианта') # если введено что-то другое 

if __name__ == '__main__':
    main()