
daily_usage_kwh = [3.2, 5.0, 7.5, 10.0, 12.4, 4.9, 10.1]
low = 0
normal = 0
high = 0
for usage in daily_usage_kwh:
    if usage < 5:
        low += 1
    elif 5 <= usage <= 10:
        normal += 1
    else:
        high += 1
total = len(daily_usage_kwh)
low_percentage = (low / total) * 100
normal_percentage = (normal / total) * 100
high_percentage = (high / total) * 100
print("Electricity Usage Summary")
print(f"Low: {low} ({low_percentage:.2f}%)")
print(f"Normal: {normal} ({normal_percentage:.2f}%)")
print(f"High: {high} ({high_percentage:.2f}%)")
