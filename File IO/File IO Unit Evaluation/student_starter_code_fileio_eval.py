#QUESTION 1

#Required function to complete


def create_wine_dictionary(filename):
    wine_dict = {}
        
    with open(filename, encoding='utf8') as fileIn:
        fileIn.readline()
        
        for line in fileIn:
            line = line.strip()
            data = line.split('\t')
            #['50', 'Italy', 'Riserva', '90', '100', 'Tuscany', 'Sangiovese', 'Capanne Ricci']
            #['0', 'US', "Martha's Vineyard", '96', '235', 'California', 'Cabernet Sauvignon', 'Heitz']
            country = data[1]
            winery = data[7]
            designation = data[2]
            price = data[4]
            
            #country
            if country not in wine_dict:
                wine_dict[country] = {}

            #winery_desig
            winery_designation = (f'{winery} | {designation}')


            if price == '':
                wine_dict[country][winery_designation] = None
            else:
                wine_dict[country][winery_designation] = int(price)
            
    return wine_dict


#Not required to complete. Can be used for testing purposes
##def print_wine_dictionary(wine_dict):
##    print(wine_dict)

#MAIN
#Remember to comment out any 'MAIN' code found below this line.
##all_wines = create_wine_dictionary("winemag.txt")
##print_wine_dictionary(all_wines)




#QUESTION 2

import random
import csv


def get_course_list(filename):
    course_list = []

    with open(filename, encoding='utf8') as fileIn:
        for line in fileIn:
            course_list.append(line.strip())
            
    return course_list
    


def get_student_names(filename):
    student_names = []

    with open(filename, encoding='utf8') as fileIn:
        for line in fileIn:
            student_names.append(line.strip().split())

    return student_names
            


def get_schedule(all_courses_list):
    schedule = []
    schedule = (random.sample(all_courses_list, 4))

    return schedule



def generate_student_schedules(filename, all_courses_list, all_students_list):

    with open(filename, "w", encoding='utf-8', errors='ignore', newline='') as scheduleOut:

        writer = csv.writer(scheduleOut)

        for student in all_students_list:
            schedule = get_schedule(all_courses_list)
            first_name = student[0]
            last_name = student[1]
            li = [first_name, last_name] + schedule

            writer.writerow(li)


#MAIN
#Remember to comment out any 'MAIN' code found below this line.
courses_list = get_course_list("courses.txt")
names_list = get_student_names("student_names.txt")

generate_student_schedules("irhs_schedules.csv", courses_list, names_list)


    
    





    
