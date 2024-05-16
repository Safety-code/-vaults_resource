#PIZZA TOPPINGS

toppings = "\nEnter the pizza toppings of your preference: "
toppings += "\nEnter 'quit' to end the program "

while True:
    pizza_toppings = input(toppings)

    if pizza_toppings == 'quit':
        break
    else:
        print(f"Will add {pizza_toppings.title()} to your pizza")