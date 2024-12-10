import random #подключаем модуль random
spisok=[(random.randint(-10,10),random.randint(-10,10),random.randint(-10,10),random.randint(-10,10)) for i in range(1,20+1)]# Создаем список из 20 кортежей, каждый из которых содержит 4 случайных целых числа от -10 до 10
print (spisok) #вывод на консоль
unique_pairs=set() # Создаем множество для хранения уникальных пар кортежей

for i in range(len(spisok)):
    for j in range(i + 1, len(spisok)):
        unique_pairs.add((spisok[i], spisok[j]))#cсоздаём кортеж из двух элементов и добавляем в множесво 

print("Список уникальных пар:") #вывод на консоль
for pair in unique_pairs: #проходимся с помощью цикла по каждой уникальной паре 
    print(pair) #вывод на консоль

user_input = int(input("Введите целое число: ")) #вводим число с клавиатуры

count = 0 #счётчик для уникальных пар сумма которых меньше числа, ведённого с клавиатуры 
for pair in unique_pairs: # проходим с помощью цикла по всем уникальным парам
    sum_pair = sum(pair[0]) + sum(pair[1]) #вычисляем сумму
    if sum_pair < user_input: #если сумма меньше, числа user_num
        count += 1 # к переменной count добавляем 1

print(f"Количество пар, чья сумма меньше {user_input}: {count}") #вывод на консоль
