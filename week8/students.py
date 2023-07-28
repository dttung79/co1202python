def student_management(names, gpas):
    running = True
    while running:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student(names, gpas)
        elif choice == 2:
            edit_gpa(names, gpas)
        elif choice == 3:
            delete_student(names, gpas)
        elif choice == 4:
            seach_name(names, gpas)
        elif choice == 5:
            search_gpa(names, gpas)
        elif choice == 6:
            print_all(names, gpas)
        elif choice == 7:
            running = False
        else:
            print("Invalid choice. Please try again.")

def print_menu():
    print("1. Add a student")
    print("2. Edit a student's GPA")
    print("3. Delete a student")
    print("4. Search for a student by name")
    print("5. Search for a student by GPA")
    print("6. Print all students")
    print("7. Quit")

def add_student(names, gpas):
    name = input("Enter the student's name: ")
    gpa = float(input("Enter the student's GPA: "))
    names.append(name)
    gpas.append(gpa)
    print(f'Student {name} added successfully.')

def edit_gpa(names, gpas):
    name = input('Enter student name to edit: ')
    
    found_index = find_student(names, name) # find index of student with name
    if found_index != -1:
        new_gpa = float(input('Enter new GPA: '))
        gpas[found_index] = new_gpa     # update new gpa at found_index

def delete_student(names, gpas):
    name = input('Enter student name to delete: ')
    
    found_index = find_student(names, name) # find index of student with name
    if found_index != -1: 
        names.pop(found_index)      # remove name at found_index
        gpas.pop(found_index)       # remove gpa at found_index
    
    print(f'Student {name} deleted successfully.')

def seach_name(names, gpas):
    name = input('Enter student name to search: ')
    found_index = find_student(names, name) # find index of student with name
    
    if found_index != -1:
        print('Student found:')
        print(f'Name: {names[found_index]}')
        print(f'GPA: {gpas[found_index]}')

def find_student(names, name):
    for i in range(len(names)):
        if names[i] == name:
            return i
    
    print(f'Student {name} not found.')
    return -1

def search_gpa(names, gpas):
    gpa = float(input('Enter student GPA to search for: '))
    
    for i in range(len(gpas)):
        if gpas[i] >= gpa:
            print(f'Name: {names[i]}, GPA: {gpas[i]}')

def print_all(names, gpas):
    for i in range(len(names)):
        print(f'Name: {names[i]}, GPA: {gpas[i]}')


### MAIN PROGRAM ###
names = ['John', 'Jane', 'Jack', 'Jill']
gpas = [3.5, 3.9, 3.2, 3.8]
student_management(names, gpas)