students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
for i in students:
    if i in grades:
        print(f"{i} оценка: {grades[i]} ")
    else:
        print(f"{i}Контрольную работу не писал(а)")

bad = []
good = []
for i in students:
    if i in grades:
        if grades[i] >= 8:
            good.append(i)
    else:
        bad.append(i)
print(good, bad)

marks = {'Mary': [5, 8, 9, 10, 3, 5, 6, 6],
        'John': [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex': [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia': [2, 1, 6, 8, 2, 3, 7, 4]}
course = int(input()) - 1
total = 0
for i in marks.values():
        total += i[course]
print(round(total / len(marks)))


marks = {'Mary': [5, 8, 9, 10, 3, 5, 6, 6],
         'John': [3, 3, 6, 8, 2, 1, 8, 5],
         'Alex': [4, 4, 7, 4, 7, 3, 2, 9],
         'Patricia': [2, 1, 6, 8, 2, 3, 7, 4]}
categories = {'отлично': [8, 9, 10],
              'хорошо': [6, 7],
              'удовлетворительно': [4, 5],
              'неуд': [0, 1, 2, 3]}
course = int(input()) - 1
total = 0
for i in marks.values():
        total += i[course]
for k, v in categories.items():
        if round(total / len(marks)) in v:
                print(k)

marks = {'Mary': [5, 8, 9, 10, 3, 5, 6, 6],
         'John': [3, 3, 6, 8, 2, 1, 8, 5],
         'Alex': [4, 4, 7, 4, 7, 3, 2, 9],
         'Patricia': [2, 1, 6, 8, 2, 3, 7, 4]}
mark = int(input())
c = 0
for k, v in marks.items():
        for i in v:
                if i >= mark:
                        c += 1
print(c)


