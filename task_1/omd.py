def step2_umbrella():
    print('Конечно, по всем законам нашей жизни, когда берешь зонтик, дождя обязательно не будет)')


def step2_no_umbrella():
    print('Конечно, когда у тебя нет с собой зонтика, дождь обязательно пойдет)')
    print('Давай поможем утке сделать выбор: прыгать по лужам или бежать прятаться в бар')
    
    choice = ''
    options = {'1': 'прыгать по лужам', '2': 'бежать в бар'}  
    
    while choice not in options:
        print('Что же делать?: {}/{}'.format(*options.keys()))  
        choice = input().strip()  
    
    if choice == '1':
        print('Отличный выбор! Как легко наслаждаться жизнью в моменте!')
    else:
        print('Прекрасно! Утка точно не простудится')

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input().lower().strip()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()