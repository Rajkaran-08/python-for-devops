name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
city = input("Please enter the city where you live: ")

print("Hello my name is {0}. I'm {1} years old and I live in {2}." .format(name.title(), age, city.upper()))
print("Length of your name is: ", len(name))
if name.lower() == "raj":
    print("The name is {}" .format(name.title()))
else:
    print("The name is not Raj")