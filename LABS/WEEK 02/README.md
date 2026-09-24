````markdown
# Lab 02 — Python Fundamentals for Problem Solving

## Concepts Practiced
- Variables and data types
- Operators
- Conditionals
- Loops
- Functions

## Tasks Completed
1. Daily Expense Tracker
2. Internet Package Advisor
3. Temperature Monitoring
4. Model Score Analysis
5. Applicant Eligibility
6. Functions
7. Problem Decomposition Challenge

## Boundary / Test Cases

### Task 2 — Internet Package Advisor

| Input (GB) | Result |
|---:|---|
| 0 | Basic |
| 5 | Basic |
| 5.1 | Standard |
| 15 | Standard |
| 15.1 | Premium |
| -1 | Invalid — usage cannot be negative |

### Task 3 — Temperature Monitoring

The boundary values `15.0°C` and `30.0°C` were tested and both were classified as **Normal**.

Expected summary for the original readings:

```text
Below Normal: 1
Normal: 4
High: 2
````

### Task 4 — Model Score Analysis

The original scores produced:

```text
Meeting target (>= 0.85): 3
Below target: 4
Average score: 0.81
Percentage meeting target: 42.86%
```

An empty list was also tested and the program displayed a clear message instead of causing a division-by-zero error.

### Task 5 — Applicant Eligibility

| Applicant | Age | Programming Score | Prerequisite | Result                                        |
| --------- | --: | ----------------: | ------------ | --------------------------------------------- |
| 1         |  19 |                72 | True         | Eligible                                      |
| 2         |  18 |                60 | True         | Eligible                                      |
| 3         |  17 |                55 | False        | Not eligible — all three requirements not met |

## What I Found Difficult
* Understanding how to use conditions correctly, especially boundary values.
* Using loops and counters to process multiple values.
* Understanding how functions can make repeated logic reusable.
## What I Learned
* How to use `if`, `elif`, and `else` for decision making.
* How to use `for` and `while` loops.
* How to work with lists and counters.
* How to create functions using parameters and return values.
* How to test programs using boundary and edge cases.
## AI Engineering Relevance
### Data Processing
Loops, conditions, and functions can be used to process and organize data before it is used by an AI model.
### Validation
Conditional logic can check whether input data is valid before processing it.
### Model Evaluation
Thresholds, averages, counts, and percentages can be used to evaluate model scores and performance.
### AI Application Code
Functions and conditionals are commonly used to build reusable logic inside AI applications, data-processing pipelines, and decision-making systems.
