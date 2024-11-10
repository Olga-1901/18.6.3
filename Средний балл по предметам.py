import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
        print(f'''{student}
        {students_marks[student]}''')

        print('''
            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Выход из программы
             ''')

while True:
            command = int(input('Введите команду: '))
            if command == 1:
                print('1. Добавить оценку ученика по предмету')
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                mark = int(input('Введите оценку: '))
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                else:
                 print('ОШИБКА: неверное имя ученика или название предмета')

            elif command == 2:
                print('2. Вывести средний балл по всем предметам по каждому ученику')
                for student in students:
                    print(student)
                    for class_ in classes:
                        marks_sum = sum(students_marks[student][class_])
                        marks_count = len(students_marks[student][class_])
                        print(f'{class_} - {marks_sum // marks_count}')
                    print()


Александра
        {'Математика': [3, 5, 5], 'Русский язык': [2, 1, 1], 'Информатика': [4, 1, 3]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Выход из программы
             
Ангелина
        {'Математика': [1, 2, 3], 'Русский язык': [4, 2, 1], 'Информатика': [5, 5, 3]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Выход из программы
             
Аполлон
        {'Математика': [2, 2, 4], 'Русский язык': [5, 2, 2], 'Информатика': [2, 1, 4]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Выход из программы
             
Дарья
        {'Математика': [2, 5, 1], 'Русский язык': [3, 3, 5], 'Информатика': [5, 1, 5]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Выход из программы
             
Ярослав
        {'Математика': [4, 4, 1], 'Русский язык': [5, 1, 1], 'Информатика': [3, 3, 2]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Выход из программы
             
Введите команду: 1
1. Добавить оценку ученика по предмету
Введите имя ученика: Дарья
Введите предмет: Информатика
Введите оценку: 4
Для Дарья по предмету Информатика добавлена оценка 4
Введите команду: 2
2. Вывести средний балл по всем предметам по каждому ученику
Александра
Математика - 4
Русский язык - 1
Информатика - 2

Ангелина
Математика - 2
Русский язык - 2
Информатика - 4

Аполлон
Математика - 2
Русский язык - 3
Информатика - 2

Дарья
Математика - 2
Русский язык - 3
Информатика - 3

Ярослав
Математика - 3
Русский язык - 2
Информатика - 2

Введите команду: 
