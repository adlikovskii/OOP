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


some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 9.9)
some_reviewer.rate_hw(some_student, 'Python', 9.8)

some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 9.9)
some_student.rate_hw(some_lecturer, 'Python', 9.8)

print(f'{some_reviewer}\n\n{some_lecturer}\n\n{some_student}\n')

# Сравнение лекторов и студентов
print(comparison(some_student) > comparison(some_lecturer))
# Для сравнения всех лекторов и студентов я добавил общий показатель
print(comparison(Lecturer) == comparison(Student))

