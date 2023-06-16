# Enter 3 grades: math, english, physics
# Check if 3 grades are valid (0 <= grade <= 10)
# If not, print 'Invalid grade'
# If all 3 grades are valid, print average grade
math = int(input('Enter math grade: '))
english = int(input('Enter english grade: '))
physics = int(input('Enter physics grade: '))

if math < 0 or math > 10:
    print('Invalid math grade')
elif english < 0 or english > 10:
    print('Invalid english grade')
elif physics < 0 or physics > 10:
    print('Invalid physics grade')
else:
    avg = (math + english + physics) / 3
    print('Average grade: ', avg)