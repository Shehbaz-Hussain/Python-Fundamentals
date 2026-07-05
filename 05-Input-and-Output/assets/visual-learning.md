# Visual Learning Guide: Input and Output

## 1. Concept Map

```text
User Input --> Program Processing --> Program Output
    |                 |                   |
 input()         variables/data         print()
```

## 2. Flow of a Simple Program

```text
Start
  |
  v
Ask for input
  |
  v
Store input
  |
  v
Process data
  |
  v
Show output
  |
  v
End
```

## 3. Print Function Flow

```text
print(value1, value2, sep=..., end=...)
   |          |         |          |
   |          |         |          +--> end of line
   |          |         +--> separator between values
   |          +--> values to display
   +--> output to console
```

## 4. Input Function Flow

```text
input(prompt)
   |
   +--> displays message
   |
   +--> waits for user entry
   |
   +--> returns entered text
```

## 5. Memory Trick

- Input = Inward movement of data
- Output = Outward movement of data

## 6. Learning Shortcut

Remember this pattern:

```python
data = input("Enter something: ")
print(f"You entered: {data}")
```

## 7. Comparison Table

| Concept | Purpose |
|---|---|
| `input()` | Receive data |
| `print()` | Show data |
| `sep` | Customize separators |
| `end` | Customize ending characters |
| `f-strings` | Format output clearly |
