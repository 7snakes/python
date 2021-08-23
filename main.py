# 1. ����������� � �����������, �������� ���������, �������� �� �����,
a = 1
b = 'two'
print(a)
print(b)
# ��������� � ������������ ��������� ����� � ����� � ��������� � ����������,
print('Enter your age:')
age = input()

print('Enter your name:')
name = input()

# �������� �� �����.
print('Hello {}, are you {} old "y/n"?'.format(name, age))
correct = input()

if correct == 'y':
    print('ok')
else:
    print('oh, i''m sorry')


# 2. ������������ ������ ����� � ��������.
#    ���������� ����� � ����, ������ � ������� � �������� � ������� ��:��:��.
#    ����������� �������������� �����.
print('Enter time (in sec.):')
time_in_seconds_string = input()
time_in_seconds = int(time_in_seconds_string)
hours = (time_in_seconds // 3600) % 24
minutes = (time_in_seconds // 60) % 60
seconds = time_in_seconds % 60

print('Time is {}:{}:{}'.format(hours, minutes, seconds))


# 3. ������� � ������������ ����� n.
#    ������� ����� ����� n + nn + nnn. ��������, ������������ ��� ����� 3. ������� 3 + 33 + 333 = 369.
print('Enter n:')
n = input()
result_value = 0
for i in [1, 11, 111]:
    result_value = result_value + i * int(n)

print('result is {}'.format(result_value))


# 4. ������������ ������ ����� ������������� �����.
#    ������� ����� ������� ����� � �����.
#    ��� ������� ����������� ���� while � �������������� ��������.
print('Enter n:')
n = input()
i = 0
max_value = 0
while i < len(n):
    if max_value < int(n[i]):
        max_value = int(n[i])
    i += 1
print('Number is {} and max digit is {}'.format(n, max_value))


# 5. ��������� � ������������ �������� ������� � �������� �����.
#    ����������, � ����� ���������� ����������� �������� ����� (������� � ������� ������ ��������, ��� ������ � �������� ������ �������).
#    �������� ��������������� ���������.
#    ���� ����� ���������� � ��������, ��������� �������������� ������� (����������� ������� � �������).
#    ����� ��������� ����������� ����������� ����� � ���������� ������� ����� � ������� �� ������ ����������.
print('�������� �������:')
v_str = input()
v = float(v_str)

print('�������� ��������:')
i_str = input()
i = float(i_str)

if v > i:
    print('�������')
else:
    print('������')

print('�������������� {:.2%}'.format((v - i) / v))


# 6. ��������� ���������� ����������� ����������. � ������ ���� ��� ��������� �������� a ����������.
#    ������ ���� ��������� ���������� ��������� �� 10 % ������������ �����������.
#    ��������� ���������� ����� ���, �� ������� ����� ��������� ���������� ��������� �� ����� b ����������.
#    ��������� ������ ��������� �������� ���������� a � b � �������� ���� ����������� ����� � ����� ���.
# ��������: a = 2, b = 3.
# ���������:
# 1-� ����: 2
# 2-� ����: 2,2
# 3-� ����: 2,42
# 4-� ����: 2,66
# 5-� ����: 2,93
# 6-� ����: 3,22
#
# �����: �� 6-� ���� ��������� ������ ���������� � �� ����� 3 ��.

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

