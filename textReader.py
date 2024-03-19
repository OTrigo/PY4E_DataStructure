file_name = input("Enter file name: ")
file_handler = open(file_name)

for row in file_handler:
    print(row.rstrip().upper())