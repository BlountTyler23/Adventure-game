import random
points = 250

print("You have 250 points to allocate to five different skills")

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
    
if start.lower() == "3": 
    roll = random.randrange(0, s) 
    if roll > 10:
        print("well slaving away in the mines. you strike a hard rock boucing the picaxe back into your face. The foreman declares you legally dumb and sends you home to farm corn")

    else:
        print("well slaving away in the mines. you strike a hard rock boucing the picaxe back into your face rendring your self unconscious falling straight off a cliff.")
        exit()
roll = random.randrange(0, f)
if roll > 20:
        print("You plow your fields one day and find the burried sword of Sting")
second = input("After finding the lengdary sword of Sting, what would you like to?\n 1. Join King John Denver's war against North Virginia\n 2. Rally the peasentry to overthrow the corrupt king?\n 3. Betray your people and join the Northerns\n>")
if second.lower() == "1":
        print("You come to the king's aid.")
        roll = random.randrange(0, c) 
        roll2 = random.randrange(0, h)
        if roll > 40 and roll2 < 10:
            print("You over come the kings evil greed he allows you to join the army as a captian")

        else:
            print("Out of greed, the king has you killed and steals the lengdary sword.")
            exit()

if second.lower() == "2":
        print("You sneak into the capitial and stand before a group of people. You yell out by the gods our king is to corrupt to lead the people of the lower class and the people in general. Rally behind me and behind this sword. As you stick Sting skywarrd.")
        roll = random.randrange(0, c)
        roll2 = random.randrange(0, h)
        if roll > 75 and roll2 < 5:
            print("The people rally behind you weapons in hand. Joined by many gaurds you over power the capital's loyalist.")
        else:
            print("Not swayed, the people boo. Quickly the guards arrest you. Ater three years in the dungeon you are beheaded")
            exit()

if second.lower() == "3":
        print("You try to make you across the magical echanted boarder.")
        roll = random.randrange(0, s)
        roll2 = random.randrange(0, m)
        roll2 = random.randrange(0, c)
        if roll > 85 and roll2 > 90 and roll3 > 30:
            print("You use disenchant spell dispelling the border wall and flee to the Northerns. The Northerns catch you but notice your carrying the lengdary sword, using quick words you meet with their king who allows you lead troops into the up coming battle.")
        
        else:
            print("You run head long into the border hoping that your disenchant spell worked. Unfortunately you realize to late it failed. Runing into the shieled you're vaporized.")
            exit()