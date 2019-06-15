#Виселица
import random

#Функция ответственная за рандомное слово
def random_word():
    x = random.choice([
    "apple", 
    "lamon", 
    "man",
    "woman",
    "friend", 
    "businessman", 
    "doctor",
    "artist",
    "cat", 
    "dog",
    "wolf", 
    "house", 
    "tree", 
    "room"])
    return x
choice = random_word()
print("Слово загаданно")

#Длина слова
lenght = len(choice)
print("Длина слова : ", lenght)

#Функция определяющая жизни при отгадывании
def life_in_the_game():
    litter = input("Введите букву : ")
    if litter == choice:
