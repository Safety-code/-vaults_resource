import pprint

# alien_0 = {'color':'green', 'points':5}
# alien_0['x-position'] = 0
# alien_0['y-position'] = 25
# print(alien_0)
# new_point = alien_0['points']
# print(f"You just earned {new_point} point!")

# #create a dictionary
# my_dict = {'name': 'Max', 'age':28, 'city':'New York'}
# print(my_dict)
# print(my_dict['name'])
# print(my_dict['age'])
# print(my_dict['city'])

myCat = {'sizes':'fat', 'color':'gray', 'dispositions':'loud'}
print(myCat)
print("My cat has", myCat['color'], "fur")

spam = ['cats', 'dog', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon

birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}
while True:
    print("Enter a name (blank to quit...)")
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("I do not have information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database is updated")

#keys(), values(), items()
spam = {'color':'red', 'age':42}
print(spam.keys())
dict_keys = (['color', 'age'])
print(list(spam.keys()))

#multiple assignment trick in for loop
for k, v in spam.items():
    print(' Key: ' + k + ' Value: ' + str(v))

for v in spam.values():
    print(v)


for k in spam.keys():
    print(k)

for m in spam.items():
    print(m)

spam = {'name':'Zophie', 'age':7}
'name' in spam.keys()

print('name in spam: ',  spam.keys())

#the get() method
picnicitems = {'apples':5, 'cups':2}
print('I am bringing ' + str(picnicitems.get('cups', 0)) + ' cups')

print('I am bringing ' + str(picnicitems.get('eggs', 0)) + ' eggs')

#setdefault() method 
spam = {'name':'Pooker', 'age':5}
if 'color' not in spam:
    spam['color'] = 'black'
    print(spam)

spam = {'name':'Pooker', 'age':5}
spam.setdefault('color', 'black')
print(spam)

message = "It was a bright cold day in April, and the clocks was striking thirteen"
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)


message = "It was a bright cold day in April, and the clocks was striking thirteen"
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

#TIC-TAC TOE BAORD
# theBoard = {'top-L' :'0 ', 'top-M':'0 ', 'top-R' :'0 ',
#             'mid-L' :'X ', 'mid-M' :'X ', 'mid-R':' ',
#             'low-L' :' ', 'low-M' :' ', 'low-R' :'X ',}

# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-++-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-++-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
#     print('-++-')

# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + ' Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = '0'
#     else:
#         turn = 'X'
# printBoard(theBoard)


#nested dictionaries
allGuests = {'Alice': {'apples':5, 'pretzels':12},
             'Bob': {'ham sandwiches': 3, 'apples':2},
             'Carol': {'cups':3, 'apple pies': 1}}
def totalBrought(guest, item):
    numBrought = 0
    for k, v in guest.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples      '+str(totalBrought(allGuests, 'apples')))
print(' - Cups       '+str(totalBrought(allGuests, 'cups')))
print(' - Cakes         '+str(totalBrought(allGuests, 'cakes')))
print(' - Ham sandwiches    '+str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple pies         '+str(totalBrought(allGuests, 'apple pies')))


my_dcit1 = {'name': 'Max', 'age':28}
my_dict2 = {'name': 'Alex', 'age':25}
nested_dict = {'dictA': my_dict2, 'dictB': my_dict2}
print(nested_dict)

#using update() to merge two dictionaries
my_dict = {'name': 'Max', 'age':28, 'email': 'max@example'}
my_dict_2  = dict(name='Lisa', age=27, city='Boston') #keys overwritten
my_dict.update(my_dict_2)
print(my_dict)

#deleting item in a dictionary
#delete a key-value pair
#my_dict = {'name': 'Max', 'age':28, 'email': 'max@example'}
del my_dict['email']
print(my_dict)
print("popped item:", my_dict["age"])
my_dict.clear()
print(my_dict)

#copy a dictionary
