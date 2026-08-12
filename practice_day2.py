# Day 2: User Input, Type Casting, and Conditionals

# Default name variable
user_name = "Sownak"

print(f"=== Welcome {user_name} to Day 2 Practice ===")

# 1. Age Verification
age = int(input(f"Hello {user_name}, enter your age: "))

if age >= 18:
    print(f"Great, {user_name}! You are eligible for full access.")
else:
    print(f"Hey {user_name}, you are under 18.")

# 2. Simple Bill Splitter 
print(f"\n--- {user_name}'s Bill Calculator ---")
total_bill = float(input("Enter total bill amount: "))
people = int(input("How many people: "))

per_person = total_bill / people
print(f"Hey {user_name}, each person has to pay: {per_person:.2f}")