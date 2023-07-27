# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

a = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# приводим все элементы строки к нижнему регистру:
a = a.lower()
# заменяем I'm на I am:
a = a.replace("I'm","I am")
# заменяем точку на пробел:
a = a.replace("."," ")
# получаем таблицу из строки, разделитель - пробел:
b = a.split()
print(b)
# приводим список к типу данных множество (у него не повторяются элементы) и считаем количество элементов множества.
print(len(set(b)))