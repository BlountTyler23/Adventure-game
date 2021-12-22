import random
points = 250

h = int(input("How is your huberis?\n0-100\n>"))
if h > 100 or h < 0 or h > points:
    print("Can you not count get out of here")
    exit()
points = points - h
print("Even the god's are terrifed of your Huberis. Huberis set to " + str(h))
print("You have " + str(points) + " skill points remaining")

s = int(input("How strong are you boi\n0-100\n>"))
if s > 100 or s < 0 or s > points:
    print("Can you not count get out of here")
    exit()
points = points - s
print("Wow so strong Strength set to " + str(s))
print("You have " + str(points) + " skill points remaining")

c = int(input("How is your speechcraft?\n0-100\n>"))
if c > 100 or c < 0 or c > points:
    print("Can you not count get out of here")
    exit()
points = points - c
print("Wow so talkitive. Charisma set to " + str(c))
print("You have " + str(points) + " skill points remaining")

f = int(input("How is your farming skill?\n0-100\n>"))
if f > 100 or f < 0 or f > points:
    print("Can you not count get out of here")
    exit()
points = points - f
print("Wow you can realy farm. Farming set to " + str(f))
print("You have " + str(points) + " skill points remaining")

m = int(input("How is your skill with magic?\n0-100\n>"))
if m > 100 or m < 0 or m > points:
    print("Can you not count get out of here")
    exit()
points = points - m
print("Wow you have really harnessed the powers of magic. Magic set to " + str(m))
print("You have " + str(points) + " skill points remaining")


print("Your a lonely peasent man")
start = input("What is your job, \n1. Corn Farmer \n2. Local Levy \n3. Miner \n>")

if start.lower() == "2":
    roll = random.randrange(0, s)
    roll2 = random.randrange(0, h)
    if roll > 75 and roll2 < 15:
            print("Your kingdom of West Virginia goes to war with North Virginia. In your first battle, well clashing with a Northern he slices your leg off. You return home back to a life of corn farming")
    else:
        print("Your kingdom of West Virginia goes to war with North Virginia. Your King John Denver asks for you to go to war, in your first battle you die to a spiked arrow")
        exit()
if start.lower() == "1":
    roll = random.randrange(0, f)
    if roll > 20:
        print("You plow your fields one day and find the burried sword of Sting")

    else:
        print("Well plowing field your plow hit a metal object in the ground lunching you over your plow landing over the cliff near by.")
        exit()
    second = input("After finding the lengdary sword of Sting, what would you like to join King John Denver's war against North Virginia or rally the peasentry to overthrow the corrupt king? (To War/Rally the people)\n>")
    if second.lower() == "to war":
        print("You come to the king's aid. Out of greed, the king has you killed and steals the lengdary sword.")
    if second.lower() == "rally the people":
        print("You sneak into the capitial and stand before a group of people. You yell out by the gods our king is to corrupt lead the people of the lower class and the people in general. Rally behind me and behind this sword. as you stick Sting skywarrd.")

if start.lower() == "3": 
    roll = random.randrange(0, s) 
    if roll > 10:
        print("well slaving away in the mines. you strike a hard rock boucing the pic back into your face. The foreman declares you legally dumb and sends you home to farm corn")

    else:
        print("well slaving away in the mines. you strike a hard rock boucing the pic back into your face rendring your self unconscious falling straight off a cliff.")
        exit()