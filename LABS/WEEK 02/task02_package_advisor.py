usage = float(input("Enter data usage in GB: "))
if usage < 0:
    print("Invalid — usage cannot be negative")
elif 0 <= usage <= 5:
    print("Recommended Package: Basic")
elif 5 < usage <= 15:
    print("Recommended Package: Standard")
else:
    print("Recommended Package: Premium")
