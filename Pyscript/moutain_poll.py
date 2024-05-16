responses = {}

#Set a flag to indicate the polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # Store the response in a dictionary
    responses[name]= response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (Yes/No) ")

    if repeat == 'no':
        polling_active = False
    
# Polling is complete.Show the results
print("\n----Poll Results-----")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()} someday")
