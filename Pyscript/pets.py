# pets = ['dog', 'cat', 'dog', 'mouse', 'cat', 'rat', 'bird', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
#     #pets.remove('dog')
#     print(pets)

#random
#import random

# for i in range(10):
#     x = random.random()
#     print(x)

#randint
# x = random.randint(5, 10)
# print(x)

#choice
# t = [1, 2, 3]
# x = random.choice(t)
# print(x)

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night and I work all day")

# x = print_lyrics()
# print(x)


# #repeat function in another function
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# y = repeat_lyrics()
# print(y)


def addtwo(a ,b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)