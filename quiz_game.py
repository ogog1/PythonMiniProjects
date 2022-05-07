print("Hi! Welcome to my quiz!")

playing = input("Want to take the quiz? (Y/N) ")

if "y" in playing[0] or "Y" in playing[0]:
    print("Let's play")
else:
    print("Maybe later...")
    quit()

score = 0


Question1 = "What element does O represent on the periodic table? "
answer1 = input(Question1)

    if answer1 == "oxygen" or answer1 == "Oxygen" or answer1 == "OXYGEN":
        score = score + 1
        print(f"That's correct! Your score is {score}/10.")
    else:
        print(f"Sorry,that's not correct... Your score is {score}/10.")
        again = input("Want to try again?")
        if "n" in again[0] or "N" in again[0]:


