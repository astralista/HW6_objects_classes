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

    def avrg_mark(self, grades):
        a = 0
        b = 0
        for j in grades:
            a += sum(grades[j])
            b += len(grades[j])
        return round(a / b, 1)

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за лекции: {self.avrg_mark(self.grades)}"


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

fine_lecturer = Lecturer('John', 'Dow')
fine_lecturer.courses_attached += ['Python']
best_student.rate_lecture(fine_lecturer, 'Python', 8)

some_lecturer = Lecturer('Eric', 'Prydz')
some_lecturer.courses_attached += ['Techno']
best_student.rate_lecture(some_lecturer, 'Techno', 6)

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Techno']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Techno', 2)
cool_mentor.rate_hw(best_student, 'Techno', 8)

# print(best_student.grades)
# print(best_student.finished_courses)
# print(f"student {best_student.name} gave the teacher {fine_lecturer.name} {fine_lecturer.surname} {fine_lecturer.grades}")
# print(some_lecturer.grades)
#
# best_student.courses_in_progress += ['Techno']
# best_student.rate_lecture(some_lecturer, 'Techno', 10)
print(some_lecturer)
# print(best_student)

