import os

def scan_folder(path, level):
    # check if path exists
    if not os.path.exists(path):
        print(f"Path {path} does not exist")
        return
    # check if path is a directory
    if os.path.isdir(path):
        print('  ' * level + "+ " + path.split('/')[-1])
        files = os.listdir(path)
        level += 1
        for f in files:
            scan_folder(path + '/' + f, level)
    else: # path is a file
        print('  ' * level + "- " + path.split('/')[-1])


path = input('Enter a path: ')
scan_folder(path, 0)