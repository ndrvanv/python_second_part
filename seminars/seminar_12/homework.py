import csv

class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError("ФИО должно содержать только буквы")
        if not value.istitle():
            raise ValueError("ФИО должно содержаться с заглавной буквы")
        instance._name = value


class Student:
    name = NameDescriptor()

    def __init__(self, subjects_file):
        self.subjects = self.load_subjects(subjects_file)
        self.grades = {subject: [] for subject in self.subjects}
        self.test_results = {subject: [] for subject in self.subjects}

    def load_subjects(self, subjects_file):
        with open(subjects_file, "r") as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.grades[subject].append(grade)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет")
        if result < 0 or result > 100:
            raise ValueError("Результат теста должне быть от 0 до 100")
        self.test_results[subject].append(result)


    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет")
        test_scores = self.test_results[subject]
        if not test_scores:
            return 0
        return sum(test_scores) / len(test_scores)

    def overall_average_grade(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

student = Student("subjects.csv")
student_name = "Иванов Иван Иванович"
print(student.name)


student.add_grade("English", 4)
student.add_grade("Geometry", 5)
student.add_test_result("English", 90)
student.add_test_result("Geometry", 80)

print(student.average_test_score("Ehglish"))
print(student.average_test_score("Geometry"))
print(student.overall_average_grade())
