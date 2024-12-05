print("Welcome to my computer quiz")
playing = input("do you want to play? ")
if playing.lower() != "yes":
    quit()

print("okay! let's play.... :)")

score= 0
answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Sorry, you're wrong!")


answer = input("What does RAM stand for? ")
if answer.lower() == "ramdom access memory":
    print("Correct!")   
    score +=1

answer = input("What does RAM stand for? ")
if answer.lower() == "ramdom access memory":
    print("Correct!")   
    score +=1










else:
    print("Sorry, you're wrong!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score +=1

else:
    print("Sorry, you're wrong!")


print("You got "+ str(score)+ "questions correct!")

print("You got "+ str((score/3)*100)+ "%")