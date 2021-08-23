# 1. Поработайте с переменными, создайте несколько, выведите на экран,
a = 1
b = 'two'
print(a)
print(b)
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
print('Enter your age:')
age = input()

print('Enter your name:')
name = input()

# выведите на экран.
print('Hello {}, are you {} old "y/n"?'.format(name, age))
correct = input()

if correct == 'y':
    print('ok')
else:
    print('oh, i''m sorry')


# 2. Пользователь вводит время в секундах.
#    Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#    Используйте форматирование строк.
print('Enter time (in sec.):')
time_in_seconds_string = input()
time_in_seconds = int(time_in_seconds_string)
hours = (time_in_seconds // 3600) % 24
minutes = (time_in_seconds // 60) % 60
seconds = time_in_seconds % 60

print('Time is {}:{}:{}'.format(hours, minutes, seconds))


# 3. Узнайте у пользователя число n.
#    Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print('Enter n:')
n = input()
result_value = 0
for i in [1, 11, 111]:
    result_value = result_value + i * int(n)

print('result is {}'.format(result_value))


# 4. Пользователь вводит целое положительное число.
#    Найдите самую большую цифру в числе.
#    Для решения используйте цикл while и арифметические операции.
print('Enter n:')
n = input()
i = 0
max_value = 0
while i < len(n):
    if max_value < int(n[i]):
        max_value = int(n[i])
    i += 1
print('Number is {} and max digit is {}'.format(n, max_value))


# 5. Запросите у пользователя значения выручки и издержек фирмы.
#    Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#    Выведите соответствующее сообщение.
#    Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
#    Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print('значения выручки:')
v_str = input()
v = float(v_str)

print('значения издержек:')
i_str = input()
i = float(i_str)

if v > i:
    print('прибыль')
else:
    print('убыток')

print('рентабельность {:.2%}'.format((v - i) / v))


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
#    Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#    Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
#    Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

print('a:')
a = input()
a = int(a)

print('b:')
b = input()
b = int(b)

day = 0
prev_value = a
next_value = 0
while b > next_value:
    next_value = prev_value + prev_value / 10
    print('{:.2f}'.format(next_value))
    prev_value = next_value

