# name = input("Please enter your name: ")
# print(f"\nHello, {name}")

# height = input("How tall are you, in inches?: ")
# height = int(height)

# if height >=48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're little older.")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd")

#outer for loop
for i in range(1, 11):
    #nested loop
    #to iterate from 1 to 10
    for j in range(1, 11):
        print(i * j, end=' ')
    print("")


rows = 5
for i in range(5):
    for j in range(3):
        print("*", end=" ")
    print('')

