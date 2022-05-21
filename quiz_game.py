print("Hi! Welcome to my quiz!")

playing = input("Want to take the quiz? (Y/N) ")

if "y" in playing[0] or "Y" in playing[0]:
    print("Let's play")
else:
    print("Maybe later...")
    quit()

score = 0

while True:
    Question1 = "What element does O represent on the periodic table? "
    answer1 = input(Question1).lower()

    if answer1 == "oxygen":
        score = score + 1
        print(f"That's correct! Your score is {score}/5.")
        break
    else:
        print(f"Sorry,that's not correct... Your score is {score}/5.")
        again = input("Want to try again? ")
        if "y" in again[0] or "Y" in again[0]:
            True
        else:
            print("Next question!")
            break
while True:
    Question2 = "How many makes up a baker's dozen? "
    answer2 = input(Question2)

    if answer2 == "13":
        score = score + 1
        print(f"That's correct! Your score is {score}/5.")
        break
    else:
        print(f"Sorry,that's not correct... Your score is {score}/5.")
        again = input("Want to try again? ")
        if "y" in again[0] or "Y" in again[0]:
            True
        else:
            print("Next question!")
            break

while True:
    Question3 = "What's the capital of Spain? "
    answer3 = input(Question3).lower()

    if answer3 == "madrid":
        score = score + 1
        print(f"That's correct! Your score is {score}/5.")
        break
    else:
        print(f"Sorry,that's not correct... Your score is {score}/5.")
        again = input("Want to try again? ")
        if "y" in again[0] or "Y" in again[0]:
            True
        else:
            print("Next question!")
            break

while True:
    Question4 = "Which fictional city is the home of Batman? "
    answer4 = input(Question4).lower()

    if "gotham" in answer4:
        score = score + 1
        print(f"That's correct! Your score is {score}/5.")
        break
    else:
        print(f"Sorry,that's not correct... Your score is {score}/5.")
        again = input("Want to try again? ")
        if "y" in again[0] or "Y" in again[0]:
            True
        else:
            print("Next question!")
            break

while True:
    Question5 = "What color is the circle on the Japanese national flag? "
    answer5 = input(Question5).lower()

    if answer5 == "red":
        score = score + 1
        print(f"That's correct! Your score is {score}/5.")
        break
    else:
        print(f"Sorry,that's not correct... Your score is {score}/5.")
        again = input("Want to try again? ")
        if "y" in again[0] or "Y" in again[0]:
            True
    break

print("\nResults:")
if score == 5:
    print("Congratulations! You got every question right!")
    print(f"Total Score: {score}/5")
else:
    print("Try a little better next time...")
    print(f"Total Score: {score}/5")

print("Thank you for playing!")