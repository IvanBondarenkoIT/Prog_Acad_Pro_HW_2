class Human:
    def __init__(self, inn: str, full_name: str, date_of_birth: str):
        self.inn = inn
        self.full_name = full_name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"inn={self.inn} full name={self.full_name} date of birth={self.date_of_birth}"

    def print_data(self):
        return f"INN: {self.inn}\nFull name: {self.full_name}\nDate of birth: {self.date_of_birth}"
