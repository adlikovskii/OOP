class Student:
    GPA = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.GPA = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            lecturer.GPA = lecturer.GPA + [grade]
            Lecturer.GPA = Lecturer.GPA + [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return ('Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за домашние задания: '
                + str(comparison(self)) + '\nКурсы в процессе изучения: : ' +
                ', '.join(self.courses_in_progress) + '\nЗавершенные курсы: ' + ', '.join(self.finished_courses))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.GPA = []


class Lecturer(Mentor):
    GPA = []

    def __str__(self):
        return ('Имя: ' + self.name + '\nФамилия: ' + self.surname + '\nСредняя оценка за лекции: '
                + str(comparison(self)))


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.GPA = student.GPA + [grade]
            Student.GPA = Student.GPA + [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: ' + self.name + '\nФамилия: ' + self.surname


def comparison(person):
    return sum(person.GPA) / len(person.GPA)


def comparison_students_course(list_students, course):
    csa = []
    for i in list_students:
        csa = csa + i.grades[course]
    return sum(csa) / len(csa)


def comparison_lecturer_course(list_lecturers, course):
    cla = []
    for i in list_lecturers:
        cla = cla + i.grades[course]
    return sum(cla) / len(cla)


some_reviewer_1 = Reviewer('Some', 'Buddy')
some_reviewer_1.courses_attached += ['Python', 'Git']

some_reviewer_2 = Reviewer('Buddy', 'Some')
some_reviewer_2.courses_attached += ['Python', 'Git']

some_lecturer_1 = Lecturer('Some', 'Buddy')
some_lecturer_1.courses_attached += ['Python']

some_lecturer_2 = Lecturer('Buddy', 'Some')
some_lecturer_2.courses_attached += ['Python']

some_student_1 = Student('Ruoy', 'Eman', 'your_gender')
some_student_1.courses_in_progress += ['Python', 'Git']
some_student_1.finished_courses += ['Введение в программирование']

some_student_2 = Student('Eman', 'Ruoy', 'your_gender')
some_student_2.courses_in_progress += ['Python']

some_reviewer_2.rate_hw(some_student_2, 'Python', 10)
some_reviewer_2.rate_hw(some_student_2, 'Python', 9.9)
some_reviewer_2.rate_hw(some_student_2, 'Python', 9.8)

some_reviewer_1.rate_hw(some_student_1, 'Python', 10)
some_reviewer_1.rate_hw(some_student_1, 'Python', 9.9)
some_reviewer_1.rate_hw(some_student_1, 'Python', 9.8)

some_student_1.rate_hw(some_lecturer_1, 'Python', 10)
some_student_1.rate_hw(some_lecturer_1, 'Python', 9.9)
some_student_1.rate_hw(some_lecturer_1, 'Python', 9.8)

some_student_2.rate_hw(some_lecturer_2, 'Python', 10)
some_student_2.rate_hw(some_lecturer_2, 'Python', 9.9)
some_student_2.rate_hw(some_lecturer_2, 'Python', 9.8)

# Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
print(comparison_students_course([some_student_2, some_student_1], 'Python'))
# Подсчет средней оценки за лекции всех лекторов в рамках курса
print(comparison_lecturer_course([some_lecturer_1, some_lecturer_2], 'Python'))
