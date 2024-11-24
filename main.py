import random

def game(rounds):
    famous_people = {'Пушкин': '26.06.1799', 'Лермонтов': '15.10.1814', 'Есенин': '03.10.1895'}
    for i in range(rounds):
        name, date = random.choice(list(famous_people.items()))
        answer = input(f'когда родился {name}')
        if answer == date:
            print("верно")
        else:
            print("неверно")
    return("пока")
