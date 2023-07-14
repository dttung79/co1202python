items = []
n_items = 0
buying = True

print('Welcome to the Grocery Store!')

while buying:
    item = input(f'Item {n_items + 1}: ')
    if item == '':
        buying = False
    else:
        items.append(item)
        n_items += 1

choice = input('Which item (all/index): ')

if choice == 'all':
    print('Your shopping list:', items)
else:
    i = int(choice)
    if i < 1 or i > n_items:
        print('Invalid index')
    else:
        print(f'Your item: {items[i - 1]}')