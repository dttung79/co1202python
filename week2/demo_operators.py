# Number (integer, float) operators: +, -, *, /, //, %, **
a = int(input('Enter a: '))
b = int(input('Enter b: '))

print('a + b =', a + b)    # addition
print('a - b =', a - b)    # subtraction
print('a * b =', a * b)    # multiplication
print('a / b =', a / b)    # division
print('a // b =', a // b)  # integer division (floor division)
print('a % b =', a % b)    # remainder (modulo)
print('a ** b =', a ** b)  # exponentiation (power)

# Think of a scenario where you need to use one of these operators
# and write a small program to demonstrate it.

initial_balance = float(input('Enter initial balance: '))
interest_rate = int(input('Enter interest rate: '))
years = int(input('Enter number of years: '))

# A = P(1 + r/100)^n
final_balance = initial_balance * (1 + interest_rate / 100) ** years
print('Final balance:', final_balance)