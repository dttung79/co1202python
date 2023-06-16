number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

operation = input('Choose math operation (+, -, *, /): ')

if operation not in ('+', '-', '*', '/'):
    print('Invalid operation')
else:
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = number1 / number2
    print('Result: ', result)