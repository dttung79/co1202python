# Write a program to manage products with following features:
# 1. Add a new product (ask for name and price, check name is not in the dictionary)
# 2. Delete a product (ask for name, check name is in the dictionary)
# 3. Edit a product (ask for name, check name is in the dictionary, ask for new price)
# 4. Search a product (ask for name, check name is in the dictionary, print price)
# 5. Sell a product (ask for name, number of product, print receipt, add revenue to total, show current total)
# 6. Print all products

def product_management():
    running = True
    products = {'computer': 1000, 'ram': 200, 'keyboard': 100, 'mouse': 50}
    total_revenue = 0

    while running:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_product(products)
        elif choice == 2:
            delete_product(products)
        elif choice == 3:
            edit_product(products)
        elif choice == 4:
            search_product(products)
        elif choice == 5:
            total_revenue = sell_product(products, total_revenue)
        elif choice == 6:
            print_all(products)
        elif choice == 0:
            running = False
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    print("1. Add a product")
    print("2. Delete a product")
    print("3. Edit a product")
    print("4. Search for a product")
    print("5. Sell a product")
    print("6. Print all products")
    print("0. Quit")

def add_product(products):
    product_name = input("Enter the product's name: ")
    
    if check_exist(product_name, products):
        return

    product_price = float(input("Enter the product's price: "))
    products[product_name] = product_price
    print(f'Product {product_name} added successfully.')

def delete_product(products):
    product_name = input('Enter product name to delete: ')
    if check_not_exist(product_name, products):
        return
    
    products.pop(product_name)
    print(f'Product {product_name} deleted successfully.')

def edit_product(products):
    product_name = input('Enter product name to edit: ')
    if check_not_exist(product_name, products):
        return

    new_price = float(input('Enter new price: '))
    products[product_name] = new_price
    print(f'Product {product_name} edited successfully.')

def search_product(products):
    product_name = input('Enter product name to search: ')
    if check_not_exist(product_name, products):
        return

    print(f'Product {product_name}, price ${products[product_name]}.')

def sell_product(products, total_revenue):
    product_name = input('Enter product name to sell: ')
    if check_not_exist(product_name, products):
        return total_revenue
    
    n_products = int(input('Enter number of products to sell: '))
    revenue = products[product_name] * n_products
    print('Receipt:')
    print(f'Product name: {product_name}')
    print(f'Number of products: {n_products}')
    print(f'Payment: ${revenue}')

    total_revenue += revenue
    print(f'Total revenue: ${total_revenue}')
    return total_revenue

def print_all(products):
    for p in products:
        print(f'{p}: ${products[p]}')

def check_not_exist(name, products):
    if name not in products:
        print(f'Product {name} does not exist.')
        return True
    return False

def check_exist(name, products):
    if name in products:
        print(f'Product {name} already exists.')
        return True
    return False
### MAIN ####
product_management()