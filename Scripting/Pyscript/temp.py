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
score = input('Enter your score: ')
try:
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
except:
    print("Error, enter decimal between 0.0-1.0")