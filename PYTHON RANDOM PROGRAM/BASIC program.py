'''try:
    numerator=int(input("enter numerator"))
    denominator=int(input("enter denominator"))
    result=numerator/denominator
except ZeroDivisionError:
    printf("error: cannot divide by zero")
except ValueError:
    print("error: please enter valid integer")
else:
    print("result",result)
finally:
    print("execution completed")'''

#program 2

'''a=13
print(a)
ab=67
print(ab)
_a=87
print(_a)
a9=65
print(a9)
abc=18
print(abc)
a=12
print(a)'''

#program 3
'''lst=["23",23,1+3j,"abhishek"]

print(lst)

lst.append("ram")
print(lst)

lst.extend("98")
print(lst)

lst.pop(1)
print(lst)

a=len(lst)
print(a)

a=lst.count("abhishek")
print (a)

lst.insert(1,"ark")
print(lst)

lst.clear()
print(lst)

a=lst.index("23")
print(a)

lst.remove("abhishek")
print(lst)

lst_unsorted=[10,100.23,45,35,67,89]
lst_unsorted.sort()
print(lst_unsorted)'''

#negative indexing of list
'''lst=[1,234,'cse101','pyhton',347,'ABHI']
print(lst[-1:-5])'''



#program 4 STRING OPERATION

#str="breakfast is ready"
#print(str[-6:])
#print(str[1:8:1])

'''data="Python rocks!"
word_list=data.split()
print(word_list)

uppercase=data.upper()
print(uppercase)

pos=data.find("rocks")
print(pos)

update=data.replace("!","?")
print(update)

# Convert string to number
str_value = "234.23"
number = float(str_value)
print(type(number))
print("Converted number:", number)

# Convert number to string
number_value = 234.23
str_value = str(number_value)
print(type(str_value))
print("New converted string:", str_value)


fname = "Sanjay"
lname = "Kapoor"
fname += lname
print(fname)'''

#program 5 DICTIONARY OPERATION

# Dictionary literals
'''my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print("Occupation:", my_dict['occupation'])

# Updating a value
my_dict['age'] = 26
print("Updated Age:", my_dict['age'])

# Removing a key-value pair
removed_value = my_dict.pop('city')
print("Removed City:", removed_value)

# Traversing the dictionary
print("\nTraversing the Dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Check if a key exists
if 'age' in my_dict:
    print("\nThe 'age' key exists in the dictionary.")

# Check if a key doesn't exist
if 'country' not in my_dict:
    print("The 'country' key does not exist in the dictionary.")'''


#PROGRAM 6 FIBANOIC SERIES
'''def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
fib(10)'''

#PROGRAM 7 PRIME NUMBER
'''n=int(input("enter any number"))
for i in range(2,n):
      if(n%2==0):
         print(f'{n} is not prime')
         break
else:
    print(f'{n} is prime')'''


#program using polymorphism


import math 

class shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
       return 2*math.pi*self.radius

class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

class square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*self.side

#example usage
Circle=circle(2)
Rectangle=rectangle(4,6)
Square=square(4)

shapes=[Circle,Rectangle,Square]

'''for shape in shapes:
   print(f"Shape:{type(shape)...name...}")
   print(f"Area: {shape.area()}")
   print(f"Perimeter: {shape.perimeter()}")
   print("--------------------------")'''

for shape in shapes:
    print(f"Shape: {type(shape).__name__}")
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    print("---------------")






      
    






