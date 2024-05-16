# celsius = input('Enter temperature in Defrees Celcius:\n')
# Fahrenheit = (float(celsius) * 9/5 + 32)
# print('Temperature in Fahrenheit:',Fahrenheit)

# inp = input('Enter Fahrenheit Temperature: ')
# try:
#     fahr = float(inp)
#     cel = (fahr -32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Please enter a number')



#SCORE PROGRAMME
# Entered score should be between 0.0 and 1.0
# score = input('Enter your score: ')
# try:
#     score = float(score)

#     if score >=0.9 and score <= 1.0:
#         print(f"This score {score} is a Grade A")
#     elif score >=0.8 and score < 0.9:
#         print(f"This score {score} is a Grade B")
#     elif score >=0.7 and score < 0.8:
#         print(f"This score {score} is a Grade C")
#     elif score >=0.6 and score < 0.7:
#         print(f"This score {score} is a Grade D")
#     elif score <=0.6:
#         print(f"This score {score} is a Grade F")
#     else:
#         print('Bad score, out of range')
# except:
#     print("Error, enter decimal between 0.0-1.0")



# score = input('Enter your score: ')
# score = float(score)

def compute_grade(score):

    score = float(score)
    if score >=0.9 and score <= 1.0:
        print(f"This score {score} is a Grade A")
    elif score >=0.8 and score < 0.9:
        print(f"This score {score} is a Grade B")
    elif score >=0.7 and score < 0.8:
        print(f"This score {score} is a Grade C")
    elif score >=0.6 and score < 0.7:
        print(f"This score {score} is a Grade D")
    elif score <=0.6:
        print(f"This score {score} is a Grade F")
    else:
        print('Bad score, out of range')
    return score

final_score = compute_grade(0.5)
print(final_score)  


#STRINGS
greeting='hello world'
new_greeting = 'j' + greeting[1:]
print(new_greeting)

def count(letter, string):
    word = 'banana'
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

count_letter = count('a', 'banana')
print(count_letter)

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

spos = data.find(' ',atpos)
print(spos)

host = data[atpos+1:spos]
print(host)

camel = 42
print('%d' % camel)

while True:
    line = input('>')
    if line.startswith('#'):
        continue
    if line == 'done':
        break
    print(line)
print('Done!')



# READING FILES AND EXCEPTIONS
file_path = './files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())

# reading file contents line by line using for loop
file_path = './files/pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())


#Using the file contents outside the 'with' statement
file_path = './files/pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('\nEnter your birth date in the form yymmdd: ')
if birthday in pi_string:
    print('Your birthday appears in the first millionth digit of pi')
else:
    print("Your birthday does not appear in the first millionth digit of pi")
print(f"{pi_string[(1+1):52]}...")
print(len(pi_string))
