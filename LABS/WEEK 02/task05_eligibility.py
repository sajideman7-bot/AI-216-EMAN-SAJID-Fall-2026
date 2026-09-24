age = 19
programming_score = 72
prerequisite_completed = True

print("--- Applicant Eligibility ---")

if age >= 18 and programming_score >= 60 and prerequisite_completed:
    print("Eligible")
else:
    print("Not eligible")

    if age < 18:
        print("- Age requirement not met")

    if programming_score < 60:
        print("- Programming score requirement not met")

    if not prerequisite_completed:
        print("- Prerequisite course not completed")
