# #PETS - POSTIONAL ARGUMENTS
# def describe_pets(pet_name, animal_type='dog'):
#     """Display information about your pet"""
#     print(f"\nI have {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# my_pet = describe_pets('harry', 'hamster')
# my_pet = describe_pets(pet_name='harry', animal_type='hamster') # default value argument
# my_pet = describe_pets(animal_type='hamster', pet_name='harry') # keyword argument
# my_pet = describe_pets('willie') # default value argument
# my_pet = describe_pets(pet_name='willie') # default value argument
# #my_pet = describe_pets()

#print(my_pet)

#RETURN VALUES
#RETURNING A DICTIONARY TO A FUNCTION

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly foramatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix', 'bee')
musician = get_formatted_name('joseph', 'mensah')
print(musician)



def build_person(first_name, last_name,age=None, occupation=None):
    """Return a dictionary of information about a person"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    if occupation:
        person['occupation'] = occupation
    return person

musician = build_person('jimi', 'hendrix', 25, 'programmer')
print(musician)


# USING DICTIONARIES WITH WHILE LOOPS
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly foramatted"""
    full_name = f"{first_name}  {last_name}"
    return full_name.title()

#This is an infinite loop
while True:
    print("\nPlease tell me your name")
    print("\nEnter 'q' to quit the program")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")



# PASSING A LIST

def greet_users(names):
    """Pass a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'joe']
greet_users(usernames)

# WITHOUT USING FUNCTIONS
# Start with designs that needs to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each designs until none is left
# Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"\nPrinting Model: {current_design}")
    completed_models.append(current_design)

# Display all completed Models
print("\nThe following models have been printed")
for completed_model in completed_models:
    print(completed_model)


#USING FUNCTIONS TO ORGANIZE THE ABOVE CODE

# first function takes care of printing the models
def print_models(unprinted_designs, completed_models):
    """Simulate printing each designs until none is left
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"\nPrinting Models: {current_design}")
        completed_models.append(current_design)

# second function displays the models after printing
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



# PASSING ARBITRARY NUMBER OF ARGUMENTS
def make_pizza(*toppings):
    """Print list of toppings that have been provided"""
    print(toppings)


topping = make_pizza('pepperoni')
topping = make_pizza('mushrooms', 'green peppers', 'extra cheese')
print(topping)


def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")


top = make_pizza('pepperoni')
top = make_pizza('mushrooms', 'green peppers', 'extra cheese')
print(top)

# MIXING POSTIONAL AND ARBITRARY ARGUMENTS


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")


top = make_pizza(16, 'pepperoni')
top = make_pizza(25,'mushrooms', 'green peppers', 'extra cheese')
print(top)


# USING AN ARBITRARY KEYWORD ARGUMENTS
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='Princeton', field='physics')
print(user_profile)