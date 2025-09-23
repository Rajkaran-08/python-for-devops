name = input("Please enter your name: ").strip()
age = int(input("Please enter your age: "))
city = input("Please enter the city where you live: ").strip()

#using str.format
print("Hello my name is {0}. I'm {1} years old and I live in {2}." .format(name.title(), age, city.upper()))
print("Length of your name is: ", len(name))
if name.lower() == "raj":
    print("The name is {}" .format(name.title()))
else:
    print("The name is not Raj")

#using f-string
print(f"Hellow my name is {name}. I'm {age} years old and I live in {city.upper()}")
print(f"Lengt of the name is {len(name)}")
if "raj" in name.lower():
    print("The name includes the word 'RAJ'")
else:
    print("The name does not include 'RAJ'")