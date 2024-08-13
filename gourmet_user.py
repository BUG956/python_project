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

#1.
restaurant = Restaurant('Culinary Delight', 'Gourmet')
print('number served: ', restaurant.number_served)
restaurant.number_served = 5
print('changed number served: ', restaurant.number_served)

#2.
restaurant.set_number_served(10)
print('set number served: ', restaurant.number_served)

#3.
restaurant.increment_number_served(100)
print('incremented number served: ', restaurant.number_served)

#5.
user01 = User('Alex', 'Johnson')
user01.increment_login_attempts()
user01.increment_login_attempts()
user01.increment_login_attempts()
print('login attempts: ', user01.login_attempts)
user01.reset_login_attempts()
print('login attempts: ', user01.login_attempts)
