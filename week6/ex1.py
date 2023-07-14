def print_line(n, symbol):
    for _ in range(n):
        print(symbol, end="")

def print_normal_triangle(n):
    for i in range(1, n + 1):
        print_line(i, '* ')
        print()

def print_reversed_triangle(n):
    for i in range(1, n + 1):
        print_line(n - i, '  ')
        print_line(i, '* ')
        print()

def print_bottom_up_triangle(n):
    for i in range(n):
        print_line(n - i, '* ')
        print()

def print_iso_triangle(n):
    for i in range(n):
        print_line(n - i - 1, '  ')
        print_line(2 * i + 1, '* ')
        print()

def print_triangle(n, mode):
    if mode not in ['normal', 'reversed', 'bottom-up', 'iso']:
        print('Invalid mode')
        return
    if mode == 'normal':
        print_normal_triangle(n)
    elif mode == 'reversed':
        print_reversed_triangle(n)
    elif mode == 'bottom-up':
        print_bottom_up_triangle(n)
    else:
        print_iso_triangle(n)

n = int(input('Enter n: '))
mode = input('Enter mode: ')
print_triangle(n, mode)