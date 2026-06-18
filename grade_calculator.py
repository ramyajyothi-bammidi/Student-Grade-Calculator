
def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent Work! Keep Shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep It Up! 👍"
    elif marks >= 70:
        return "C", "Good Job! You Can Do Even Better! 😊"
    elif marks >= 60:
        return "D", "Keep Practicing and Improving! 📚"
    else:
        return "F", "Don't Give Up! Success Comes With Practice! 💪"


print("=" * 40)
print("      STUDENT GRADE CALCULATOR")
print("=" * 40)

name = input("Enter Student Name: ")

while True:
    try:
        marks = int(input("Enter Marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100. Try again.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

grade, message = calculate_grade(marks)

print("\n" + "=" * 40)
print("           RESULT CARD")
print("=" * 40)
print(f"Student Name : {name}")
print(f"Marks        : {marks}/100")
print(f"Grade        : {grade}")
print(f"Feedback     : {message}")
print("=" * 40)

