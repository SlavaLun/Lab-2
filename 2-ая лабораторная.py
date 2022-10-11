import csv


def esc(code):
    return f'\u001b[{code}m'


GREEN = esc(42)
END = esc(0)
YELLOW = esc(43)
RED = esc(41)
WHITE = esc(47)
count_less_150 = 0
count_more_150 = 0
N = int(input("Сколько раз повторить рисунок?"))


def Flag():  # Создание флага
    for i in range(3):
        print(GREEN + ' ' * 11 + YELLOW + ' ' * 19 + END)
    for i in range(3):
        print(GREEN + ' ' * 11 + RED + ' ' * 19 + END)


def Pattern(N):  # Создание рисунка нужное количество раз вниз и вправо
    count = 1
    n = 2
    for i in range(N):
        print(('0' * 83) * N)

        for i in range(6):
            print(('0' * (26 - n) + '1' * count + '0' * (20 - n) + '0' * (17 - n) + '1' * count + '0' * (26 - n)) * N)
            count += 6
            n += 3

        print(('0' * (26 - n) + '1' * (count + 34) + '0' * (26 - n)) * N)
        print(('0' * (26 - n - 3) + '1' * (count + 40) + '0' * (26 - n - 3)) * N)
        print(('0' * (26 - n) + '1' * (count + 34) + '0' * (26 - n)) * N)

        for i in range(6):
            print(('0' * (29 - n) + '1' * (count - 6) + '0' * (23 - n) + '0' * (20 - n) + '1' * (count - 6) + '0' * (
                    29 - n)) * N)
            count -= 6
            n -= 3


def Function():  # Создание графика функции
    for i in range(1, 9):
        print(WHITE + str(10 - i) + WHITE + '  ' * (8 - i) + RED + ' ' * 2 + WHITE + '  ' * (i - 1) + END)

    print(WHITE + '1' + WHITE + ' ' * 16 + END)
    print(WHITE + '0 1 2 3 4 5 6 7 8' + END)


with open('books.csv', 'r') as file:
    G = file.readline()  # Считывание первой ненужной строчки таблицы
    table = csv.reader(file, delimiter=';')
    for row in table:
        if int(float(row[7])) <= 150:
            count_less_150 += 1
        else:
            count_more_150 += 1


def Diagram():  # Создание диаграммы по полученным значениям книг
    if count_more_150 > count_less_150:
        print(str(count_more_150) + WHITE + ' ' * 16 + RED + '  ' + WHITE + ' ' * 10 + END)
    else:
        print(str(count_less_150) + WHITE + ' ' * 16 + RED + '  ' + WHITE + ' ' * 10 + END)

    for i in range(4):
        print('    ' + WHITE + ' ' * 16 + RED + '  ' + WHITE + ' ' * 10 + END)

    if count_more_150 < count_less_150:
        print(
            str(count_more_150) + WHITE + ' ' * 9 + RED + '  ' + WHITE + ' ' * 5 + RED + '  ' + WHITE + ' ' * 10 + END)
    else:
        print(
            str(count_less_150) + WHITE + ' ' * 9 + RED + '  ' + WHITE + ' ' * 5 + RED + '  ' + WHITE + ' ' * 10 + END)

    for i in range(3):
        print('    ' + WHITE + ' ' * 9 + RED + '  ' + WHITE + ' ' * 5 + RED + '  ' + WHITE + ' ' * 10 + END)
    print(' ' * 12 + '>150' + ' ' * 3 + '<=150')


print("Флаг Бенина")
Flag()

print("\n" * 2 + "Рисунок")
Pattern(N)

print("\n" * 2 + "Функция y=x+1 ")
Function()

print("\n" * 2 + "Диаграмма по книгам")
Diagram()
