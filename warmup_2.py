classes = []

class_name = input('Enter Class name ')

while class_name:
    classes.append(class_name)
    class_name = input('Enter a class name? Press enter to quit: ')

print(classes)

for index, c in  enumerate(classes):
    print(f'{index + 1}: {c}')
