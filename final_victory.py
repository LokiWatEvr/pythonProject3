from main import game

def welcome():
    print("привет")
    username = str(input("как тебя зовут?"))
    ready = input(username + ", ты готов?да\нет").lower()
    if ready == "да":
        print(game(1))
    elif ready == "нет":
        print("тогда подготовься еще")
    else:
        print("я тебя не понимаю")


print(welcome())