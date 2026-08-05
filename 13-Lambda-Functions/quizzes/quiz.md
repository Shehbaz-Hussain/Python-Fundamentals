# Module 13 - Lambda Functions Quiz

## Python Programming Foundation

**Python Version:** 3.13+  
**Module:** 13 - Lambda Functions  
**Difficulty:** Beginner → Intermediate → Advanced  

---

# Part 1: Multiple Choice Questions (MCQs)

## Beginner Level

### 1. What is a lambda function in Python?

A) A function with a name  
B) An anonymous function without a name  
C) A Python class  
D) A Python module  

---

### 2. Which keyword is used to create a lambda function?

A) function  
B) def  
C) lambda  
D) anonymous  

---

### 3. Which is the correct lambda function syntax?

A)

```python
lambda parameters: expression
```

B)

```python
lambda expression(parameters)
```

C)

```python
def lambda(parameters)
```

D)

```python
function => expression
```

---

### 4. What is the output of this code?

```python
square = lambda x: x * x

print(square(5))
```

A) 10  
B) 15  
C) 25  
D) Error  

---

### 5. Lambda functions are mainly used for:

A) Large programs  
B) Short and simple operations  
C) Creating classes  
D) Importing packages  

---

### 6. A lambda function can contain:

A) Multiple statements  
B) One expression  
C) Multiple classes  
D) Multiple files  

---

### 7. Which function applies a function to every item in an iterable?

A) filter()  
B) map()  
C) sorted()  
D) reduce()  

---

### 8. What does map() return in Python 3?

A) List  
B) Tuple  
C) Map object  
D) Dictionary  

---

### 9. Which function is used to select items based on a condition?

A) map()  
B) filter()  
C) sorted()  
D) print()  

---

### 10. Which function is commonly used with lambda for sorting?

A) input()  
B) sorted()  
C) type()  
D) len()  

---

# Intermediate Level

### 11. What is the output?

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

A) [1, 2, 3, 4]  
B) [2, 4, 6, 8]  
C) [1, 4, 9, 16]  
D) Error  

---

### 12. What is the main purpose of map()?

A) Sorting data  
B) Transforming data  
C) Removing data  
D) Printing data  

---

### 13. What is the purpose of filter()?

A) Transform every value  
B) Select values based on a condition  
C) Sort values  
D) Create variables  

---

### 14. What does the key parameter in sorted() do?

A) Defines sorting logic  
B) Creates dictionary keys  
C) Deletes records  
D) Converts data  

---

### 15. What does this code do?

```python
students = [
    {"name": "Ali", "marks": 90},
    {"name": "Sara", "marks": 80}
]

result = sorted(
    students,
    key=lambda student: student["marks"]
)
```

A) Removes students  
B) Sorts students by marks  
C) Calculates marks  
D) Filters students  

---

### 16. What is the output?

```python
add = lambda a, b: a + b

print(add(3, 7))
```

A) 37  
B) 10  
C) Error  
D) None  

---

### 17. Which task is suitable for map()?

A) Convert temperatures  
B) Find passing students  
C) Sort products  
D) Remove duplicates  

---

### 18. Which task is suitable for filter()?

A) Increase salaries  
B) Select expensive products  
C) Calculate totals  
D) Convert names  

---

### 19. What does reverse=True do in sorted()?

A) Sorts descending  
B) Deletes values  
C) Stops sorting  
D) Converts data  

---

### 20. Lambda functions are best used for:

A) Small expressions  
B) Large algorithms  
C) Complete applications  
D) Database systems  

---

# Advanced Level

### 21. Lambda functions are associated with:

A) Functional programming  
B) Hardware programming  
C) Networking  
D) Operating systems  

---

### 22. Which statement is incorrect?

A) Lambda functions can accept parameters  
B) Lambda functions return values  
C) Lambda functions can contain many statements  
D) Lambda functions can be stored in variables  

---

### 23. Why avoid complex lambda expressions?

A) They reduce readability  
B) Python cannot execute them  
C) They cannot return values  
D) They are always slower  

---

### 24. Which function combines values into one result?

A) map()  
B) filter()  
C) reduce()  
D) sorted()  

---

### 25. Where is reduce() available?

A) Built-in functions  
B) functools module  
C) random module  
D) math module  

---

### 26. A lambda function can be:

A) Stored in a variable  
B) Passed as an argument  
C) Returned from a function  
D) All of these  

---

### 27. The key parameter in sorted() is used for:

A) Custom sorting  
B) Encryption  
C) Filtering  
D) File handling  

---

### 28. Which approach improves maintainability?

A) Writing huge lambdas  
B) Using lambda everywhere  
C) Using normal functions for complex logic  
D) Avoiding names  

---

### 29. Lambda functions are commonly used in:

A) Data processing  
B) Machine learning preprocessing  
C) Automation  
D) All of these  

---

### 30. Which statement is true?

A) Lambda replaces all functions  
B) Lambda is useful for small operations  
C) Lambda cannot process lists  
D) Lambda cannot return values  

---

# Part 2: True / False Questions

### 31. Lambda functions are anonymous functions.

True / False

---

### 32. Lambda functions are created using the def keyword.

True / False

---

### 33. map() applies a function to every element.

True / False

---

### 34. filter() selects values based on conditions.

True / False

---

### 35. sorted() can use lambda functions with key.

True / False

---

### 36. Lambda functions can contain multiple statements.

True / False

---

### 37. Every lambda function improves readability.

True / False

---

### 38. Lambda functions are useful in data processing.

True / False

---

### 39. Complex logic should always be written using lambda.

True / False

---

### 40. Lambda functions can work with dictionaries.

True / False

---

# Part 3: Short Answer Questions

### 41. What is a lambda function?

---

### 42. Write the syntax of a lambda function.

---

### 43. Difference between normal functions and lambda functions?

---

### 44. Explain the purpose of map().

---

### 45. Explain the purpose of filter().

---

### 46. Explain the key parameter in sorted().

---

### 47. Why should lambda functions be simple?

---

### 48. Give a real-world example of lambda usage.

---

### 49. Which programming concept is related to lambda functions?

---

### 50. When should lambda functions be avoided?

---