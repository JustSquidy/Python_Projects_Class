libraries = ['pandas', 'numpy', 'flask', 'matplotlib']
print(libraries)

for l in libraries:
    print(l)

first = libraries[0]
last = libraries[-1]

quantity_list = len(libraries)
print(f"There are {quantity_list} things in the list")

print(f"The first item is {first} and the last item is {last}")