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

city  = describe_city('accra')
city = describe_city(city_name='takoradi')
city = describe_city(city_name='abidjan', country='ivory coast')
print(city)

# 8-6 CITY NAMES
def city_country(city_name, country):
    """Return a well formatted city and the corresponding country"""
    city = f"{city_name} {country}"
    return city.title()

country_city = city_country("'santiago',", "'chile'")
country_city = city_country("'accra',", "'ghana'")
country_city = city_country("'manchester',", "'england'")
print(country_city)


# 8-7 ALBUMS

def make_album(artist_name, album_title, No_songs=None):
    """Return a dictionary of an artist and album"""
    music_album = {'artist':artist_name, 'album title':album_title}
    if No_songs:
        music_album['No_songs'] = No_songs
    return music_album


catalog = make_album('Sarkodie', 'Mary', 5)
print(catalog)
catalog = make_album('Kidi', 'Golden Boy')
print(catalog)


# 8-8 USER ALBUMS

def make_album(artist_name, album_title, No_songs=None):
    """Return a dictionary of an artist and album"""
    music_album = {'Artist':artist_name, 'Album_title':album_title}
    return music_album


#infinite loop
while True:
    print("\nPrint Artist Details:")
    print("(Enter 'q' anywhere to quit)")
    art_name = input("Enter artist name: ")
    if art_name == 'q':
        break
    alb_name = input("Enter artist album name: ")
    if alb_name == 'q':
        break


    formatted_catalog = make_album(art_name, alb_name)
    print(f"{formatted_catalog}")

# 8-9 MESSAGES
def show_messages(messages):
    """Passing a list of messages"""
    for message in messages:
        msg = f"{message.title()}"
        print(msg)

short_msgs = ['hello pal', 'call me', 'am busy']
show_messages(short_msgs)

# 8-10 SENDING MESSAGES
def send_messages(unsent_msgs, sent_messages):
    """Passing a list of text messages """
    while unsent_msgs:
        current_messages = unsent_msgs.pop()
        print(f"\nPrinting unsent messages: {current_messages}")
        sent_messages.append(current_messages)


def show_sent_messages(sent_messages):
    """Display sent messages"""
    print(f"\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message)


unsent_msgs = ['hello pal', 'call me later', 'am busy']
sent_messages = []

send_messages(unsent_msgs, sent_messages)
show_sent_messages(sent_messages)

# 8--11 ARCHIVED MESSAGES
def send_messages(unsent_msgs, sent_messages):
    """Passing a list of text messages """
    while unsent_msgs:
        current_messages = unsent_msgs.pop()
        print(f"\nPrinting unsent messages: {current_messages}")
        sent_messages.append(current_messages)


def show_sent_messages(sent_messages):
    """Display sent messages"""
    print(f"\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message)


unsent_msgs = ['hello pal', 'call me later', 'am busy']
sent_messages = []

send_messages(unsent_msgs[:], sent_messages)
show_sent_messages(sent_messages)


# 8-12 SANDWICHES

def make_sandwich(*sandwich_items):
    """Build sandwich items and describe them"""
    print("\nMaking ordered sandwich items...")
    for item in sandwich_items:
        print(f"-{item}")

sand_item = make_sandwich("pepperoni")
sand_item = make_sandwich("cheese", "green pepper", "orange")
sand_item = make_sandwich("mushrooms", "pepper", "fruits")
print(sand_item)


# 8-13 BUILD PROFILE

def build_profile(first_name, last_name, **kwargs):
    """Building profile about a person."""
    kwargs['first_name'] = first_name
    kwargs['last name'] = last_name
    return kwargs

user_profile = build_profile('Degrasse', 'Tyson', location='United States', fields= 'Astrophysics', Born='1975')
print(user_profile)

# 8- 14 CARS

def car_info(manufacturer, model_name, **kwargs):
    """Describe different car models"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model name'] = model_name
    return kwargs


car_profile = car_info('Volkswaggen','Y-21', location='Germany', color='Aurbegine', tow_package=True)
print(car_profile)

car_profile = car_info('Buggati', 'Veron', location='USA', color='Mate Green', tow_package=True)
print(car_profile)

# EXERCISE 6.14

data = 'X-DSPAM-Confidence:0.8475'
colon = data.find(':')
print(colon)
num = data[colon + 1:]
print(num)
print(float(num)) # Converts string(num) to floating point number


# 10-1 LEARNING PYTHON 
