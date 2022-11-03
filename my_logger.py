import logging


class My_loger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

        self.logger.setLevel(logging.INFO)
        __formatter = logging.Formatter('%(asctime) s %(name)-12s %(levelname)-8s %(message)s')

        __filehandler = logging.FileHandler(f'{__name__}.log')
        __filehandler.setLevel(logging.INFO)
        __filehandler.setFormatter(__formatter)

        __streamhandler = logging.StreamHandler()
        __streamhandler.setLevel(logging.WARNING)
        __streamhandler.setFormatter(__formatter)
        self.logger.addHandler(__filehandler)
        self.logger.addHandler(__streamhandler)

    def add_warning(self, message):
        self.logger.warning(message)

    def add_info(self, message):
        self.logger.info(message)
    #     (f'{student}: Wrong datatype with student')
    #     raise TypeError('Student must be an instance of class Student')
    #
    # if student in self.__students:
    #     logger.warning(f'{student}: Duplicat of student')
    #     raise ValueError('Student is already in group')
    # if len(self.__students) >= self.students_limit:
    #     logger.warning(f'{student}: Limit')
