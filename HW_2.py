# Домашнє завдання 2:

# todo 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
class Human:
    def __init__(self, inn: str, full_name: str, date_of_birth: str):
        self.inn = inn
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"inn={self.inn} full name={self.full_name} date of birth={self.date_of_birth}"

    def print_data(self):
        return f"INN: {self.inn}\nFull name: {self.full_name}\nDate of birth: {self.date_of_birth}"


# todo 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
class Student(Human):
    def __init__(self, inn: str, full_name: str, date_of_birth: str, start_data: str):
        super().__init__(inn=inn, full_name=full_name, date_of_birth=date_of_birth)
        self.date_of_admission_to_university = start_data

    def __str__(self):
        return f"inn={self.inn} full name={self.full_name} date of birth={self.date_of_birth}" \
               f" date of admission to university={self.date_of_admission_to_university}"

    def print_all_data(self):
        return super().print_data() + f"\nDate of admission to university: {self.date_of_admission_to_university}"


# todo 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
#  Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
#  Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
class Group:
    def __init__(self, name: str, max_students: int=10):
        self.name = name
        self.students = []
        self.max_students = max_students

    def add_student(self, student: Student) -> str:
        """Added new student to group"""
        if len(self.students) >= self.max_students:
            return "Sorry, cannot add student, group is full"
        elif isinstance(student, Student):
            if student not in self.students:
                self.students.append(student)
                return f"Student {student} - added"
            else:
                return "This student already in group"

    def remove_student(self, student: Student) -> str:
        """Remove a student from group"""
        if student in self.students:
            self.students.remove(student)
            return f"Student {student} - removed"
        else:
            return "Student not in group"

    def find_student(self, lastname: str) -> list:
        """Find students with giving last name"""
        __list = []
        for student in self.students:
            __ln = student.full_name.split()
            if __ln[0].lower() == lastname.lower():
                __list.append(str(student))
        return __list
    def __str__(self):
        __result = f"Group:{self.name}\n"
        __result += "".join([str(student)+'\n' for student in self.students])
        return __result


students = []
students.append(Student(inn="123456789", full_name="Bondarenko Ivan",
                    date_of_birth='26.11.1982', start_data='15.09.2022'))
students.append(Student(inn="123456788", full_name="Bondarenko Anatoly",
                    date_of_birth='10.01.1985', start_data='15.09.2022'))
students.append(Student(inn="123456787", full_name="Ivanov Ivan",
                    date_of_birth='01.01.1999', start_data='15.09.2022'))

group = Group("Python PRO")
for i in range(len(students)):
    print(group.add_student(students[i]))

# print(group.remove_student(students[2]))
print(students[0].print_all_data())
print(group.find_student("Bondarenko"))
print(str(group))
