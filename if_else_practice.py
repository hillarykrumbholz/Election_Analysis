temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#What is the score?
score = int(input("What is your test score? "))

#Determine the grade.
if score >= 90:
    print("Your grade is an A.")
else:
    if score >= 80:
        print("Youre score is a B.")
    else:
        if score >= 70:
            print("Your score is a 70.")
        else:
            if score >= 60:
                print("Your score is a D.")
            else:
                print("Your grade is an F.")


