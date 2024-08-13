'''Note: copied show_privileges instead of moving so as not to break code for #7'''
class User():
    '''class that defines a user'''
    def __init__(self, first, last, dept='Unassigned', pnum='n/a'):
        self.first_name = first
        self.last_name = last
        self.fullname = first + ' ' + last
        self.email = first + '.' + last + '@usergroup.com'
        self.department = dept
        self.phone = pnum
        self.login_attempts = 0

    def describe_user(self):
        '''prints a user's information'''
        print('Name: ', self.fullname)
        print('Department: ', self.department)
        print('Email: ', self.email)
        print('Phone: ', self.phone)

    def greet_user(self):
        '''prints a greeting to a user'''
        print('Greetings, ', self.first_name, '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        '''prints privileges for #12, marked as "class" to differentiate'''
        print('privileges (class): ', self.privileges)    

class Admin(User):

    def __init__(self, first, last, dept='Unassigned', pnum='n/a'):
        super().__init__(first, last, dept='Unassigned', pnum='n/a')
        #privileges attribute here for #7
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        #privileges from class for #12
        self.priv = Privileges()

    def show_privileges(self):
        '''prints privileges for #7'''
        print('privileges: ', self.privileges)

class Restaurant():
    '''A class that defines a restaurant'''
    def __init__(self, rname, ctype):
        self.restaurant_name = rname
        self.cuisine_type = ctype
        self.number_served = 0

    def describe_restaurant(self):
        '''Prints a description of the restaurant name and cuisine.'''
        print('Restaurant Name: ', self.restaurant_name)
        print('Cuisine Type: ', self.cuisine_type)
    
    def open_restaurant(self):
        '''Prints message that the restaurant is open'''
        print(self.restaurant_name, ' is open.')

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, customers=1):
        self.number_served += customers

class IceCreamStand(Restaurant):

    def __init__(self, rname, ctype):
        super().__init__(rname, ctype)
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Neapolitan']

    def show_flavors(self):
        print('Flavors: ', self.flavors)

#3.
iscream = IceCreamStand('Frosty Delights', 'ice cream')
iscream.show_flavors()

#8.
admin1 = Admin('Jerry', 'Arias')
admin1.show_privileges()

#12.
admin2 = Admin('Steve', 'Arias')
admin2.priv.show_privileges()
