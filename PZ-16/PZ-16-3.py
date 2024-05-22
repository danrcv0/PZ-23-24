


import pickle


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

def save_def(students):
    with open('students_info.pickle', 'wb') as file:
        pickle.dump(students, file)

def load_def():
    with open('students_info.pickle', 'rb') as file:
        return pickle.load(file)

# Создание объектов класса Student
student1 = Student("Иван", "Иванов", [5, 4, 4, 5, 5])
student2 = Student("Петр", "Петров", [4, 3, 5, 4, 4])
student3 = Student("Мария", "Сидорова", [5, 5, 5, 5, 5])

# Сохранение информации об объектах в файл
save_def([student1, student2, student3])

# Загрузка информации из файла
loaded_students = load_def()

for student in loaded_students:
    print(f"{student.first_name} {student.last_name}:")
    print(f"Оценки: {student.grades}")
    print(f"Средний балл: {student.calculate_average_grade()}")
    if student.is_excellent_student():
        print("Студент отличник")
    else:
        print("Студент не отличник")
    print()
