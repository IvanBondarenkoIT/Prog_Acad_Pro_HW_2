from human import Human


class Student(Human):
    def __init__(self, inn: str, full_name: str, date_of_birth: str, start_data: str):
        super().__init__(inn=inn, full_name=full_name, date_of_birth=date_of_birth)
        self.date_of_admission_to_university = start_data

    def __str__(self):
        return f"inn={self.inn} full name={self.full_name} date of birth={self.date_of_birth}" \
               f" date of admission to university={self.date_of_admission_to_university}"

    def print_all_data(self):
        return super().print_data() + f"\nDate of admission to university: {self.date_of_admission_to_university}"
