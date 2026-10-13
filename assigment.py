ticket = int(input("Enter the number of tickets:"))
student = input("Are you a student? (yes/no): ")
amount = float(input("Enter the amount of money you have: "))

if student == "yes" and ticket >= 8:
    price = 7
elif student == "yes" and ticket < 8: 
    price = 10
elif student == "no" and ticket >= 8:
    price = 10
else:
    price = 13

total_cost = ticket * price
print(f"Price per ticket: {price}")
print(f"Total cost: {total_cost}")

if amount > total_cost:
    left = amount - total_cost
    print(f" You will have {left} left.") 
elif amount == total_cost:
    print("Exactly enough money")
else:
    needed = abs(total_cost - amount)
    print(f"More money needed {needed}.")    

