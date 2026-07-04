# Interview Questions: Data Types

## Beginner Questions

1. What is a data type in Python?
2. What is the difference between `int` and `float`?
3. What is a string?
4. What is the difference between a list and a tuple?
5. What is a dictionary?
6. What is a set?
7. What does `None` represent?
8. What is the difference between mutable and immutable?
9. What is a boolean?
10. What is the difference between `==` and `is`?
11. What is a variable?
12. What is an object in Python?
13. Why are data types important?
14. How do you create a tuple?
15. How do you create a list?
16. What happens when you add two strings?
17. What happens if you try to add a string and an integer?
18. What is type conversion?
19. How do you convert a string to an integer?
20. How do you convert a number to a string?

## Intermediate Questions

1. Why is Python dynamically typed?
2. What is the difference between static and dynamic typing?
3. What is the difference between strong and weak typing?
4. Why are strings immutable?
5. What is the purpose of `bytes`?
6. What is the difference between `list` and `array`?
7. How does a dictionary store data?
8. What is hashing in relation to sets and dictionaries?
9. What is the difference between `range` and `list`?
10. Why might `tuple` be preferable to `list` for fixed data?

## Advanced Questions

1. How does Python manage memory for small integers?
2. What is object identity?
3. What is reference counting?
4. How does garbage collection work in Python?
5. Why can mutable default arguments be risky?
6. How does Python implement `NoneType`?
7. What is the difference between shallow and deep copy?
8. Why are sets unordered?
9. What is the performance impact of using tuples instead of lists?
10. How can data types influence AI pipelines?

## Detailed Answers

### Beginner

1. A data type describes the kind of value stored in memory.
2. `int` stores whole numbers; `float` stores decimal values.
3. A string is a sequence of characters used for text.
4. A list is mutable and ordered; a tuple is immutable and ordered.
5. A dictionary stores data as key-value pairs.
6. A set stores unique values without maintaining order.
7. `None` represents the absence of a value.
8. Mutable objects can change after creation; immutable ones cannot.
9. A boolean represents `True` or `False`.
10. `==` compares values; `is` compares object identity.

### Intermediate

1. Python is dynamically typed because it infers types at runtime.
2. Static typing checks types before execution; dynamic typing checks them during execution.
3. Strong typing prevents implicit, unsafe conversions; weak typing allows them.
4. Strings are immutable so Python can safely share and optimize them.
5. `bytes` stores binary data and is useful for file and network data.
6. A list is a Python collection; `array` is more specialized and uses less overhead for numeric storage.
7. A dictionary stores values by key, allowing fast lookup.
8. Sets and dictionaries use hashing to locate items quickly.
9. `range` produces values lazily and uses less memory than a list for large sequences.
10. A tuple is safer when the values should not change.

### Advanced

1. Python may reuse small integer objects for efficiency.
2. Object identity is the unique identity of an object in memory.
3. Reference counting tracks how many references point to an object.
4. Garbage collection removes objects that are no longer referenced.
5. Mutable default arguments can accidentally share state between calls.
6. `NoneType` is the type of the singleton `None`.
7. Shallow copy duplicates the outer structure; deep copy duplicates nested objects too.
8. Sets are unordered because they are based on hashing and membership logic.
9. Tuples are generally slightly faster and use less memory than lists for fixed collections.
10. Data types influence performance, correctness, and representational choices in AI systems.
