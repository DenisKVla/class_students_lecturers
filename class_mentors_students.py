class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self,lecturer,course,grade):
        if isinstance(lecturer, Lecturer) and self.courses_in_progress and lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __avg_rate(self,grades):
        common_rate = 0
        count_rates = 0
        for course in grades:
            for grade in grades[course]:
                common_rate += grade
                count_rates +=1
        if count_rates != 0:
            avg_rates = common_rate/count_rates
            return avg_rates
        else:
            return "Error"


    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания:{self.__avg_rate(self.grades)}\n" \
              f"Курсы в процессе изучения:{','.join(self.courses_in_progress)}\n" \
              f"Завершенные курсы:{','.join(self.finished_courses)}"
        return res

    def compare_rates(self, student_two):
        if isinstance(student_two,Student):
            if self.__avg_rate(self.grades) > self.__avg_rate(student_two.grades):
                print(f"Средний бал {self.name} {self.surname} больше {student_two.name} {student_two.surname}")
            elif self.__avg_rate(self.grades) < self.__avg_rate(student_two.grades):
                print(f"Средний бал {student_two.name} {student_two.surname} больше {self.name} {self.surname}")
            else:
                print("Средний бал студентов одинаков")
        else:
            return "Error"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def __avg_rate(self,grades):
        common_rate = 0
        count_rates = 0
        for course in grades:
            for grade in grades[course]:
                common_rate += grade
                count_rates +=1
        avg_rates = common_rate/count_rates

        return avg_rates

    def __str__(self):
        name = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.avg_rate(self.grades)}"
        return name

    def compare_rates(self, lecturer_two):
        if isinstance(lecturer_two,Lecturer):
            if self.__avg_rate(self.grades) > self.__avg_rate(lecturer_two.grades):
                print(f"Средний бал {self.name} {self.surname} больше {lecturer_two.name} {lecturer_two.surname}")
            elif self.__avg_rate(self.grades) < self.__avg_rate(lecturer_two.grades):
                print(f"Средний бал {lecturer_two.name} {lecturer_two.surname} больше {self.name} {self.surname}")
            else:
                print("Средний бал лекторов одинаков")
        else:
            return "Error"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def rate_hw(self, student, course, grade):
        if isinstance(student,Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


first_lecturer = Lecturer("Willy", "Bradov")
first_student = Student("Ted","Mask","M")
first_reviewer = Reviewer("Mark","Menson")

second_lecturer = Lecturer("Fred","Novak")
second_student = Student("Den","Ninja","M")
second_reviewer = Reviewer("Harold","Rembrand")

first_lecturer.courses_attached = ["Python","Databases","Math"]
second_lecturer.courses_attached = ["C/C++","Hardware"]
first_reviewer.courses_attached = ["Python","C/C++"]
second_reviewer.courses_attached = ["Hardware","Databases"]
first_student.courses_in_progress = ["Python","Databases","C/C++"]
second_student.courses_in_progress = ["Hardware","Databases","C/C++"]

first_student.finished_courses = ["Math","Musics"]
first_student.rate_lecturer(first_lecturer,"Python",10)
first_student.rate_lecturer(first_lecturer,"Python",9)
first_student.rate_lecturer(first_lecturer,"Databases",8)
first_student.rate_lecturer(second_lecturer,"C/C++",9)

first_reviewer.rate_hw(first_student,"Python",9)
second_reviewer.rate_hw(second_student,"Databases",9)
second_reviewer.rate_hw(first_student,"Databases",10)

first_student.compare_rates(second_student)
first_lecturer.compare_rates(second_lecturer)

list_students = [first_student, second_student]
list_lecturers = [first_lecturer, second_lecturer]


def common_avg_rate_students(list_students,course):
    count = 0
    common_grade = 0
    for student in list_students:
        for key,grades in student.grades.items():
            if key == course:
                common_grade += sum(grades)
                count += len(grades)

    print(f"Средний бал по предмету {course} равен {common_grade/count}")

def common_avg_rate_lecturers(list_lecturers,course):
    count = 0
    common_grade = 0
    for lecturer in list_lecturers:
        for key, grades in lecturer.grades.items():
            if key == course:
                common_grade += sum(grades)
                count += len(grades)

    print(f"Средний бал лекторов по предмету {course} равен {common_grade/count}")

common_avg_rate_students(list_students,"Databases")
common_avg_rate_lecturers(list_lecturers,"Python")






