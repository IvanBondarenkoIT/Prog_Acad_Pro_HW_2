from exception import User_Exception
from student import Student


class Group:
    def __init__(self, name: str):
        self.name = name
        self.students = []

    def add_student(self, student: Student) -> str:
        """Added new student to group"""
        if len(self.students) >= 10:
            raise User_Exception(f"Sorry, cannot add student {student}, group is full")
        else:
            if isinstance(student, Student):
                if student not in self.students:
                    self.students.append(student)
                    # need to LOG
                    # return f"Student {student} - added"
                else:
                    raise User_Exception("This student already in group")
            else:
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
