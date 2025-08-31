print("Hello capstone")

#variables
school = 'MCTC'
gpa = 3.5
student_in_class = 22

#if statements
if gpa == 4:
    print('Wow!')
elif gpa > 3:
    print('Awesome')
else:
    print('cool!')

#lists

schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']

if 'MCTC' in schools:
    print('MCTC is in the list')

schools.sort()
print(schools)

schools.append('Century College')
print(schools)

schools.reverse() # returns none
print(schools)


#strings
class_name = 'Software Development Capstone'
print(class_name.upper())
print(len(class_name))
print(class_name.split())
print(class_name.split('o'))

if "Capstone" in class_name:
    print('This must be capstone')


#loops

for x in range(10):
    print (x)

for s in schools:
    print(s.upper())


for letter in school:
    print(letter * 10)

data = [0] * 10

print(data)

more_data = [None] * 10
print(more_data)


#while loops
name = input('enter your name: ')

while not name:
    print('Please enter as least one character ')
    print('Enter your name: ')

# true and false

start_of_semester = True
winter = False

if winter:
    print('BRR')
else:
    print('It is not winter')
    

#dictonaries

class_codes = {2905: 'Capstone', 2560: 'Web', 2545: "Java"}

print(class_codes[2560])

for code in class_codes:
    print(code)
    print(class_codes[code])

for code, name in class_codes.items():
    print('The class code is ' + str(code) + ' and the name is ' + name)
    
for code, name in class_codes.items():
    print(f'The class code is {code} and the name is {name}')

#slicing strings

schools = ['MCTC', 'DCTC', 'North Hennepin Technical College']

first_two = schools[0:2]
print(first_two)

last_school = schools[-1]
last_two_schools = schools[-2:]
print(last_two_schools)

school_name = 'Minneapolis community and technical colleege'
city = school_name[:11]
print(city)

#file io

with open('data.txt') as f:
    print(f.read())

with open('schools.txt', 'w') as f:
    f.writelines(schools)

#functions

def get_name():
    print("Hello, please enter your name")
    name = input("Your Name is: ")
    return name

name = get_name()