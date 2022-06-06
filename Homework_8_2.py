import operator


class Student:
    def __init__(self, full_name, age, grade, subscribed_course):
        self.full_name = full_name
        self.age = age
        self.grade = grade
        self.subscribed_course = subscribed_course
        self.homeworks = []


first_student = Student('Victoria Petrivna Smith', 25, 4, 'Math')
second_student = Student('Olga Andriivna Miller', 28, 5, 'English literature')
third_student = Student('Petro Petrovych Kovalenko', 21, 3, 'Science')
fourth_student = Student('Steve Ivanovych Ivanov', 32, 4, 'Geography')
fifth_student = Student('Inna Olehivna Petruk', 23, 5, 'Physics')


def sort_students():
    list_of_students = [first_student, second_student, third_student, fourth_student, fifth_student]
    sorted_students = sorted(list_of_students, key=operator.attrgetter('grade'))
    for student in sorted_students:
        print(student.full_name, student.age, student.grade, student.subscribed_course)


sort_students()


class Homework:
    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status


    def describe_homework(self):
        print(f"{self.name}, {self.description}, {self.complexity}, {self.status}")

    def status_change(self, new_status):
        self.status = new_status
        print(f"Status of {self.name} has been changed to {self.status}")


a = Homework('homework1', 'description of homework 1 ', 'easy', 'passed')
b = Homework('homework 2', 'description of homework 2', 'hard', 'not passed')
a.describe_homework()
b.describe_homework()
a.status_change('not passed')
b.status_change('passed')
