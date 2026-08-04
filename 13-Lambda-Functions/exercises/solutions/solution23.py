"""
===============================================================================
Module: 13 - Lambda Functions
Solution: 23
Exercise Title: Automation - Log File Preprocessing
Difficulty: Advanced

Objective:
    Use lambda functions to preprocess application log records for reporting
    and automation tasks using map(), filter(), reduce(), and sorted().

Python Version:
    Python 3.13+

Author:
    Python-Programming-Foundation
===============================================================================
"""

from functools import reduce

# -----------------------------------------------------------------------------
# Solution
# -----------------------------------------------------------------------------

# Create the application log records.
logs = [
    ("09:00", "INFO", 120),
    ("09:05", "ERROR", 840),
    ("09:10", "WARNING", 320),
    ("09:15", "INFO", 110),
    ("09:20", "ERROR", 960),
    ("09:25", "INFO", 140),
    ("09:30", "WARNING", 410),
    ("09:35", "ERROR", 780),
]

# Create a processed log list with status information.
processed_logs = list(
    map(
        lambda log: (
            log[0],
            log[1],
            log[2],
            "Slow" if log[2] > 500 else "Normal",
        ),
        logs,
    )
)

# Extract only ERROR log records.
error_logs = list(
    filter(
        lambda log: log[1] == "ERROR",
        processed_logs,
    )
)

# Calculate the total response time.
total_response_time = reduce(
    lambda total, log: total + log[2],
    processed_logs,
    0,
)

# Calculate the average response time.
average_response_time = total_response_time / len(processed_logs)

# Sort log records by response time in descending order.
logs_sorted_by_response_time = sorted(
    processed_logs,
    key=lambda log: log[2],
    reverse=True,
)

# -----------------------------------------------------------------------------
# Challenge Solutions
# -----------------------------------------------------------------------------

# Create a list containing only response times.
response_times = list(
    map(
        lambda log: log[2],
        logs,
    )
)

# Count the number of ERROR log records.
error_log_count = len(error_logs)

# Display log records whose response time exceeds 400 ms.
logs_above_400_ms = list(
    filter(
        lambda log: log[2] > 400,
        processed_logs,
    )
)

# Sort log records alphabetically by log level and then by timestamp.
logs_sorted_by_level_and_time = sorted(
    processed_logs,
    key=lambda log: (log[1], log[0]),
)

# -----------------------------------------------------------------------------
# Display Results
# -----------------------------------------------------------------------------

print("Original Log Records:")
print(logs)

print("\nProcessed Log Records:")
print(processed_logs)

print("\nERROR Log Records:")
print(error_logs)

print("\nTotal Response Time:")
print(total_response_time)

print("\nAverage Response Time:")
print(average_response_time)

print("\nLog Records Sorted by Response Time (Highest First):")
print(logs_sorted_by_response_time)

print("\nResponse Times:")
print(response_times)

print("\nTotal ERROR Log Records:")
print(error_log_count)

print("\nLog Records with Response Time Greater Than 400 ms:")
print(logs_above_400_ms)

print("\nLog Records Sorted by Log Level and Timestamp:")
print(logs_sorted_by_level_and_time)

print("\nSummary Report")
print("-" * 30)
print(f"Total Logs: {len(logs)}")
print(f"Total ERROR Logs: {error_log_count}")
print(f"Average Response Time: {average_response_time} ms")


"""
===============================================================================
Expected Output
===============================================================================

Original Log Records:
[('09:00', 'INFO', 120), ('09:05', 'ERROR', 840),
 ('09:10', 'WARNING', 320), ('09:15', 'INFO', 110),
 ('09:20', 'ERROR', 960), ('09:25', 'INFO', 140),
 ('09:30', 'WARNING', 410), ('09:35', 'ERROR', 780)]

Processed Log Records:
[('09:00', 'INFO', 120, 'Normal'),
 ('09:05', 'ERROR', 840, 'Slow'),
 ('09:10', 'WARNING', 320, 'Normal'),
 ('09:15', 'INFO', 110, 'Normal'),
 ('09:20', 'ERROR', 960, 'Slow'),
 ('09:25', 'INFO', 140, 'Normal'),
 ('09:30', 'WARNING', 410, 'Normal'),
 ('09:35', 'ERROR', 780, 'Slow')]

ERROR Log Records:
[('09:05', 'ERROR', 840, 'Slow'),
 ('09:20', 'ERROR', 960, 'Slow'),
 ('09:35', 'ERROR', 780, 'Slow')]

Total Response Time:
3680

Average Response Time:
460.0

Log Records Sorted by Response Time (Highest First):
[('09:20', 'ERROR', 960, 'Slow'),
 ('09:05', 'ERROR', 840, 'Slow'),
 ('09:35', 'ERROR', 780, 'Slow'),
 ('09:30', 'WARNING', 410, 'Normal'),
 ('09:10', 'WARNING', 320, 'Normal'),
 ('09:25', 'INFO', 140, 'Normal'),
 ('09:00', 'INFO', 120, 'Normal'),
 ('09:15', 'INFO', 110, 'Normal')]

Response Times:
[120, 840, 320, 110, 960, 140, 410, 780]

Total ERROR Log Records:
3

Log Records with Response Time Greater Than 400 ms:
[('09:05', 'ERROR', 840, 'Slow'),
 ('09:20', 'ERROR', 960, 'Slow'),
 ('09:30', 'WARNING', 410, 'Normal'),
 ('09:35', 'ERROR', 780, 'Slow')]

Log Records Sorted by Log Level and Timestamp:
[('09:05', 'ERROR', 840, 'Slow'),
 ('09:20', 'ERROR', 960, 'Slow'),
 ('09:35', 'ERROR', 780, 'Slow'),
 ('09:00', 'INFO', 120, 'Normal'),
 ('09:15', 'INFO', 110, 'Normal'),
 ('09:25', 'INFO', 140, 'Normal'),
 ('09:10', 'WARNING', 320, 'Normal'),
 ('09:30', 'WARNING', 410, 'Normal')]

Summary Report
------------------------------
Total Logs: 8
Total ERROR Logs: 3
Average Response Time: 460.0 ms

===============================================================================
Step-by-Step Explanation
===============================================================================

1. A list of application log records is created.
2. The map() function creates a new list containing each log record along
   with a status:
   - "Slow" if the response time is greater than 500 ms.
   - "Normal" otherwise.
3. The filter() function extracts only the ERROR log records.
4. The reduce() function calculates the total response time of all logs.
5. The average response time is calculated using the total response time
   divided by the number of log records.
6. The sorted() function orders the log records from the highest response
   time to the lowest.
7. The challenge tasks demonstrate additional processing by extracting
   response times, counting ERROR logs, filtering slow responses, sorting
   alphabetically, and generating a summary report.

How the Lambda Expressions Work
-------------------------------

Lambda 1:

    lambda log: (
        log[0],
        log[1],
        log[2],
        "Slow" if log[2] > 500 else "Normal"
    )

Creates a processed log record with a status field.

Lambda 2:

    lambda log: log[1] == "ERROR"

Selects only ERROR log records.

Lambda 3:

    lambda total, log: total + log[2]

Accumulates the response times into a single total.

Lambda 4:

    lambda log: log[2]

Returns the response time for sorting.

Lambda 5:

    lambda log: (log[1], log[0])

Sorts first by log level and then by timestamp.

===============================================================================
Concepts Used
===============================================================================

- Lambda functions
- map()
- filter()
- reduce()
- sorted()
- key parameter
- Conditional expressions
- Lists
- Tuples
- Arithmetic operations

===============================================================================
Time Complexity
===============================================================================

Overall Complexity: O(n log n)

Explanation:
- map(): O(n)
- filter(): O(n)
- reduce(): O(n)
- sorted(): O(n log n)

Sorting is the most expensive operation.

===============================================================================
Space Complexity
===============================================================================

Overall Complexity: O(n)

Explanation:
Additional lists are created for transformed, filtered, and sorted data while
keeping the original dataset unchanged.

===============================================================================
Best Practices
===============================================================================

- Preserve the original log records.
- Keep lambda expressions concise and focused.
- Use meaningful variable names.
- Use functional programming tools for preprocessing pipelines.

===============================================================================
Common Mistakes
===============================================================================

- Forgetting to import reduce() from functools.
- Using incorrect tuple indexes.
- Filtering the original dataset instead of the processed records when the
  status field is required.
- Omitting reverse=True when sorting in descending order.
- Forgetting to convert map() and filter() objects into lists.

===============================================================================
Alternative Approach
===============================================================================

Instead of counting ERROR logs with len(error_logs), reduce() could be used
to count matching records by accumulating 1 for each ERROR record.

===============================================================================
Real-World Relevance
===============================================================================

This workflow is commonly used in:

- Application monitoring
- Log preprocessing
- Performance analysis
- DevOps automation
- System health reporting

===============================================================================
Key Takeaways
===============================================================================

- map() enriches records with calculated information.
- filter() extracts records matching operational criteria.
- reduce() aggregates numerical values efficiently.
- sorted() enables custom ordering for reports.
- Lambda functions provide concise solutions for data preprocessing tasks.
===============================================================================
"""