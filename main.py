def new_file(file_name, message):
    with open(file_name, 'a') as file: # w: write, r: read, a: append
        file.write(message)

def second_file():
    with open('toto.txt', 'r') as file_2:
        print(file_2.read())

def main():
    new_file('tata.txt', 'Kikou 2')

main()