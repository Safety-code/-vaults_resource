
hours = input('Enter hours per day:\n')
rate = input('Enter the daily hourly rate:\n')

try:
    Pay = (int(hours) * float(rate))

    if Pay > 40:
        new_hourly_rate = (1.5 * float(rate))
        print('Your Pay for work above 40 hours:', int(hours) * new_hourly_rate)
    else:
        print('Your daily Pay is: ', Pay)
except:
    print("Error, Please enter numeric input")
