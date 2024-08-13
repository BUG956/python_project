class Person():
    '''class that defines a person'''
    def __init__(self, first, last, dept='Unassigned', pnum='n/a'):
        self.first_name = first
        self.last_name = last
        self.fullname = first + ' ' + last
        self.email = first + '.' + last + '@usergroup.com'
        self.department = dept
        self.phone = pnum
        self.login_attempts = 0

    def describe_person(self):
        '''prints a person's information'''
        print('Name: ', self.fullname)
        print('Department: ', self.department)
        print('Email: ', self.email)
        print('Phone: ', self.phone)

    def greet_person(self):
        '''prints a greeting to a person'''
        print('Greetings, ', self.first_name, '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Permissions():
    '''defines basic permissions for an administrative person'''
    def __init__(self):
        self.permissions = ['can add post', 'can delete post', 'can ban user']

    def show_permissions(self):
        '''method for printing permissions'''
        print('Permissions: ', self.permissions)    

class Admin(Person):

    def __init__(self, first, last, dept='Unassigned', pnum='n/a'):
        super().__init__(first, last, dept='Unassigned', pnum='n/a')
        #permissions from class for #12
        self.perm = Permissions()

class Eatery():
    '''A class that defines an eatery'''
    def __init__(self, ename, ctype):
        self.eatery_name = ename
        self.cuisine_type = ctype
        self.number_served = 0

    def describe_eatery(self):
        '''Prints a description of the eatery name and cuisine.'''
        print('Eatery Name: ', self.eatery_name)
        print('Cuisine Type: ', self.cuisine_type)
    
    def open_eatery(self):
        '''Prints message that the eatery is open'''
        print(self.eatery_name, ' is open.')

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, customers=1):
        self.number_served += customers

class IceCreamParlor(Eatery):

    def __init__(self, ename, ctype):
        super().__init__(ename, ctype)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Neapolitan']

    def show_flavors(self):
        print('Flavors: ', self.flavors)

#creates ice cream parlor and shows its flavors
parlor = IceCreamParlor('Parlor Delight', 'ice cream')
parlor.show_flavors()

#Shows permissions
admin1 = Admin('Alice', 'Johnson')
admin1.perm.show_permissions()

admin2 = Admin('Bob', 'Smith')
admin2.perm.show_permissions()
