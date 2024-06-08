magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"Hello {magician.title()},  that was a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}\n")

print("\n Thank you everyone, that was a great show")

#PIZZAS
pizzas = ["peppreoni", "chicken", "cheese"]
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")

print("\n I really like cheese pizza so much")
print("I really love pizza\n")


#ANIMALS
animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(f"A {animal.title()} will make a great pet")

print("\n Any of these animals would make a great pet")


#NUMERIACL LIST
for value in range(5):
    print(value)


numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []

for value in range(1,11):
    #square = value **2
    squares.append(value **2)
print(squares)

digit = [1,2,3,4,5,6,7,8,9,0]
print(digit)
print("minimum:",min(digit))
print("maximum:",max(digit))
print("sum:",sum(digit))


#LIST COMPREHENSION
squares = [value ** 2 for value in range(1,11)]
print(squares)

#TIY
for value in range(1,21,3):
    print(value)

# million = list(range(1,1000001))
# print(million)
# print("minimum:",min(million))
# print("minimum:",max(million))
# print("minimum:",sum(million))


# millionth = []
# for number in range(1,1000001):
#     millionth.append(number)
# print(millionth)

#list comprehension
# millionth = [number for number in range(1,1000001)]
# print(millionth)
#odd numbers
odd_number = []
for value in range(1,21,2):
    odd_number.append(value)

print("List of odd numbers:",odd_number)

#MULTIPLES OF THREE
multiple_of_three = []
for value in range(3,31, 1*3):
    multiple_of_three.append(value)
print(multiple_of_three)

multiple_of_three = [value for value in range(3,31, 1*3)]
print("Multiples of 3:",multiple_of_three)


list_of_cubes = [value ** 3 for value in range(1,11)]
print("List of first 10 cubes:",list_of_cubes)


#SLICING A LIST
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team\n")
for player in players[0:3]:
    print(player.title())

#COPYING LIST
my_foods = ["piza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("carroli")
friend_foods.append("ice cream")

print("My favorite foods are: ")
print(my_foods)

print("\nMy friends favorite foods are: ")
print(friend_foods)

#list repeated element
list_with_zeros = [0] * 5
print(list_with_zeros)

#concatenation
list_concat = my_foods + friend_foods
print(list_concat)

#string to list
string_to_list = list("hello")
print(string_to_list)


#checking if an item exist
if "carroli" in friend_foods:
    print("yes")
else:
    print("no")


a = [1,2,3,4,5,6,7]
b = a[::3]  #3 is a stepsize
b = a[::-2]
print(b)    

#nested list
a = [[1,2], [3,4]]
print(a)
print(a[0][1])


#TIY
print(friend_foods) 
print("The first three items in the list are: ")
print(friend_foods[:3]) 
print("Three items from the middle of the list are: ")
print(friend_foods[1:-1])
print("The last three items are: ")
print(friend_foods[1:])


pizzas = ["peppreoni", "chicken", "cheese"]
friends_pizza = pizzas[:]
friends_pizza.append("turkey")
pizzas.append("mushrooms")

print("My friend's pizza:",friends_pizza)
print("Original pizza list:",pizzas)

for pizza in pizzas:
    print(f"My favorite pizzas are:{pizza.title()}")

for friend in friends_pizza:
    print(f"My friend's favorite pizzas are:{friend.title()}")