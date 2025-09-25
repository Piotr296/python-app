import random

def division_quiz():
    print("Welcome to Division Practice! Test 1")
    score = 0
    
    while True:
        # make sure denominator is not zero
        a = random.randint(1, 100)
        b = random.randint(1, 10)  

        correct_answer = round(a / b, 2)  # round to 2 decimals
        print(f"\nWhat is {a} ÷ {b}? (Round to 2 decimals)")

        user_input = input("Your answer (or 'q' to quit): ")
        if user_input.lower() == "q":
            print(f"Final score: {score}")
            break

        try:
            user_answer = float(user_input)
        except ValueError:
            print("Please enter a number.")
            continue

        if abs(user_answer - correct_answer) < 0.01:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The right answer was {correct_answer}.")

if __name__ == "__main__":
    division_quiz()
