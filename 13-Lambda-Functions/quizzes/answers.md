# Module 13 - Lambda Functions Quiz Answers

## Python Programming Foundation

**Python Version:** 3.13+  
**Module:** 13 - Lambda Functions  

---

# Part 1: Multiple Choice Questions Answers

## Beginner Level

### 1. What is a lambda function in Python?

**Correct Answer:** B) An anonymous function without a name

**Explanation:**
A lambda function is a small anonymous function created using the `lambda` keyword. It does not require a function name like functions created with `def`.

**Related Concept:**
Lambda Functions

---

### 2. Which keyword is used to create a lambda function?

**Correct Answer:** C) lambda

**Explanation:**
Python uses the `lambda` keyword to define anonymous functions.

**Related Concept:**
Lambda Syntax

---

### 3. Which is the correct lambda function syntax?

**Correct Answer:** A)

```python
lambda parameters: expression
```

**Explanation:**
A lambda function contains parameters followed by a single expression separated by a colon.

**Related Concept:**
Lambda Function Structure

---

### 4. What is the output of this code?

```python
square = lambda x: x * x
print(square(5))
```

**Correct Answer:** C) 25

**Explanation:**
The lambda function multiplies the value by itself. `5 * 5` gives `25`.

**Related Concept:**
Lambda Function Execution

---

### 5. Lambda functions are mainly used for:

**Correct Answer:** B) Short and simple operations

**Explanation:**
Lambda functions are designed for small expressions where creating a full function using `def` is unnecessary.

**Related Concept:**
Anonymous Functions

---

### 6. A lambda function can contain:

**Correct Answer:** B) One expression

**Explanation:**
Lambda functions support only a single expression and automatically return its result.

**Related Concept:**
Lambda Limitations

---

### 7. Which function applies a function to every item in an iterable?

**Correct Answer:** B) map()

**Explanation:**
`map()` applies a given function to each element of an iterable.

**Related Concept:**
Data Transformation

---

### 8. What does map() return in Python 3?

**Correct Answer:** C) Map object

**Explanation:**
Python 3 returns a map iterator. It is commonly converted into a list using `list()`.

**Related Concept:**
Iterators

---

### 9. Which function is used to select items based on a condition?

**Correct Answer:** B) filter()

**Explanation:**
`filter()` returns elements that satisfy a given condition.

**Related Concept:**
Data Filtering

---

### 10. Which function is commonly used with lambda for sorting?

**Correct Answer:** B) sorted()

**Explanation:**
`sorted()` accepts a `key` parameter that can use lambda functions for custom sorting.

**Related Concept:**
Custom Sorting

---

# Intermediate Level

### 11. What is the output?

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
```

**Correct Answer:** B) [2, 4, 6, 8]

**Explanation:**
The lambda function doubles every number in the list.

**Related Concept:**
map() Transformation

---

### 12. What is the main purpose of map()?

**Correct Answer:** B) Transforming data

**Explanation:**
`map()` creates new values by applying a function to each element.

**Related Concept:**
Functional Programming

---

### 13. What is the purpose of filter()?

**Correct Answer:** B) Select values based on a condition

**Explanation:**
`filter()` keeps only elements where the condition returns True.

**Related Concept:**
Filtering Data

---

### 14. What does the key parameter in sorted() do?

**Correct Answer:** A) Defines sorting logic

**Explanation:**
The `key` parameter specifies the function used to determine sorting order.

**Related Concept:**
sorted() Key Function

---

### 15. What does this code do?

**Correct Answer:** B) Sorts students by marks

**Explanation:**
The lambda function extracts the marks value used for sorting.

**Related Concept:**
Lambda with sorted()

---

### 16. What is the output?

```python
add = lambda a, b: a + b
```

**Correct Answer:** B) 10

**Explanation:**
The function adds `3` and `7`.

**Related Concept:**
Lambda Parameters

---

### 17. Which task is suitable for map()?

**Correct Answer:** A) Convert temperatures

**Explanation:**
map() is used when every item needs transformation.

**Related Concept:**
Transformation Pipeline

---

### 18. Which task is suitable for filter()?

**Correct Answer:** B) Select expensive products

**Explanation:**
Filtering selects records based on conditions.

**Related Concept:**
Conditional Selection

---

### 19. What does reverse=True do in sorted()?

**Correct Answer:** A) Sorts descending

**Explanation:**
It changes sorting order from ascending to descending.

**Related Concept:**
Sorting Direction

---

### 20. Lambda functions are best used for:

**Correct Answer:** A) Small expressions

**Explanation:**
Lambda functions are intended for short operations.

**Related Concept:**
Best Practices

---

# Advanced Level

### 21. Lambda functions are associated with:

**Correct Answer:** A) Functional programming

**Explanation:**
Lambda functions are commonly used in functional programming patterns.

**Related Concept:**
Functional Programming

---

### 22. Which statement is incorrect?

**Correct Answer:** C) Lambda functions can contain many statements

**Explanation:**
Lambda functions support only one expression.

**Related Concept:**
Lambda Limitations

---

### 23. Why avoid complex lambda expressions?

**Correct Answer:** A) They reduce readability

**Explanation:**
Complex lambdas make code harder to understand and maintain.

**Related Concept:**
Code Readability

---

### 24. Which function combines values into one result?

**Correct Answer:** C) reduce()

**Explanation:**
`reduce()` repeatedly applies a function to combine values.

**Related Concept:**
Aggregation

---

### 25. Where is reduce() available?

**Correct Answer:** B) functools module

**Explanation:**
In Python, reduce() is provided by the `functools` module.

**Related Concept:**
Python Modules

---

### 26. A lambda function can be:

**Correct Answer:** D) All of these

**Explanation:**
Lambda functions can be stored, passed, and returned like normal functions.

**Related Concept:**
First-Class Functions

---

### 27. The key parameter in sorted() is used for:

**Correct Answer:** A) Custom sorting

**Explanation:**
It allows sorting based on a calculated value.

**Related Concept:**
Sorting Strategy

---

### 28. Which approach improves maintainability?

**Correct Answer:** C) Using normal functions for complex logic

**Explanation:**
Complex logic should use named functions for readability.

**Related Concept:**
Clean Code

---

### 29. Lambda functions are commonly used in:

**Correct Answer:** D) All of these

**Explanation:**
Lambda functions are useful in data processing, automation, and ML preprocessing.

**Related Concept:**
Real-World Applications

---

### 30. Which statement is true?

**Correct Answer:** B) Lambda is useful for small operations

**Explanation:**
Lambda functions are designed for simple temporary functions.

**Related Concept:**
Lambda Best Practices

---

# Part 2: True / False Answers

### 31. Lambda functions are anonymous functions.

**Answer:** True

**Explanation:**
Lambda functions do not require a function name.

**Related Concept:**
Anonymous Functions

---

### 32. Lambda functions are created using the def keyword.

**Answer:** False

**Explanation:**
Lambda functions use the `lambda` keyword.

**Related Concept:**
Lambda Syntax

---

### 33. map() applies a function to every element.

**Answer:** True

**Explanation:**
map() processes each item in an iterable.

**Related Concept:**
map()

---

### 34. filter() selects values based on conditions.

**Answer:** True

**Explanation:**
filter() keeps values where the condition is True.

**Related Concept:**
filter()

---

### 35. sorted() can use lambda functions with key.

**Answer:** True

**Explanation:**
Lambda functions are commonly used as key functions.

**Related Concept:**
sorted()

---

### 36. Lambda functions can contain multiple statements.

**Answer:** False

**Explanation:**
Lambda functions allow only one expression.

**Related Concept:**
Lambda Restrictions

---

### 37. Every lambda function improves readability.

**Answer:** False

**Explanation:**
Complex lambda expressions can reduce readability.

**Related Concept:**
Code Quality

---

### 38. Lambda functions are useful in data processing.

**Answer:** True

**Explanation:**
They are commonly used in transformation and filtering tasks.

**Related Concept:**
Data Processing

---

### 39. Complex logic should always be written using lambda.

**Answer:** False

**Explanation:**
Complex logic should use normal functions.

**Related Concept:**
Best Practices

---

### 40. Lambda functions can work with dictionaries.

**Answer:** True

**Explanation:**
Lambda functions can process dictionary values.

**Related Concept:**
Data Structures

---

# Part 3: Short Answer Answers

### 41. What is a lambda function?

**Answer:**

A lambda function is a small anonymous function created using the lambda keyword that contains a single expression.

**Related Concept:**
Lambda Functions

---

### 42. Write the syntax of a lambda function.

**Answer:**

```python
lambda parameters: expression
```

**Related Concept:**
Lambda Syntax

---

### 43. Difference between normal functions and lambda functions?

**Answer:**

Normal functions use `def` and can contain multiple statements. Lambda functions are anonymous and contain one expression.

**Related Concept:**
Function Types

---

### 44. Explain the purpose of map().

**Answer:**

`map()` applies a function to every element of an iterable and returns transformed results.

**Related Concept:**
Transformation

---

### 45. Explain the purpose of filter().

**Answer:**

`filter()` selects elements from an iterable based on a condition.

**Related Concept:**
Filtering

---

### 46. Explain the key parameter in sorted().

**Answer:**

The key parameter defines the function that determines how elements are compared during sorting.

**Related Concept:**
Custom Sorting

---

### 47. Why should lambda functions be simple?

**Answer:**

Simple lambda functions improve readability and make code easier to maintain.

**Related Concept:**
Clean Code

---

### 48. Give a real-world example of lambda usage.

**Answer:**

Lambda functions can calculate product discounts, filter customers, or rank employees.

**Related Concept:**
Practical Applications

---

### 49. Which programming concept is related to lambda functions?

**Answer:**

Functional programming.

**Related Concept:**
Programming Paradigms

---

### 50. When should lambda functions be avoided?

**Answer:**

Lambda functions should be avoided when the logic becomes complex or requires multiple statements.

**Related Concept:**
Best Practices

---