# Student Grade Calculator

## Project Overview

The Student Grade Calculator is a Python console application developed as part of Week 2 of the Python Programming assignment.

The program accepts a student's name and marks, validates the entered marks, calculates the appropriate grade using predefined grading rules, and displays an encouraging feedback message.

This project demonstrates fundamental Python concepts including:

* Conditional Statements (if-elif-else)
* Functions
* While Loops
* Input Validation
* Exception Handling
* User Input and Output

---

## Objectives

* Understand decision-making using conditional statements.
* Practice implementing grading logic.
* Learn input validation techniques.
* Create reusable functions.
* Handle invalid user inputs using exception handling.
* Develop a simple real-world application.

---

## Technologies Used

* Python 3.x
* Visual Studio Code (or any Python IDE)
* Git & GitHub

---

## Features

* Accepts student name and marks.
* Validates marks between 0 and 100.
* Prevents invalid or non-numeric inputs.
* Calculates grades automatically.
* Displays encouraging feedback messages.
* Uses functions for modular programming.
* Generates a formatted result card.

---

## Grading Logic

| Marks Range | Grade |
| ----------- | ----- |
| 90 - 100    | A     |
| 80 - 89     | B     |
| 70 - 79     | C     |
| 60 - 69     | D     |
| 0 - 59      | F     |

### Feedback Messages

| Grade | Feedback Message                               |
| ----- | ---------------------------------------------- |
| A     | Excellent Work! Keep Shining! 🌟               |
| B     | Very Good! Keep It Up! 👍                      |
| C     | Good Job! You Can Do Even Better! 😊           |
| D     | Keep Practicing and Improving! 📚              |
| F     | Don't Give Up! Success Comes With Practice! 💪 |

---

## Project Structure

```text
Student-Grade-Calculator/
│
├── README.md
├── grade_calculator.py
├── test_cases.txt
└── screenshots/
    └── output.png
```

---

## Setup Instructions

### Prerequisites

* Python 3.x installed on your computer.

### Installation

1. Clone the repository:

```bash
https://github.com/ramyajyothi-bammidi/Student-Grade-Calculator
```


2. Open the project folder:

```bash
cd Student-Grade-Calculator
```

3. Run the application:

```bash
python grade_calculator.py
```

---

## Code Structure

### Function Used

```python
calculate_grade(marks)
```

### Purpose

The function:

* Receives marks as input.
* Determines the appropriate grade.
* Returns both the grade and feedback message.

### Main Components

1. Student name input
2. Marks input
3. Input validation using while loop
4. Grade calculation using function
5. Result card generation

---

## Technical Details

### Algorithm

1. Display the application title.
2. Accept the student's name.
3. Accept marks from the user.
4. Validate that marks are between 0 and 100.
5. Handle invalid inputs using try-except.
6. Call the grading function.
7. Determine grade and feedback.
8. Display the result card.
9. End the program.

### Concepts Used

* Variables
* Functions
* Conditional Statements
* While Loops
* Exception Handling
* User Input & Output

### Program Flow

```text
User Input
     ↓
Input Validation
     ↓
calculate_grade()
     ↓
Grade Determination
     ↓
Feedback Generation
     ↓
Result Card Display
```

---

## Sample Output

```text
========================================
      STUDENT GRADE CALCULATOR
========================================
Enter Student Name: Priya
Enter Marks (0-100): 92

========================================
           RESULT CARD
========================================
Student Name : Priya
Marks        : 92/100
Grade        : A
Feedback     : Excellent Work! Keep Shining! 🌟
========================================
```

---

## Testing Evidence

| Test Case | Input | Expected Output       |
| --------- | ----- | --------------------- |
| 1         | 95    | Grade A               |
| 2         | 85    | Grade B               |
| 3         | 75    | Grade C               |
| 4         | 65    | Grade D               |
| 5         | 45    | Grade F               |
| 6         | 105   | Invalid Marks Message |
| 7         | -10   | Invalid Marks Message |
| 8         | abc   | Invalid Input Message |

---

## Screenshots

screenshots/input_validation.png



## Documentation Link

Google Docs Documentation:

```text
[PASTE YOUR GOOGLE DOCS LINK HERE]
```

---

## Learning Outcomes

Through this project, I learned:

* Decision-making using if-elif-else statements.
* Creating reusable functions.
* Using loops for validation.
* Handling errors with try-except.
* Building a complete Python console application.
* Managing projects using GitHub.

---

## Author

Name: [YOUR NAME]

Course: Python Programming

Assignment: Week 2 – Student Grade Calculator

GitHub Repository: [YOUR GITHUB REPOSITORY LINK]
