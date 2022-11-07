class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def avrg_mark(self, grades):
        a = 0
        b = 0
        for j in grades:
            a += sum(grades[j])
            b += len(grades[j])
        return round(a / b, 1)
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент')
            return
        return self.avrg_mark(self.grades) < other.avrg_mark(other.grades)

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за домашние задания: {self.avrg_mark(self.grades)}" \
               f"\nКурсы в процессе изучения: {self.courses_in_progress}" \
               f"\nЗавершенные курсы: {self.finished_courses}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.grades = {}


    def av_mark(self, grades):
        a = 0
        b = 0
        for value in grades:
            a += sum(grades[value])
            b += len(grades[value])
        return round(a / b, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор')
            return
        return self.av_mark(self.grades) < other.av_mark(other.grades)

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за лекции: {self.av_mark(self.grades)}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Techno']
best_student.finished_courses += ['English']

eric_clapton = Student('Eric', 'Clapton', 'man')
eric_clapton.courses_in_progress += ['Python']
eric_clapton.courses_in_progress += ['Techno']

john_dow = Lecturer('John', 'Dow')
john_dow.courses_attached += ['Python']
best_student.rate_lecture(john_dow, 'Python', 8)

eric_prydz = Lecturer('Eric', 'Prydz')
eric_prydz.courses_attached += ['Techno']
best_student.rate_lecture(eric_prydz, 'Techno', 6)
best_student.rate_lecture(eric_prydz, 'Techno', 10)
best_student.rate_lecture(eric_prydz, 'Techno', 10)
best_student.rate_lecture(eric_prydz, 'Techno', 10)

some_buddy = Reviewer('Some', 'Buddy')
some_buddy.courses_attached += ['Python']
some_buddy.courses_attached += ['Techno']

some_buddy.rate_hw(best_student, 'Python', 10)
some_buddy.rate_hw(best_student, 'Python', 10)
some_buddy.rate_hw(best_student, 'Python', 10)
some_buddy.rate_hw(best_student, 'Techno', 2)
some_buddy.rate_hw(best_student, 'Techno', 8)
some_buddy.rate_hw(eric_clapton, 'Techno', 8)
some_buddy.rate_hw(eric_clapton, 'Techno', 5)
some_buddy.rate_hw(eric_clapton, 'Techno', 5)
some_buddy.rate_hw(eric_clapton, 'Python', 4)
some_buddy.rate_hw(eric_clapton, 'Python', 10)

best_student.courses_in_progress += ['Techno']
best_student.rate_lecture(eric_prydz, 'Techno', 10)

# print(best_student)
# print(eric_clapton)
print(eric_clapton < best_student)



