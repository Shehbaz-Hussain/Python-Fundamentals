"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Exercise 23: Automation - Log File Preprocessing

Difficulty:
Advanced

Estimated Time:
35–45 Minutes

Objective:
Use lambda functions to preprocess application log records for reporting
and automation tasks.

Instructions:
An application stores log entries in the following format:

(Timestamp, Log Level, Response Time in ms)

Create the following list:

logs = [
    ("09:00", "INFO", 120),
    ("09:05", "ERROR", 840),
    ("09:10", "WARNING", 320),
    ("09:15", "INFO", 110),
    ("09:20", "ERROR", 960),
    ("09:25", "INFO", 140),
    ("09:30", "WARNING", 410),
    ("09:35", "ERROR", 780)
]

Perform the following tasks:

1. Display the original log records.

2. Use map() with a lambda function to create a new list containing:

   (
       Timestamp,
       Log Level,
       Response Time,
       Status
   )

   Where:
   - "Slow" if response time is greater than 500 ms.
   - "Normal" otherwise.

3. Use filter() with a lambda function to extract only ERROR log
   records.

4. Import reduce from functools and calculate the total response time
   of all log records.

5. Calculate the average response time.

6. Use sorted() with a lambda function to sort log records by response
   time from highest to lowest.

7. Display all generated results with meaningful headings.

Requirements:
- Use lambda functions.
- Use map(), filter(), reduce(), and sorted().
- Keep the original dataset unchanged.
- Follow PEP 8 style guidelines.

Challenge:

1. Create a list containing only response times.
2. Count the total number of ERROR log records.
3. Display only log records whose response time exceeds 400 ms.
4. Sort the records alphabetically by log level and then by timestamp.
5. Create a summary report showing:
   - Total logs
   - Total ERROR logs
   - Average response time
===============================================================================
"""