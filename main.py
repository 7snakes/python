# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
user_data = []
while True:
    user_data.append(input("Enter text:") + "\n")
    if len(user_data[-1]) == 1:
        break

# Держать открытым ресурс - это плохо, поэтому в 2 цикла
with open("part1.txt", "w") as user_file:
    user_file.writelines(user_data[0:-1])

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
lines_count = 0
with open("part2.txt", "r") as user_file:
    for line in user_file:
        lines_count += 1
        print("line: {}, words_count: {}".format(lines_count, len(line.split())))
print("lines count: {}".format(lines_count))

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
avg_list = []
with open("part3_dream_team.txt", "r") as user_file:
    for user in user_file.readlines():
        avg_list.append(int(user.split()[1]))
        if avg_list[-1] < 20000:
            print("оклад менее 20 тыс: {}".format(user))
print("avg: {}".format(sum(avg_list) / len(avg_list)))

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
print(rus_dict)

with open("part4.txt", "r") as data_file:
    with open("part4_new.txt", "w") as new_data_file:
        for line in data_file:
            new_data_file.write(line.replace(line.split(" - ")[0], rus_dict[line.split(" - ")[0]]))

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
number = 5
with open("part5_data.txt", "w") as data_file:
    for i in range(number):
        data_file.write("{} ".format(i))

with open("part5_data.txt", "r") as data_file:
    data_from_file = data_file.readline()
    summa = 0
    for i in data_from_file.split():
        summa += int(i)
    print("сумма чисел в файле: {}".format(summa))


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def numbers_only(some_text):
    result_value = ""
    for char_value in some_text:
        if char_value.isdigit():
            result_value += char_value
    return 0 if len(result_value) == 0 else int(result_value)


final_result = {}
with open("part6.txt", "r") as data_file:
    for line in data_file:
        line_array = line.split()
        final_result[line_array[0]] = numbers_only(line_array[1]) + numbers_only(line_array[2]) + numbers_only(line_array[3])
print(final_result)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

json_data = {}
lines_count = 0
average_profit = 0
with open('part7.txt', 'r') as data_file:
    for line in data_file:
        lines_count += 1
        data_info = line.split()
        vr = int(data_info[2]) - int(data_info[3])
        if vr > 0:
            average_profit += vr
        json_data[data_info[0]] = vr

with open("part7_result.txt", "w") as new_data_file:
    json.dump([json_data, {"average_profit": average_profit / lines_count}], new_data_file)
