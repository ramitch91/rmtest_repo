print("-------------------")
print("   Odd or Even")
print("-------------------")
print()

number = 1

while number:
    number = int(input("Please enter a number or 0 to quit: "))
    if number == 0:
        break
    elif number % 2 == 0:
        print(f"The number you entered {number} is EVEN.")
    else:
        print(f"The number you entered {number} is ODD.")

print()
print("Thank you for playing, goodbye!")
print()
