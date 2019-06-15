import random

#Рандомное загаданное число компьютером
def random_number(x):
	x = random.randint(1 , 20)		#x будет хранить в себе случайное число
	return x
random_number()
print("Рандомное число загаданное")

#Сторона пользователя
while True:
	numder = int(input("Введите ваше число: "))
	if number == random_number():
		print("Поздравляем это загаданное число!")
		False
	elif number > random_number():
		print("Число намного меньше,выберите другое")
	else:
		print("Число намного больше,выберите другое")
		
