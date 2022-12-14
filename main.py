class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
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
        stud_courses_in_progr = ', '.join(self.courses_in_progress)
        stud_finished_cours = ', '.join(self.finished_courses)
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за домашние задания: {self.avrg_mark(self.grades)}" \
               f"\nКурсы в процессе изучения: {stud_courses_in_progr}" \
               f"\nЗавершенные курсы: {stud_finished_cours}"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.grades = {}
        Lecturer.lecturer_list.append(self)

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
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Gogi', 'Tsaridze', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['English']

student_2 = Student('Sultan', 'Suleiman', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Statistics']

reviewer_1 = Reviewer('Egor', 'Letov')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2 = Reviewer('Anton', 'Ishutin')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']
reviewer_2.rate_hw(student_2, 'Git', 6)
reviewer_2.rate_hw(student_2, 'Python', 9)

lecturer_1 = Lecturer('Eric', 'Prydz')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']
student_1.rate_lecture(lecturer_1, 'Python', 9)
student_2.rate_lecture(lecturer_1, 'Python', 7)

lecturer_2 = Lecturer('Calvin', 'Harris')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']
student_1.rate_lecture(lecturer_2, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Python', 5)
student_2.rate_lecture(lecturer_2, 'Git', 5)

def avrg_grade_course(list_avg, course):
    sum_g = 0
    len_g = 0
    for element in list_avg:
        if course in element.grades.keys():
            sum_g += sum(list(map(int, element.grades[course])))
            len_g += len(list(map(int, element.grades[course])))
    avg = round(sum_g / len_g, 1)
    return avg

print(f'лектор Кальвин Харрис круче чем лектор Ерик Придз: {lecturer_1 > lecturer_2}\n')
print(student_1)
print()
print(lecturer_1)
print()
print(f'Средняя оценка студентов по дисциплине Python = {avrg_grade_course(Student.student_list, "Python")}')
print(f'Средняя оценка лекторов по дисциплине Git = {avrg_grade_course(Lecturer.lecturer_list, "Git")}')