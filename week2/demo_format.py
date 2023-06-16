message = 'Hello Python'
print(message)
print('|' + message + '|')
print(f'|{message:20}|')   # by default, text is left-aligned
print(f'|{message:>20}|')
print(f'|{message:<20}|')
print(f'|{message:^20}|')

n = 100
print(f'|{n:20}|')         # by default, numbers are right-aligned
print(f'|{n:>20}|')
print(f'|{n:<20}|')
print(f'|{n:^20}|')

PI = 3.141592653589793
print(f'|{PI:20}|')
print(f'|{PI:20.5f}|')
print(f'|{PI:<20.5f}|')
print(f'|{PI:^20.5f}|')