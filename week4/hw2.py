personal_income = int(input("What is your personal income?"))
credit_score = int(input("What is your credit score?"))

if personal_income > 100000:
    print("You are eligible for a loan with the lowest interest rates.")
elif personal_income > 50000:
    if credit_score > 700:
        print("You are eligible for a loan with low interest rates.")
elif personal_income > 30000:
    if credit_score > 500:
        print("You are eligible for a loan with moderate interest rates.")
    elif credit_score < 500:
        print("Sorry, you are not eligible for a loan at this time.")
else:
    print("Sorry, you are not eligible for a loan at this time.")
print()