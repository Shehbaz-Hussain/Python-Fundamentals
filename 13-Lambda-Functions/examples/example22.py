"""
File: example22.py
Topic: Lambda Function with sorted() for Ranking Data

Description:
This example demonstrates how lambda functions can be used with
sorted() to rank records according to a specific value.

Concepts Covered:
- Lambda functions with sorted()
- key parameter
- Descending order sorting
- Ranking data

Python Version:
Python 3.13+
"""


# Creating a list of player records
players = [
    ("Ali", 85),
    ("Sara", 95),
    ("Ahmed", 78),
    ("Zain", 90)
]


# Sorting players by score in descending order
ranked_players = sorted(
    players,
    key=lambda player: player[1],
    reverse=True
)


# Displaying ranked players
print(ranked_players)


"""
Expected Output:

[('Sara', 95), ('Zain', 90), ('Ali', 85), ('Ahmed', 78)]


Explanation:

1. A list of player records is created.
2. Each record contains:
   - Player name
   - Player score

3. The sorted() function arranges the records.
4. The key parameter receives a lambda function.
5. The lambda function extracts the score from each record.
6. The reverse=True parameter sorts scores from highest to
   lowest.
7. The final ranking is stored in 'ranked_players'.

Best Practice:

Use lambda functions with sorted() for simple ranking rules.
For complex ranking systems involving multiple conditions,
use a regular function.

Real-World Relevance:

Ranking data is widely used in leaderboard systems, sports
applications, recommendation systems, analytics platforms,
and machine learning evaluation workflows.
"""