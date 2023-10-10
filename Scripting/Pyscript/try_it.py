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

user_responses = {}

#Set a flag to indicate the poll is active
poll_active = True

while poll_active:
    #Prompt users for their name and responses
    name = input("\nEnter your name: ")
    response = input("\nIf you could visit one place in this world, where would it be? ")

    #Store the response in a dictionary
    user_responses[name] = response

    # Find out if anyone else would take the poll
    repeat_poll = input("Would you like to let another person respond? (yes/no) ")
    if repeat_poll == 'no':
        poll_active = False

# Polling is complet.Show the results.
print("\n---------POLL RESULT---------")
for name, response in user_responses.items():
    print(f"{name.title()} would like to visit {response.title()} someday")


