# input:
#processing:
#output:
food = float(input("Enter food expense: "))
transport = float(input("Enter transport expense: "))
other = float(input("Enter other expense: "))
budget = float(input("Enter daily budget: "))

total_expense = food + transport + other
remaining_budget = budget - total_expense

print("\n--- Daily Expense Report ---")
print("Total Expense:", total_expense)
print("Remaining Budget:", remaining_budget)

if total_expense < budget:
    print("Status: Within budget")
elif total_expense == budget:
    print("Status: Exactly at budget")
else:
    print("Status: Over budget")

