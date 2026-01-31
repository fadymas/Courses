#Example B01 
my_list = []
my_tuple = ()
my_set = set()
my_dict = {}

my_list.append(1)
my_list.append("ahmed")
my_list.append(3.2)

my_tuple = my_tuple + ("dog", "cat")

my_set.add(5)
my_set.add(10)

my_dict["color"] = "blue"
my_dict["size"] = 20

print("Final List:", my_list)
print("Final Tuple:", my_tuple)
print("Final Set:", my_set)
print("Final Dictionary:", my_dict)

#Example C01

fruits = ["apple", "banana", "cherry", "date", "orange"]

print("Fruits List:", fruits)
print("Head (first three):", fruits[:3])
print("Tail (last two):", fruits[-2:])
print("Second element:", fruits[1])

fruits[2] = "grape"

fruits[0], fruits[3] = fruits[3], fruits[0]

print("Updated Fruits List:", fruits)

#Example C02

list1 = [100, 200, 300, 400, 500]

list1.reverse()

print("Reversed List:", list1)

#Example D01
fruit_set = {'applg', 'banana', 'chgrry', 'datg'}
other_fruit_set = {'chgrry', 'datg', 'mango', 'grapg'}

intersection = fruit_set & other_fruit_set
union = fruit_set | other_fruit_set
difference = fruit_set - other_fruit_set

print("Intersection:", intersection)
print("Union:", union)
print("Difference (fruit_set - other_fruit_set):", difference)

#Example E01
fruits_tuple = ("apple", "banana", "cherry", "date", "orange")

print("Fruits Tuple:", fruits_tuple)
print("Head (first three):", fruits_tuple[:3])
print("Tail (last two):", fruits_tuple[-2:])

# Attempting to change an element
try:
    fruits_tuple[1] = "grape"
except TypeError as e:
    print("Error:", e)
    print("Explanation: Tuples are immutable, so their elements cannot be changed after creation.")

new_tuple = (fruits_tuple[0],)

print("New Tuple with only the first element:", new_tuple)

#Example E02
colors = ("red", "green", "blue")

numbers_list = [10, 25, 7, 40, 15, 5]
numbers_tuple = tuple(numbers_list)

print("Colors Tuple:", colors)
print("Numbers Tuple:", numbers_tuple)

print("Length of Numbers Tuple:", len(numbers_tuple))
print("Maximum Value:", max(numbers_tuple))
print("Minimum Value:", min(numbers_tuple))
print("Sum:", sum(numbers_tuple))
print("First Element:", numbers_tuple[0])

#Example F01

people = {
    "111-34-3434": "John",
    "343-45-5455": "Alice",
    "555-66-7777": "Bob"
}

people["234-56-9010"] = "Susan"

people["111-34-3434"] = "John Smith"

value = people.get("343-45-5455")

print("Value of key 343-45-5455:", value)
print("Final Dictionary:", people)

def upd_key(dict,o_key,n_key):
    if o_key in dict:
        dict[n_key]=dict.pop(o_key)
    return dict
upd_key(people,'555-66-7777','555-66-8888')
print(people)

#Example Pseudo Code 01
students = {
    "Ali": 85,
    "Sara": 92,
    "Omar": 70
}

name = "Sara"

if name in students:
    print(f"{name}'s score is {students[name]}")
else:
    print(f"{name} is not found in the dictionary")

#Example Pseudo Code 02

products = {
    "Laptop": 1500,
    "Phone": 800,
    "Tablet": 600
}

for item, price in products.items():
    print(f"{item} costs ${price}")


#Example Pseudo Code 03/ mini login system

users = {
    "ahmed": "1234",
    "sara": "abcd"
}

attempts = 0

while attempts < 3:  
    username = input("Enter username: ")

    if username in users:  
        password_attempts = 0
        while password_attempts < 3:  
            password = input("Enter password: ")
            if password == users[username]:
                print("Login successful!")
                break  
            else:
                print("Incorrect password, try again.")
                password_attempts += 1
        break  
    else:
        print("Username not found. Try again.")
        attempts += 1
