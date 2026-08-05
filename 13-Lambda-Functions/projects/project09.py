"""
===============================================================================
Python Programming Foundation
Module 13 - Lambda Functions

Project 09: Ranking and Recommendation System

Difficulty:
Advanced

Estimated Completion Time:
75-90 Minutes

Objective:
Build a simple ranking and recommendation system using lambda functions,
map(), filter(), and sorted() to analyze user preferences, calculate scores,
rank items, and generate recommendations.

This project introduces how functional programming concepts are used in
recommendation and ranking workflows.

Python Version:
3.13+

===============================================================================
"""


# =============================================================================
# Project Description
# =============================================================================

"""
Problem Statement:
------------------

A streaming platform wants to recommend content to users based on:

- User ratings
- Number of views
- Popularity score

The platform needs a simple ranking system that can:

- Calculate recommendation scores.
- Classify content popularity.
- Filter recommended items.
- Rank content from highest to lowest score.
- Generate a recommendation report.


Functional Requirements:
-----------------------

The program must:

1. Store content records.
2. Calculate recommendation scores using map().
3. Assign popularity categories.
4. Filter recommended content.
5. Sort content by recommendation score.
6. Display the final ranking report.


Prerequisites:
--------------

Learners should understand:

- Lambda functions
- map()
- filter()
- sorted()
- key parameter
- Lists
- Dictionaries


Constraints:
------------

Do not use:

- Import statements
- External libraries
- Classes
- File handling
- Machine learning libraries


Implementation Roadmap:
-----------------------

Step 1:
Create content data.

Step 2:
Calculate recommendation scores.

Step 3:
Classify popularity levels.

Step 4:
Filter recommended items.

Step 5:
Rank content.

Step 6:
Display recommendations.

===============================================================================
"""


# =============================================================================
# Content Dataset
# =============================================================================

content = [
    {
        "title": "Python Course",
        "rating": 4.8,
        "views": 50000,
        "likes": 9000
    },
    {
        "title": "AI Tutorial",
        "rating": 4.9,
        "views": 70000,
        "likes": 12000
    },
    {
        "title": "Web Development",
        "rating": 4.5,
        "views": 40000,
        "likes": 7000
    },
    {
        "title": "Data Science",
        "rating": 4.7,
        "views": 60000,
        "likes": 10000
    },
    {
        "title": "Cybersecurity",
        "rating": 4.6,
        "views": 30000,
        "likes": 5000
    }
]


# =============================================================================
# Step 1: Calculate Recommendation Score
# =============================================================================

content_with_score = list(
    map(
        lambda item: {
            **item,
            "score": (
                item["rating"] * 20
                +
                item["views"] / 1000
                +
                item["likes"] / 500
            )
        },
        content
    )
)


# =============================================================================
# Step 2: Add Popularity Category
# =============================================================================

categorized_content = list(
    map(
        lambda item: {
            **item,
            "category": (
                "Highly Recommended"
                if item["score"] >= 100
                else "Recommended"
                if item["score"] >= 80
                else "Average"
            )
        },
        content_with_score
    )
)


# =============================================================================
# Step 3: Filter Recommended Content
# =============================================================================

recommended_content = list(
    filter(
        lambda item: item["score"] >= 80,
        categorized_content
    )
)


# =============================================================================
# Step 4: Rank Content
# =============================================================================

ranked_content = sorted(
    recommended_content,
    key=lambda item: item["score"],
    reverse=True
)


# =============================================================================
# Recommendation Report
# =============================================================================

print("=" * 75)
print("CONTENT RECOMMENDATION REPORT")
print("=" * 75)

rank = 1

for item in ranked_content:
    print(
        f"Rank: {rank}\n"
        f"Title: {item['title']}\n"
        f"Rating: {item['rating']}\n"
        f"Views: {item['views']}\n"
        f"Likes: {item['likes']}\n"
        f"Recommendation Score: {item['score']:.2f}\n"
        f"Category: {item['category']}\n"
    )

    rank += 1


print("=" * 75)
print(f"Recommended Items: {len(recommended_content)}")
print("=" * 75)


"""
===============================================================================
Sample Input:
===============================================================================

{
    "title": "Python Course",
    "rating": 4.8,
    "views": 50000,
    "likes": 9000
}


===============================================================================
Sample Output:
===============================================================================

===========================================================================
CONTENT RECOMMENDATION REPORT
===========================================================================

Rank: 1
Title: AI Tutorial
Rating: 4.9
Views: 70000
Likes: 12000
Recommendation Score: 144.00
Category: Highly Recommended

Rank: 2
Title: Data Science
Rating: 4.7
Views: 60000
Likes: 10000
Recommendation Score: 134.00
Category: Highly Recommended

Rank: 3
Title: Python Course
Rating: 4.8
Views: 50000
Likes: 9000
Recommendation Score: 132.00
Category: Highly Recommended

Rank: 4
Title: Web Development
Rating: 4.5
Views: 40000
Likes: 7000
Recommendation Score: 109.00
Category: Highly Recommended

Rank: 5
Title: Cybersecurity
Rating: 4.6
Views: 30000
Likes: 5000
Recommendation Score: 98.00
Category: Recommended

===========================================================================
Recommended Items: 5
===========================================================================


===============================================================================
Detailed Explanation:
===============================================================================

This project simulates a simple recommendation workflow.

The first map() operation calculates a recommendation score using multiple
factors:

- User rating
- Views
- Likes


The second map() operation classifies content based on the calculated score.

The filter() function removes content that does not meet the recommendation
threshold.

The sorted() function ranks content using:

sorted(
    content,
    key=lambda item: item["score"],
    reverse=True
)


===============================================================================
Code Walkthrough:
===============================================================================

1. Content Dataset

Stores information about available content.

2. Score Calculation

map() transforms content records by adding scores.

3. Classification

lambda functions assign recommendation categories.

4. Filtering

filter() selects suitable recommendations.

5. Ranking

sorted() creates the final ranking list.


===============================================================================
Best Practices:
===============================================================================

- Use meaningful scoring formulas.
- Keep lambda expressions readable.
- Separate data processing stages.
- Use key functions for ranking.
- Validate data before processing.


===============================================================================
Common Mistakes:
===============================================================================

1. Creating unclear scoring formulas.

2. Sorting without using key.

3. Filtering before calculating required values.

4. Using lambda for complicated business logic.


===============================================================================
Possible Improvements:
===============================================================================

- Add user-specific recommendations.
- Add machine learning models.
- Store user history.
- Add feedback-based ranking.


===============================================================================
Bonus Challenges:
===============================================================================

1. Create different ranking formulas.

2. Add category-based recommendations.

3. Add user preference matching.

4. Create a recommendation score comparison.


===============================================================================
Real-World Applications:
===============================================================================

Similar concepts are used in:

- Video recommendation systems
- Online shopping platforms
- Search ranking systems
- Machine learning pipelines
- Content discovery platforms


===============================================================================
Key Learning Outcomes:
===============================================================================

After completing this project, learners should understand:

✓ Building ranking systems with sorted()
✓ Using lambda functions for scoring
✓ Filtering recommendations
✓ Transforming data with map()
✓ Applying functional programming concepts to AI-related workflows

===============================================================================
"""