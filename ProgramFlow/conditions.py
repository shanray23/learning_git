age = int(input("How old are you ? "))

#if age >= 16 and age <= 65:
if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy free time")
else:
    print("Have a good day at work")
