# MOVIE TICKET 

age = "\nEnter your age to know your ticket price: "
age += "\nEnter 'quit' to exit the program: "

age_limit = 12
while age_limit:
    print(age_limit)
    
    if age_limit < 3:
        print("You have a free ticket")
    elif age_limit >= 3 and age_limit <= 12:
        print("Your ticket cost $10")
    elif age_limit > 12:
        print("Your ticket cost $15")
    else:
        break  



