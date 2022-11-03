# Домашнє завдання 2, 3:
from group import Group
from student import Student
import my_logger as logger
# todo 3.2. Модифікуйте Друге домашнє завдання так, щоб при спробі додавання до групи більше 10-ти студентів,
#  викликалася виняткова ситуація (тип виняткової ситуації треба самостійно реалізувати).
#  Подію додавання нового студента до групи необхідно фіксувати у лог-файлі.
# todo 2.1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
# todo 2.2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
# todo 2.3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
#  Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
#  Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.




students = []
students.append(Student(inn="123456789", full_name="Bondarenko Ivan",
                        date_of_birth='26.11.1982', start_data='15.09.2022'))
students.append(Student(inn="123456788", full_name="Bondarenko Anatoly",
                        date_of_birth='10.01.1985', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov1 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov2 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov3 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov4 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov5 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov6 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov7 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov8 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov9 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov10 Ivan",
                        date_of_birth='01.01.1999', start_data='15.09.2022'))

group = Group(name="Python PRO", logger=logger.My_loger(__name__), students_limit=4)
for i in range(len(students)):
    try:
        group.add_student(students[i])
    except Exception as exc:
        print(exc)

print(group.find_student("Bondarenko"))
print(str(group))
