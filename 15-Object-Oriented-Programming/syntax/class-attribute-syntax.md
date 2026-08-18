Class Attribute Syntax

Introduction

A class attribute is an attribute that is defined directly inside a class.

Unlike an instance attribute, which belongs to a specific object, a class attribute belongs to the class itself and can be accessed by instances when they do not have an instance attribute with the same name.

Class attributes are useful for storing data that is logically shared by objects of the same class.

---

Basic Syntax

class ClassName:
    attribute_name = value

Syntax Breakdown

- "class" defines the class.
- "ClassName" is the name of the class.
- "attribute_name" is the class attribute.
- "value" is the value assigned to the class attribute.

---

Simple Example

class Student:
    university = "KIU"


print(Student.university)

Output:

KIU

Here, "university" is a class attribute because it is defined directly inside the class body.

---

Accessing a Class Attribute Through an Object

A class attribute can also be accessed through an instance.

class Student:
    university = "KIU"


student1 = Student()

print(student1.university)

Output:

KIU

Python looks for "university" on "student1". If it does not find an instance attribute with that name, it looks at the class.

---

Class Attributes and Multiple Objects

Multiple objects can access the same class attribute.

class Student:
    university = "KIU"


student1 = Student()
student2 = Student()

print(student1.university)
print(student2.university)

Output:

KIU
KIU

Both objects can access the class attribute defined by "Student".

---

Modifying a Class Attribute Through the Class

A class attribute can be changed through the class itself.

class Student:
    university = "KIU"


Student.university = "COMSATS"

print(Student.university)

Output:

COMSATS

The assignment changes the attribute stored on the class.

---

Effect on Objects

If an object does not have its own attribute with the same name, it will see the updated class attribute.

class Student:
    university = "KIU"


student1 = Student()
student2 = Student()

Student.university = "COMSATS"

print(student1.university)
print(student2.university)

Output:

COMSATS
COMSATS

Both objects access the updated class attribute.

---

Instance Attribute with the Same Name

An instance can have an attribute with the same name as a class attribute.

class Student:
    university = "KIU"


student1 = Student()

student1.university = "COMSATS"

print(student1.university)
print(Student.university)

Output:

COMSATS
KIU

The statement:

student1.university = "COMSATS"

creates an instance attribute named "university" for "student1".

It does not change the class attribute.

---

Class Attribute vs Instance Attribute

Consider:

class Student:
    university = "KIU"

    def __init__(self, name):
        self.name = name

Here:

university → class attribute
name       → instance attribute

The class attribute is shared through the class, while each object has its own "name" attribute.

---

Example with Class and Instance Attributes

class Student:
    university = "KIU"

    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")
student2 = Student("Ali")

print(student1.name)
print(student2.name)

print(student1.university)
print(student2.university)

Output:

Shehbaz
Ali
KIU
KIU

The students have different names but access the same class-level university value.

---

Modifying an Instance Attribute

Changing an instance attribute affects only that particular object.

class Student:
    university = "KIU"

    def __init__(self, name):
        self.name = name


student1 = Student("Shehbaz")
student2 = Student("Ali")

student1.name = "Ahmed"

print(student1.name)
print(student2.name)

Output:

Ahmed
Ali

The class attribute and instance attribute have different roles.

---

Common Use of Class Attributes

Class attributes are useful for values that logically apply to all instances.

For example:

class Student:
    university = "KIU"

Another example:

class Employee:
    company = "ABC Software"

Another example:

class Circle:
    pi = 3.14159

These values are associated with the class rather than with one particular object.

---

Class Attribute with a Method

A class attribute can be accessed inside an instance method through "self" when the instance does not override that attribute.

class Student:
    university = "KIU"

    def show_university(self):
        print(self.university)


student1 = Student()

student1.show_university()

Output:

KIU

A method can also access the class attribute explicitly through the class name:

class Student:
    university = "KIU"

    def show_university(self):
        print(Student.university)


student1 = Student()

student1.show_university()

Output:

KIU

---

General Syntax

The basic class attribute syntax is:

class ClassName:
    class_attribute = value

A class can contain both class attributes and instance attributes:

class ClassName:
    class_attribute = value

    def __init__(self, value):
        self.instance_attribute = value

---

Important Points

- A class attribute is defined directly inside the class body.
- Class attributes belong to the class.
- Instances can access class attributes.
- Class attributes are useful for data shared by instances.
- A class attribute can be accessed using "ClassName.attribute".
- An instance can access it using "object_name.attribute".
- Assigning the same attribute through an instance creates or modifies an instance attribute.
- An instance attribute with the same name takes precedence when accessed through that instance.
- Class attributes and instance attributes serve different purposes.

---

Summary

The basic syntax for a class attribute is:

class ClassName:
    attribute_name = value

For example:

class Student:
    university = "KIU"

A class attribute is appropriate when a value logically belongs to the class as a whole rather than representing unique state for each individual object.