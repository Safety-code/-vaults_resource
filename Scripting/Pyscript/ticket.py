# MOVIE TICKET 

# age = input("Enter your age: ")
age = int(age)

# age_limit = 0

# while age_limit <= 12:
#     age_limit += 1

#     if age_limit <= 3:
#         continue
#         print("Your ticket is free")
#     elif age_limit > 3 and age_limit <= 12:
#         print("Your ticket cost $10")
#     elif age_limit > 12:
#         print("Your ticket is $15")
#     else:
#         print("Enter right age")
#         continue
#     print(age_limit)
    


# age = "Enter your age: "
# age_active = True

# message = ""
# while age_active:
#     message = input(age)
#     if message == 'quit':
#         age_active = False
    
#     elif message <= '3':
#         print("Your ticket is free")
#     elif message > '3':
#         print("Your ticket cost $10")
#     elif message > '12':
#         print("Your ticket is $15")
#     else:
#         print("Try again")
    
    
    

age_active = True

while age_active:
    age = ("\nEnter your age: ")
    age = int(age)

    if age == 0:
        age_active = False

    elif age <= 3:
        print("Your ticket is free")
    elif age > 3:
        print("Your ticket cost $10")
    elif age > 12:
        print("Your ticket is $15")
    else:
        print("Try again")
    
