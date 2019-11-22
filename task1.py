class Student:
    def __init__(self, name, surname, year_of_entrace, department):

        self.name = name
        self.surname = surname
        self.year_of_entrace = year_of_entrace
        self.department = department

    def get_student_info(self):
        
        return 'Студент: ' + self.name + ' ' + self.surname + ' поступил в ' + str(self.year_of_entrace) + ' ' + ' на факультет '+ self.department

student = Student('Alex', 'Terkin', 2014, 'Machine Learning')

print(student.get_student_info())
