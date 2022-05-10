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
    answer1 = input(Question1)

    if answer1 == "oxygen" or answer1 == "Oxygen" or answer1 == "OXYGEN":
        score = score + 1
        print(f"That's correct! Your score is {score}/10.")
        break
    else:
        print(f"Sorry,that's not correct... Your score is {score}/10.")
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
        print(f"That's correct! Your score is {score}/10.")
        break
    else:
        print(f"Sorry,that's not correct... Your score is {score}/10.")
        again = input("Want to try again? ")
        if "y" in again[0] or "Y" in again[0]:
            True
        else:
            print("Next question!")
            break

while True:
    Question3 = "What's the capital of Spain? "
    answer3 = input(Question3)

    if answer3 == "madrid" or answer3 == "Madrid" or answer3 == "MADRID":
        score = score + 1
        print(f"That's correct! Your score is {score}/10.")
        break
    else:
        print(f"Sorry,that's not correct... Your score is {score}/10.")
        again = input("Want to try again? ")
        if "y" in again[0] or "Y" in again[0]:
            True
        else:
            print("Next question!")
            break