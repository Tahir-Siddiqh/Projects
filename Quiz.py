print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's start")

point = 0

answer = input("What does RAM mean? ")
if answer == "Random Access Memory":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("What does ROM mean? ")
if answer == "Read Only Memory":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("What does SSD mean? ")
if answer == "Solid State Drive":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("What does CPU mean? ")
if answer == "Central Processing Unit":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("Is Keyboard Input or Output? ")
if answer == "Input":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

answer = input("Is Printer Input or Output? ")
if answer == "Output":
    print("Correct!")
    point += 1
else:
    print("Incorrect!")

print("You got "+str(point)+" questions correct")
print("You got "+str((point/6)*100)+" questions correct")
