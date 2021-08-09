
class Student:
    list_students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.list_students.append(self)
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__ (self, other):
        if not isinstance( other, Student):
            print (f'не является студентом')
            return
        return sum(self.grades['Python']) / len(self.grades['Python']) > sum(other.grades['Python']) / len(self.grades['Python'])

    def __str__(self):
        res = (f'''Имя: {self.name}\nФамилия: {self.surname}
Средняя оценка за лекции: {count_average_grade(self)}
Курсы в процессе изучения: {self.courses_in_progress}
Завершенные курсы: Введение в программирование{self.finished_courses}\n''')
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    list_lecturers = []
    def __init__(self, name, surname):
            super().__init__(name, surname)
            self.grades = {}
            self.list_lecturers.append(self)

    def __str__(self):
        res = f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {count_average_grade(self)}\n'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'не является лектором')
            return
        return sum(self.grades['Python']) / len(self.grades['Python']) > sum(other.grades['Python']) / len(other.grades['Python'])

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''Имя: {self.name}\nФамилия: {self.surname}\n'''
        return res


def count_average_grade(self):
    len_1 = 0
    summ = 0
    for grade in self.grades:
        summ += sum(self.grades[grade])
        len_1 += len(self.grades[grade])    # average_grade = float(summ/len)
    average_grade = float(summ/len_1)
    return average_grade

def count_grade_students(lecturers, course):
    avarege_grade = 0
    counter = 0
    for lecturer in lecturers:
        for course_1 in lecturer.grades:
            if course in course_1:
                counter += 1 * len(lecturer.grades[course])
                avarege_grade += sum(lecturer.grades[course])
    avarege_grade = float(avarege_grade /counter)
    print(f'средняя оценка студентов: {avarege_grade}')

def count_grade_lecturers(students, course):
    avarege_grade = 0
    counter = 0
    for student in students:
        for course_1 in student.grades:
            if course in course_1:
                counter += 1 * len(student.grades[course])
                avarege_grade += sum(student.grades[course])
    avarege_grade = float(avarege_grade /counter)
    print(f'средняя оценка лекторов: {avarege_grade}')
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'java']

student_2 = Student('Vasya', 'Pupkin', 'your_gender')
student_2.courses_in_progress += ['Python', 'C++']


reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'C++']

reviewer_2 = Reviewer('Bill', 'Murey')
reviewer_2.courses_attached += ['Python', 'java']

lecturer_1 = Lecturer('Max', 'Pain')
lecturer_1.courses_attached += ['Python', 'C++']

lecturer_2 = Lecturer('Phill', 'Jonson')
lecturer_2.courses_attached += ['Python', 'java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'C++', 10)

student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_1, 'C++', 7)
student_1.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_1, 'C++', 10)

print(student_1)
print(lecturer_1)
print(reviewer_1)

count_grade_students(Student.list_students, 'Python')
count_grade_lecturers(Lecturer.list_lecturers, 'Python')

print(student_1 > student_2)
print(lecturer_1 < lecturer_2)



