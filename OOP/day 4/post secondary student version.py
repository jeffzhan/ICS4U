
import random

#both college and university classes are polymorphic because they both have the same function(accept_applications) and this function both has a similar purpose but does it differently for both

class PostSecondary:

    def __init__(self, name):
        self._name = name
        self._students = []
        self._applicants = []
    
    def name(self):
        return self._name

    def type(self):
        return self._type

    def __str__(self):
        return (f'{self._name} with {len(self._students)} students enrolled')

    def __repr__(self):
        return (f'class PostSecondary: name={self._name}, students={self._students}, applicants={self._applicants}')

    def print_applicants(self):
        s = ""
        for a in self._applicants:
            s += a.__str__() + "\n"
        return s

    def get_applicants(self):
        return self._applicants

    def print_students(self):
        s = ""
        for a in self._students:
            s += a.__str__() + "\n"
        return s

    def get_students(self):
        return self._students
      
    def add_student(self, student):
        if student not in self._students:
            self._students.append(student)

    def add_applicant(self, applicant):
        if applicant not in self._applicants:
            self._applicants.append(applicant)

    def reject_application(self, applicant):
        if applicant in self._applicants:
            self._applicants.remove(applicant)

class Student:

    def __init__(self, name, courses, average):
        self._name = name
        self._courses = courses
        self._average = average

    def name(self):
        return self._name

    def courses(self):
        return self._courses

    def average(self):
        return self._average

    def __str__(self):
        return (f'{self._name:<10}, average={self._average:<4}, courses={self._courses}')

    def __repr__(self):
        return (f'class Student name={self._name}, avg={self._average}, courses={self._courses}')



class College(PostSecondary):

    def accept_applications(self, applicants):
        for student in applicants:
            if student.average() >= 80 and ('ENG4U' in student.courses() or 'ENG4C' in student.courses()) and ('MHF4U' in student.courses() or 'MCT4M' in student.courses()):
                self._students.append(student)

  
class University(PostSecondary):

    def accept_applications(self, applicants):
        for student in applicants:
            if student.average() >= 85 and 'ENG4U' in student.courses() and 'MHF4U' in student.courses() and 'ICS4U' in student.courses():
                self._students.append(student)



def generate_random_students():
    names = ['Nabeela Gentry', 'Ishika Lutz', 'Sullivan Johnston', 'Rhiannan Lambert', 'Elijah Odling', 'Hanna Salazar', 'Kimora Nicholson', 'Siobhan Samuels', 'Bianka Steadman', 'Sianna Franco', 'Sierra Greaves', 'Ailish Pemberton', 'Katie Luna', 'Jak Garcia', 'Summer-Louise Hughes', 'Riley Hancock', 'Garfield Moss', 'Karishma Hodgson', 'Darren Castaneda', 'Tasneem Dalton', 'Leanne Turner', 'Priyanka Read', 'Mahnoor Paine', 'Savannah Lamb', 'Waseem Wynn', 'Ruben Hartley', 'Izzie Richardson', 'Cem Scott', 'Eren Hood', 'Marc Lane']
    courses = ["MHF4U", "ENG4U", "ICS4U", "MCT4M", "ENG4C", "MDM4U", "EWC4U"]

    all_students = []

    for n in names:
        
        #pick 4 unique courses
        courseList = []
        while len(courseList) < 4:
            c = random.choice(courses)
            if c not in courseList:
                courseList.append(c)

        avg = random.choice([70, 75, 80, 85, 90, 95])

        s = Student(n, courseList, avg)
        all_students.append(s)

    return all_students


def load_applicants(institution, list_students):

    for current_student in list_students:
        institution.add_applicant(current_student)
        
        
def main():
    
    #imagine that we created even more institutions
    guelph_university = University("Guelph Univeristy")
    mohawk_college = College("Mohawk College")
    all_postsecondary = [guelph_university, mohawk_college]
    
    #generate random students
    all_students = generate_random_students()

    #add applications to institution database
    for institution in all_postsecondary:
        load_applicants(institution, all_students)
    
    
    for institution in all_postsecondary:
        print(f'\n\n{institution.name()}')
        print("Applicants are")
        print("-"*30)
        print(institution.print_applicants())

    

    #perform the acceptance check for applicants
    for institution in all_postsecondary:
        institution.accept_applications(all_students)
        

    for institution in all_postsecondary:
        print(f'\n\n{institution.name()}')
        print("Acceptances go out to")
        print("-"*30)
        print(institution.print_students())


main()

