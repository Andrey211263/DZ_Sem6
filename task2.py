# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*.
# приоритет операций стандартный. Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций. Пример:
# 1+2*3 => 7;
# (1+2)*3 => 9;
####
#### НЕТ АНАЛИЗА ДЕЛЕНИЯ НА НОЛЬ, РЕАЛИЗОВАН ВАРИАНТ С ОДНОЙ СКОБКОЙ
# ------------------
# метод выделения текста между скобками
# ------------------
def parent(text):
    # sk1 = 0
    # sk2 = 0
    if ')' in text:
        sk2 = text.index(')')
        i = sk2
        while text[i] != '(':
            i -= 1
        sk1 = i
        tmp = text[sk1+1:sk2]
        return tmp, sk1, sk2
    else:
        return -1
# ------------------
# выделение числа в лево после знака арифм. действия
# ------------------
def num_l(text, ch):
    i = 0
    num = ''
    if ch in text:
        i = text.index(ch)
        while text[i-1].isdigit() or text[i-1] == '.':
            num += text[i-1]
            i -= 1
            if i == 0:
                break
    return num[::-1], i
# ------------------
# выделение числа в право после знака арифм.
# ------------------
def num_r(text, ch):
    i = 0
    # end_text = len(text)
    num = ''
    if ch in text:
        i = text.index(ch)
        while text[i+1].isdigit() or text[i+1] == '.':
            num += text[i+1]
            i += 1
            if not(i < len(text)-1):
                break
    return num, i
# ------------------
# арифметические вычисления
# ------------------
def arifm(text, ch):
    tmp = ''
    right = num_r(text, ch)
    left = num_l(text, ch)
    l_end = left[1]
    if ch == '**':
        num = str(round(float(left[0]) ** float(right[0]), 3))
    elif ch == '/':
        num = str(round(float(left[0]) / float(right[0]), 3))
    elif ch == '*':
        num = str(round(float(left[0]) * float(right[0]), 3))
    elif ch == '+':
        tmp = float(left[0])
        if l_end == 1 and text[0] == '-':
            tmp = tmp * -1
            l_end -= 1
        num = str(round(tmp + float(right[0]), 3))
    tmp = text[:l_end] + num + text[right[1]+1:]
    return tmp
# ------------------
#прход по элементам формулы без скобки
# ------------------
def proh(re):
    while '/' in re:
        re = arifm(re, '/')
    while '*' in re:
        re = arifm(re, '*')
    while "-" in re:
        num_r = ""
        num_l = ""
        i = 1
        count = re.find("-", 1)
        if count == -1:
            break
        i = count
        while re[i + 1].isdigit() or re[i + 1] == ".":        # вправо от минуса
            num_r += re[i + 1]
            i += 1
            r = i
            if i == len(re)-1:
                break
        i = count
        while re[i - 1].isdigit() or re[i - 1] == "." or re[i - 1] == "-": # влево от минуса
            num_l += re[i - 1]
            i -= 1
            l = i
            if i == 0:
                break
        num_l = num_l[::-1]
        num = round(float(num_l) - float(num_r), 3)
        if num < 0 and l != 0:
            if re[l-1] == '+':
                l -= 1
        num = str(num)
        tmp = re[:l] + num + re[r+1:]
        re = tmp
    while '+' in re:
        re = arifm(re, '+')
    return re

# fla = '5+10-(25-163/2.5378+21+23*2+5*7)*8+3*4'
# fla = '-5*2-10/(3-110+12/234-5*6.8745+10*255+8/4)*8+3*4-5+15.231*3362-23341/2316'
# fla = '(-100-8)/10+12-16*2-2'
fla = '((1+2)-4+2)*(2+3*3)+((123-34/5)*4-6)'
print(fla)
right = ''
left = ''
result = ''
tmp = ''
# if ')' in fla:
#     scobka = parent(fla) # берем что внутри скобок
#     tmp = scobka[0]

# #убираем скобки и вставляем результат вычислений скобок в выражение
#     result = proh(tmp)     #обработка внутри скобки

#     # sk_r = scobka[2]
#     tmp = fla[:scobka[1]]       # левая скобка -> scobka[1]
#     tmp += result
#     tmp += fla[scobka[2]+1:]    # правая скобка -> scobka[2]
#     print(tmp)
# else:
#     tmp = fla
#     print(tmp)
# result = proh(tmp)     #обработка после скобки

tmp_fl = fla
while ')' in tmp_fl:
    scobka = parent(tmp_fl) # берем что внутри скобок
    tmp = scobka[0]

#убираем скобки и вставляем результат вычислений скобок в выражение
    result = proh(tmp)     #обработка внутри скобки

    # sk_r = scobka[2]
    tmp = tmp_fl[:scobka[1]]       # левая скобка -> scobka[1]
    tmp += result
    tmp += tmp_fl[scobka[2]+1:]    # правая скобка -> scobka[2]
    tmp_fl = tmp
    print(tmp_fl)
# else:
#     tmp = fla
#     print(tmp)

result = proh(tmp_fl)

print(result)
