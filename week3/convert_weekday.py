# Enter week day in number (1-7)
# Print week day in text (Monday-Sunday)
# For example, user enters 1, print 'Sunday'

# Try different way to validate week day number
week_day = int(input('Enter week day in number: '))
# if week_day < 1 or week_day > 7:
#     print('Invalid week day number')

if week_day not in (1, 2, 3, 4, 5, 6, 7):
    print('Invalid week day number')
else:
    if week_day == 1:
        print('Sunday')
    elif week_day == 2:
        print('Monday')
    elif week_day == 3:
        print('Tuesday')
    elif week_day == 4:
        print('Wednesday')
    elif week_day == 5:
        print('Thursday')
    elif week_day == 6:
        print('Friday')
    else:
        print('Saturday')

# if week_day != 1 and week_day != 2 and week_day != 3 and week_day != 4 and week_day != 5 and week_day != 6 and week_day != 7:
#     print('Invalid week day number')