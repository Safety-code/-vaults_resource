current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1


# prompt = "\nTell me something and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)


#Using break in a while loop
#Break statement can also be used in a for loop
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)

#     if city =='quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

#Using continue is a while loop
current_number = 0
while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue
    print(current_number)   