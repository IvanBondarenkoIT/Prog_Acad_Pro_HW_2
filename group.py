from exception import User_Exception
from student import Student


class Group:
    def __init__(self, name: str, logger, students_limit=10):
        self.name = name
        self.logger = logger
        self.students_limit = students_limit
        self.students = []


    def add_student(self, student: Student) -> str:
        """Added new student to group"""
        if len(self.students) >= self.students_limit:
            self.logger.add_warning(f'{student}: Limit')
            raise User_Exception(f"Sorry, cannot add student {student}, group is full")
        else:
            if isinstance(student, Student):
                if student not in self.students:
                    self.students.append(student)
                    self.logger.add_info(f'{student}: Added')
                else:
                    self.logger.add_warning(f'{student}: Duplicat of student')
                    raise User_Exception("This student already in group")
            else:
                self.logger.add_warning(f'{student}: Wrong datatype with student')
                raise TypeError

    def remove_student(self, student: Student) -> str:
        """Remove a student from group"""
        if student in self.students:
            self.students.remove(student)
            # need to LOG
            # return f"Student {student} - removed"
        #else:
            # return "Student not in group"

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
