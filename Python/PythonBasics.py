"""
    Docstring
"""
import sys
print(sys.version_info)
print("Hello, World!")

# Comment

'''
    Since Python will ignore string literals that are not assigned to a variable,
    you can add a multiline string (triple quotes) in your code, 
    and place your comment inside it

'''


# %% ##########################################################
#
#               Dynamically typed language
#
###############################################################

# Integer

my_int = 42 

# int - unlimited precision integer value
# Examples: 10, 0b10, 0o10, 0x10
# Constructor: int(3.5) - rounding towards 0
# Convert from string int("3")
# Convert from string specifing base int("3", 3)


# Float

my_float = 3.125

# float - double precision with 53-bit of binary precision
# Examples: 3.125, 3e8
# Constructor: float(7), float("1.618"),
# Special values: float("nan"), float("inf"), float("-inf")

# Bool

my_bool = True

# True, False

# Null Value

null_value = None

print(my_int)
print(my_float)
print(my_bool)
print(null_value)


# %% ########################################################
#
#                    Bytes
#
#############################################################


my_bytes = b'bytes'
print(my_bytes)

s = my_bytes.decode()
print(s)

b = s.encode()
print(b)


# %% ########################################################
#
#                    Dates
#
#############################################################


from datetime import date
from datetime import datetime

print(f'The current time is {datetime.now().isoformat()}')

today = date.today()
now = datetime.now()

dd = date(2020, 2, 14)


print(f'Today: {today}')
print(f'Now: {now}')
print(dd)

# %% ########################################################
#
#                    Operators
#
#############################################################

# == value equality operator
# === identity equality operator - same object

# is - or - and - in


# %% ########################################################
#
#                    Control Flow
#
#############################################################


if True:
    print("It's true")
elif "something else":
    print("It's elif")
else:
    print("It's false")

if False:
    print("It's true")
elif "something else":
    print("It's elif")
else:
    print("It's false")

if "eggs":
    print("Yes, please!")



# Simple loop
c = 5
while c > 0:
    print(c)
    c -= 1


# Infinite loop
while True:
    response = input()
    response = 'break'
    print("Infinite loop - " + response)
    if response == 'break':
        break

# for loop
list = [1, 9, 8]
for item in list:
    print(item)

for item in range(5):
    print(item)

# Range
#
# range(stop)
# range(start, stop)
# range(start, stop, step)


# enumerate() returns tuple ???

my_items = [5, 7, 9, 15]
for p in enumerate(my_items):
    print(p)



# %% ########################################################
#
#                         Lists
#
#############################################################


# Lists - mutable, heterogeneous sequences of objects

my_list = ["One", "Two", "Three"]
my_list.append("Four")
print(my_list)

#indexing from the end
print(my_list[-1])

# slicing
l2 = my_list[1:3]
print(l2)

# copy list with slicing
l3 = l2[:]
print(l3)
print(l3 is l2)
print (l3 == l2)


# %% ########################################################
#
#                         Dictionary
#
#############################################################

my_dictionary = {
    1 : "One",
    2 : "Two"
}
print(my_dictionary)

# Iterating with .items()
for key, value in my_dictionary.items():
   print(f'{key}: {value}') 



# %% ########################################################
#
#                         Tuple
#
#############################################################

# Immutable sequence of arbitrary objects

# Tuple (1, 2, 3)

# Nested tuple
nested_tuple = ((1, 2, 3), (2, 3, 4), (5, 6, 7))

# Single element tuple
t1 = (5,)

# Empty tuple
t0 = ()

# Tuple unpacking
def minmax(items): 
    return min(items), max(items)

lower, upper = minmax(81, 82, 83, 84, 85)

# Swap elements
a = 5
b = 10
a, b = b, a

# %% ########################################################
#
#                         Set
#
#############################################################

# Set {1, 2, 3}
# mutable collection of unique immutable objects

my_set = {55, 43, 14, 68}

print(my_set)
print(type(my_set))


# %% ########################################################
#
#                         Enumerate
#
#############################################################

# enumerate(collection) return tuple index, value

enum_list = [55, 43, 14, 68]
for i, v in enumerate(enum_list):
    print(f'{i} - {v}')



# %% ########################################################
#
#             Objects / Scopes
#
#############################################################

# Everything is an object, variables are references to the object

a = 5
b = 5

print(a == b)
print(a is b) # references same object 5

# Scopes:
# - Local - inside current function
# - Enclosing - inside enclosing functions
# - Global - top level of the module
# - Built-in

# global my_variable - references global 

# Source code blocks do not introduce new scope

# %% ########################################################
#
#             Exceptions
#
#############################################################

try:
    a = 2
    a /= 0

except TypeError:
    print(TypeError)
    raise ValueError()

except (KeyError, ZeroDivisionError) as e:
    print(e)
    print(type(e))
    pass

finally:
    print(a)



# %% ########################################################
#
#             Comprehensions
#
#############################################################

# List and Set:
# [expr(item) for item in iterable if condition]

words = "This is comprehension".split()
print(words)
c = [len(word) for word in words]
print(c)
print(type(c))

# Dictionary comprehension - using {}




# %% ########################################################
#
#             Iterators
#
#############################################################

my_items = [5, 7, 9, 15]

my_iterator = iter(my_items)

print(next(my_iterator))





# %% ########################################################
#
#             Generators and Generator Expressions
#
#############################################################

# generators use yield to return result
# lazy iteration calculation

# (x for x in range(1001) if is_prime(x))











# %% ########################################################
#
#             Classes
#
#############################################################

class MyEmptyClass:
    pass

class MyClass:
    """Class docstring"""

    my_class_attribute = 0

    def __init__(self, number, **kwargs):   # initializer, not a constructor - object already created
        self._number = number               # attribute declaration is not required, everything is public and dynamicly typed

    # **kwargs is useful for adding named arguments destined for child classes

    def my_class_function(self):
        return self._number

    @staticmethod
    def my_static_function():
        MyClass.my_class_attribute += 1
        return MyClass.my_class_attribute

    @classmethod
    def my_class_method(cls):
        cls.my_class_attribute += 1
        return cls.my_class_attribute

    # class methods can be used to create object factory / named constructors

    @classmethod
    def my_object_factory(cls, number):
        return cls(number)


f = MyClass(5)
n = MyClass.my_object_factory(10)
print(type(f))
print(f.my_class_function())
print(n.my_class_function())
print(MyClass.my_static_function())
print(MyClass.my_class_method())


# Inheristance is only useful to share functionality
# Late binding can make child elements accessible in parent class

class MyEmptyChildClass(MyClass):
    pass

class MyChildClass(MyClass):

    def __init__(self, number, *, child_number, **kwargs):
        self._number = number
        self.child_number = child_number

c = MyChildClass(7, child_number = 8)
print(c.child_number)
    



# %% ########################################################
#
#             Class Properties
#
#############################################################

class MyClassWithProperties:

    def __init__(self, my_property_value):
        self._my_property = my_property_value

    @property
    def my_property(self):
        return self._my_property

    @my_property.setter
    def my_property(self, value):
        self._my_property = value
    
p = MyClassWithProperties(12)
print(p.my_property)
p.my_property = 14
print(p.my_property)


# %% ########################################################
#
#             File I/O
#
#############################################################

f = open ('path')

# Mode rwa and tb

