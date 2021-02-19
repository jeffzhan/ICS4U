import random

#added weekly_tasks for each employee based on their position (part-time, full-time, manager) through random choice

class ParttimeEmployee:
    
    def __init__(self, name, schedule, rate):
        self._name = name
        self._schedule = schedule #as a list of days

        self._hourly_rate = rate

    def __str__(self):
        return f'{self._name:<20} {self._schedule} ${self._hourly_rate}/hr'

    def __repr__(self):
        return f'ParttimeEmployee(name={self._name}, schedule={self._schedule}, rate={self._rate}'

    def name(self):
        return self._name

    def schedule(self):
        return " ".join(self._schedule)

    def changeSchedule(self, schedule):
        self._schedule = schedule

    def hourlyrate(self):
        return round(self._hourly_rate, 2)

    def raiseSalary(self, percentage):
        self._hourly_rate = round(self._hourly_rate * (1 + percentage/100), 2)

    def generate_weekly_paycheck(self, hours_worked):

        earnings = self._hourly_rate * hours_worked
        return earnings

    def generate_weekly_tasks(self):
        task_list = []
        for i in range(random.randint(2, 3)):
            task_list.append(random.choice(['prep', 'stock', 'grill', 'fry', 'serve', 'counter']))
        return task_list

class FulltimeEmployee:

    def __init__(self, name, schedule, rate):
        self._name = name
        self._schedule = schedule #as a list of days

        self._hourly_rate = rate

    def __str__(self):
        return f'{self._name:<20} {self._schedule} ${self._hourly_rate}/hr'

    def __repr__(self):
        return f'FulltimeEmployee(name={self._name}, schedule={self._schedule}, rate={self._rate}'

    def name(self):
        return self._name

    def schedule(self):
        return " ".join(self._schedule)

    def changeSchedule(self, schedule):
        self._schedule = schedule
        
    def hourlyrate(self):
        return round(self._hourly_rate, 2)

    def raiseSalary(self, percentage):
        self._hourly_rate = round(self._hourly_rate * (1 + percentage/100), 2)

    def generate_weekly_paycheck(self, hoursworked):
        earnings = self._hourly_rate * 40
        earnings += earnings * 0.10
        return earnings
    
    def generate_weekly_tasks(self):
        task_list = []
        for i in range(random.randint(2, 4)):
            task_list.append(random.choice(['cook', 'clean', 'grill', 'fry', 'train', 'supervise', 'supply tracking']))
        return task_list

class Manager:

    def __init__(self, name, schedule, salary):
        self._name = name
        self._schedule = schedule #as a list of days

        self._salary = salary

    def __str__(self):
        return f'{self._name:<20} {self._schedule} ${self._salary}/annum'

    def __repr__(self):
        return f'Manager(name={self._name}, schedule={self._schedule}, salary={self._rate}'

    def name(self):
        return self._name

    def schedule(self):
        return " ".join(self._schedule)

    def changeSchedule(self, schedule):
        self._schedule = schedule
        
    def hourlyrate(self):
        return round(self._salary/52/44, 2)

    def raiseSalary(self, percentage):
        self._salary = round(self._salary * (1 + percentage/100), 2)

    def generate_weekly_paycheck(self, hoursworked):
        earnings = self._salary / 52
        return earnings

    def generate_weekly_tasks(self):
        task_list = []
        for i in range(random.randint(3, 5)):
            task_list.append(random.choice(['supervise', 'organize', 'meeting', 'customer complaints', 'interview', 'leading', 'supply order', 'communication']))
        return task_list    


def make_random_schedule(num_days):
    days = ['M', 'T', 'W', 'H', 'F', 'S', 'S']
        
    schedule = []
    while len(schedule) < num_days:
        day = random.choice(days)
        if day not in schedule:
            schedule.append(day)

    return schedule

    
def make_random_employees():

    names = ['Nabeela Gentry', 
'Ishika Lutz', 
'Sullivan Johnston', 
'Rhiannan Lambert', 
'Elijah Odling', 
'Hanna Salazar', 
'Kimora Nicholson', 
'Siobhan Samuels', 
'Bianka Steadman', 
'Sianna Franco', 
'Sierra Greaves', 
'Ailish Pemberton', 
'Katie Luna', 
'Jak Garcia', 
'Summer-Louise Hughes', 
'Riley Hancock', 
'Garfield Moss', 
'Karishma Hodgson', 
'Darren Castaneda', 
'Tasneem Dalton', 
'Leanne Turner', 
'Priyanka Read', 
'Mahnoor Paine', 
'Savannah Lamb', 
'Waseem Wynn', 
'Ruben Hartley', 
'Izzie Richardson', 
'Cem Scott', 
'Eren Hood', 
'Marc Lane']

    employee_list = []

    for i in range(2):
        name = random.choice(names)
        names.remove(name)
        salary = random.randrange(50000, 80000, 10000)
        m = Manager(name, ['M', 'T', 'W', 'H', 'F'], salary)

        employee_list.append(m)

    for i in range(10):
        name = random.choice(names)
        names.remove(name)
        salary = random.randint(14, 25)
        f = FulltimeEmployee(name, make_random_schedule(5), salary)

        employee_list.append(f)

    for i in range(len(names)):
        name = random.choice(names)
        names.remove(name)
        salary = random.randint(11, 15)
        
        p = ParttimeEmployee(name, make_random_schedule(3), salary)

        employee_list.append(p)
        
    
    return employee_list


def run_payroll(employee_list):

    paycheck_info = []
    
    for employee in employee_list:
        #print(type(employee))
        
        hours = random.randint(10, 20)

        pay_info = employee.generate_weekly_paycheck(hours)

        weekly_tasks = employee.generate_weekly_tasks()

        paycheck_info.append([employee.name(), employee.schedule(), hours, pay_info, weekly_tasks])

    return paycheck_info

        
def main():

    list_of_employees = make_random_employees()
    for e in list_of_employees:
        print(e)

    paycheck_list = run_payroll(list_of_employees)

    for p in paycheck_list:
        print(p)



main()
    

        
