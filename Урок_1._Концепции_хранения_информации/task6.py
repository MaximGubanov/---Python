with open("test_file.txt") as file:

    for line in file:
        print(line)


with open("test_file.txt", encoding="utf-8") as file:

    for line in file:
        print(line)