
# dataclass  - This module provides a decorators and function for automatically adding generated special methods such as __init__() and __repr__() to user-defined classes. or generate a common boilerplate methods. 

# EX- 
from dataclasses import dataclass 
@dataclass(init=True,repr=True,eq=False)
class Employee:
    eno:int
    ename:str
    esal:int
    eaddr:str 

e1=Employee(100,'Ganga',10000,'Chennai')
e2=Employee(101,'Gauri',50000,'Mumbai')
e3=Employee(101,'Gauri',50000,'Mumbai')
print(e1.eno,e1.ename,e1.esal,e1.eaddr,sep=" , ")      #   100 , Ganga , 10000 , Chennai
print(e1==e2)   # False
print(e2==e3)   # False


'''
Real-World Use Cases of @dataclass

1.Data Transfer Objects - Used to pass structured data between layers (e.g., APIs, services, or functions).Avoids writing repetitive __init__ and makes debugging/printing objects much easier.
2. Configuration Management  -  Dataclasses are great for handling app or ML model configurations.Provides default values, easy to serialize (convert to dict or JSON), and clean structure.
3.Validation and Type Safety - You can validate inputs on initialization using __post_init__. Keeps type-checked, validated data structures clean and maintainable.'''


'''Imp points:-

By default:
If your dataclass is mutable (frozen=False), Python sets __hash__ = None to prevent hashing.
If your dataclass is frozen=True (immutable), Python automatically makes it hashable using all its fields.
You can override this behavior manually with the unsafe_hash=True argument.'''

# TYPE 1 - Default behavior (not hashable)
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

# Create an object
s1 = Student("Alice", 21)
s2 = Student("Alice", 21)

print(s1 == s2)

# Explanation: Since frozen=False (default), dataclass assumes object is mutable.So it disables __hash__ to avoid inconsistent hashing.


# TYPE 2 - Using frozen=True (hashable automatically)

from dataclasses import dataclass

@dataclass(frozen=True)
class Student:
    name: str
    age: int

s1 = Student("Alice", 21)
s2 = Student("Alice", 21)

print(s1 == s2)        # True
print(hash(s1))        # Works fine
print({s1, s2})        # Set treats them as same (since same hash)

# Explanation: frozen=True makes the instance immutable (fields cannot be changed).Python safely generates a __hash__ method based on all fields.

# TYPE 3 — Using unsafe_hash=True (mutable but hashable)

from dataclasses import dataclass
@dataclass(unsafe_hash=True)
class Student:
    name: str
    age: int

s1 = Student("Alice", 21)
print(hash(s1))  # Works — but risky!
s1.age = 22      # You can still mutate it

print(hash(s1))  # Hash changed! ⚠️ (this can break dictionaries/sets)

# Explanation: unsafe_hash=True forces dataclass to create a __hash__ even though it’s mutable.Use only if you know what you’re doing.

# TYPE 4 — Custom __hash__ method

from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int

    def __hash__(self):
        # Only hash based on name
        return hash(self.name)

s1 = Student("Alice", 21)
s2 = Student("Alice", 25)

print(hash(s1), hash(s2))  # same, since only 'name' is considered
print({s1, s2})            # only one element in the set

'''IMP USE CASE-
1. Storing Immutable Configurations in a Set or Dict.
2. Caching or Memoization - Suppose you’re writing a function that processes large datasets.You want to cache results for the same input configuration.'''

** When not to use hashing
If your dataclass is mutable (e.g., Employee whose salary can change), don’t rely on hashing — a change could invalidate the stored hash.
