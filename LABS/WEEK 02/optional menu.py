
def is_passing(score, threshold):
    return score >= threshold
def calculate_percentage(part, total):
    if total == 0:
        return 0
    return (part / total) * 100
choice = ""
while choice != "3":
    print("\n--- Menu ---")
    print("1. Check pass/fail")
    print("2. Calculate percentage")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        score = float(input("Enter score: "))
        threshold = float(input("Enter passing threshold: "))
        if is_passing(score, threshold):
            print("Result: Pass")
        else:
            print("Result: Fail")
    elif choice == "2":
        part = float(input("Enter achieved value: "))
        total = float(input("Enter total value: "))
        percentage = calculate_percentage(part, total)
        print(f"Percentage: {percentage:.2f}%")
    elif choice == "3":
        print("Exiting program...")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

