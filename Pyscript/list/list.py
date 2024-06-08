# LIST
list1 = ["banana", "Apple", "cherry", "pear"]
print(list1)
print("Lenght: ", len(list1))

list1[0] = "lemon"
print(list1)


item = list1[0]
item = list1[-1]
print(item)

list2 = list() 
print(list2)
list2.append("orange")
print(list2)


#iist allowd different datatypes
list4 = [5, True, "apple"]
print(list4)

list4[-1] = 4
print(list4)

#allow duplicate
list3 = [0, 1, 2 , 1, 0]
print(list3)



bicycles = ['trek', 'cannondales','redline', 'specialized']
print("lenght:", len(bicycles))
bicycles.append("mountain")
print(bicycles)
bicycles.pop()
print(bicycles)
print(bicycles[1])
print(bicycles[-1])
bicycles.append("mountain")

print(f'My first bicycle was a {bicycles[0].title()}.')
print(f"I really admire {bicycles[-1].title()} bikes!")

names = ["fred", "franca", "daisy", "sarah", "sarkodie", "gyasi"]
print(names[-1].title())
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())

message = f"Hello my good friend: {names[0:-1]}"
print(message)

motocycles = ["honda", "yamaha", "suzuki"]
print(motocycles)

motocycles[0] = "ducati"
print(motocycles)
motocycles.append("honda")
print(motocycles)

motors = []

motors.append("honda")
motors.append("yamaha")
motors.append("ducati")
motors.append("bugatti")
print(motors)

#insert
motors.insert(1, "toyota")
print(motors)

#del
del motors[0]
print(motors)

popped_motor = motors.pop()
print(motors)
print(motocycles)

last_owned = motocycles.pop()
print(f"The last motocycle i owned was {last_owned}")

first_owned = motocycles.pop(0)
print(f"The first motocycle i owned was {first_owned}")

#remove
motocycles = ["honda", "yamaha", "suzuki"]
print(motocycles)
motocycles.remove("yamaha")
print(motocycles)

too_expensive = "suzuki"
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

guests = ["fred", "paul", "amos", "nsia"]
invite = f"I specially invite {guests[1].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[0].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[-1].title()}, to this event"
print(invite)

not_coming = guests.pop(0)
print(not_coming)
print(f"{not_coming.title()} can't make it")
print(guests)

guests.append("sarah")
print(guests)
invite = f"I specially invite {guests[1].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[0].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[-1].title()}, to this event"
print(invite)

print(guests)
guests.append("polley")
guests.append("emma")
print(guests)

guests.insert(0, "safety")
guests.insert(4, "batholomuew")
guests.append("jay")
print(guests)
invite = f"I specially invite {guests[-1].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[0].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[2].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[3].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[4].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[5].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[6].title()}, to this event"
print(invite)
invite = f"I specially invite {guests[1].title()}, to this event"
print(invite)


invite = f"Unfortunately, {guests[-1].title()}, I can only invite two guests"
print(invite)
invite = f"Unfortunately, {guests[1].title()}, I can only invite two guests"
print(invite)
invite = f"Unfortunately, {guests[2].title()}, I can only invite two guests"
print(invite)
invite = f"Unfortunately, {guests[3].title()}, I can only invite two guests"
print(invite)
invite = f"Unfortunately, {guests[0].title()}, I can only invite two guests"
print(invite)
invite = f"Unfortunately, {guests[-1].title()}, I can only invite two guests"
print(invite)
invite = f"Unfortunately, {guests[4].title()}, I can only invite two guests"
print(invite)
invite = f"Unfortunately, {guests[5].title()}, I can only invite two guests"
print(invite)

#UNINVITED GUESTS
uninvited_guest = guests.pop(-2)
print("Uninvited guets: ", uninvited_guest)
print(f"I'm sorry, {uninvited_guest.title()} i can't invite you for the dinner")
uninvited_guest = guests.pop(-3)
print("Uninvited guets: ", uninvited_guest)
print(f"I'm sorry, {uninvited_guest.title()} i can't invite you for the dinner")
uninvited_guest = guests.pop(-4)
print("Uninvited guets: ", uninvited_guest)
print(f"I'm sorry, {uninvited_guest.title()} i can't invite you for the dinner")
uninvited_guest = guests.pop()
print("Uninvited guets: ", uninvited_guest)
print(f"I'm sorry, {uninvited_guest.title()} i can't invite you for the dinner")
uninvited_guest = guests.pop()
print("Uninvited guets: ", uninvited_guest)
print(f"I'm sorry, {uninvited_guest.title()} i can't invite you for the dinner")
uninvited_guest = guests.pop()
print("Uninvited guets: ", uninvited_guest)
print(f"I'm sorry, {uninvited_guest.title()} i can't invite you for the dinner")
uninvited_guest = guests.pop()
print("Uninvited guets: ", uninvited_guest)
print(f"I'm sorry, {uninvited_guest.title()} i can't invite you for the dinner")
print(guests)

#still invited
invited_guests = f"{guests[0].title()}, you're are still invited for the dinner :)"
print(invited_guests)

del guests[0:]
print(guests)



#SORTING LIST
cars = ["bmw", "benz", "audi", "toyota", "subaru"]
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)
print("Here is the original list of cars")
print(cars)

print("\n Her   e is the sorted version of the list of cars")
print(sorted(cars))

print("\n Here is the original list of cars again")
print(cars)

print("\n Reverese chronological order of the list of cars")
cars.reverse()
print(cars)


#SEEING THE WORLD
places = ["spain", "france", "algeria", "tanzania", "nigeria"]
print("Here is the original list")
print(places)

print("\n Here is the sorted version")
print(sorted(places))

print("\n Here is the original list again")
print(places)

print("\n Here is the reverse-sorted version ")
print(sorted((places), reverse=True))

print("\n Here is the original list again")
print(places)

print("\n Here is the reverse version ")
places.reverse()
print(places)

places.reverse()
print(places)

print("\n Here is the sort version in alphabetical order")
places.sort()
print(places)

print("\n Here is the reverse-sort version in alphabetical order")
places.sort(reverse=True)
print(places)

print(guests)
print(len(guests))
























