# 7-8 DELI
# Start with a list of sandwiches and an empty list
# of ssandwiches to be finished.
# sandwich_orders = ['fish', 'tuna', 'cabbage', 'cheese']
# finished_sandwiches = []

# while sandwich_orders:
#     current_order = sandwich_orders.pop()

#     print(f"I've made your {current_order.title()} sandwich ")
#     finished_sandwiches.append(current_order)

#     #Display the finished sandwiches
#     print("\nThese sandwiches are finished: ")
#     for sandwich in finished_sandwiches:
#         print(sandwich.title())


# 7-9 NO PASTRAMI
# sandwich_orders = ['fish', 'tuna','pastrami', 'cabbage', 'cheese', 'pastrami', 'corn', 'pastrami']
# finished_sandwiches = []

# # DELI has run out of pastrami
# no_pastrami = ("Deli has run out of pastrami")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     current_order = sandwich_orders.pop()

#     print(f"I've made your {current_order.title()} sandwich ")
#     finished_sandwiches.append(current_order)

#     #Display the finished sandwiches
#     print("\nThese sandwiches are finished: ")
#     for sandwich in finished_sandwiches:
#         print(sandwich.title())


# 7-10 DREAM VACATION

# user_responses = {}

# #Set a flag to indicate the poll is active
# poll_active = True

# while poll_active:
#     #Prompt users for their name and responses
#     name = input("\nEnter your name: ")
#     response = input("\nIf you could visit one place in this world, where would it be? ")

#     #Store the response in a dictionary
#     user_responses[name] = response

#     # Find out if anyone else would take the poll
#     repeat_poll = input("Would you like to let another person respond? (yes/no) ")
#     if repeat_poll == 'no':
#         poll_active = False

# # Polling is complet.Show the results.
# print("\n---------POLL RESULT---------")
# for name, response in user_responses.items():
#     print(f"{name.title()} would like to visit {response.title()} someday")


#   FUNCTIONS
#8-1 Messages
def display_message(message):
    """Display a message of what you're learning"""
    print(f"\n Hello folks, am currently learning {message}")

message_display = display_message('Function parameters and arguments')
print(message_display)

#8-2 Favorite bokks

def favorite_books(book):
    """Display info about your favorite book"""
    print(f"\n My favorite book us called '{book.title()}'")

my_favorite = favorite_books('Alice in wonderland')
print(my_favorite)

# 8-3 T-SHIRTS
def make_shirt(message='i love python', size='large'):
    """Describe the shirt"""
    print(f"\n My shirt is of size '{size}' and has the message '{message.title()}', written behind it")

shirt = make_shirt('small', 'an eye for an eye makes the world go blind')
shirt = make_shirt(size='small', message='an eye for an eye makes the world go blind')
shirt = make_shirt()
shirt = make_shirt(size='medium')
shirt = make_shirt(size='extra large', message='I love cybersecurity')
print(shirt)


# 8-5 CITIES
def describe_city(city_name, country='ghana'):
    """Describe the city"""
    print(f"{city_name.title()} is in {country.title()}")

city  = describe_city('acra')
city = describe_city(city_name='takoradi')
city = describe_city(city_name='abidjan', country='ivory coast')
print(city)