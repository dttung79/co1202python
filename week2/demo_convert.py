n = input('Enter number: ')
print(n, type(n))
n = int(n) # convert a string to an integer, not always possible
print(n, type(n))
m = n + 10
print(m)

# convert a number to a string => always possible
n = 10
s = str(n)
print(n, s)
print(type(n), type(s))

# convert integer to float
n = 10
f = float(n)
print(f)

# convert float to integer
f = 10.9999
n = int(f)
print(n)