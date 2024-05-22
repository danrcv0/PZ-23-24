
"""27. Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником."""



class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_excellent_student(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 5


student1 = Student("Иван", "Иванов", [5, 5, 5, 5, 5])
student2 = Student("Петр", "Петров", [3, 4, 5, 4, 3])

print(f"{student1.first_name} {student1.last_name} средний балл: {student1.calculate_average_grade()}")
print(f"{student1.first_name} {student1.last_name} является отличником: {student1.is_excellent_student()}")

print(f"{student2.first_name} {student2.last_name} средний балл: {student2.calculate_average_grade()}")
print(f"{student2.first_name} {student2.last_name} является отличником: {student2.is_excellent_student()}")