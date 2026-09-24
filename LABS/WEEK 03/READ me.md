### Variable Scope TASK 2
The two values are different because the `score` variable inside the function is a separate **local variable** from the `score` variable outside the function.
* **Local variable:** `score = 70` — it is created inside `show_score()` and can only be used inside that function.
* **Global variable:** `score = 90` — it is created outside the function and can be accessed from outside the function.
Therefore, the output is:

text
Inside function: 70
Outside function: 90
### What is the purpose of `if __name__ == "__main__":`?

It makes sure that the code inside it runs only when the Python file is run directly. If the file is imported into another Python file, the code inside the main guard will not run.
Example is 
If you run score_utils.py directly → the demo code runs.
If you import score_utils.py into main.py → the demo code does not run.

