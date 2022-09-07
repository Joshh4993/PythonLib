import sys
import random
import json

ans = True

startnum_file = open('settings.json')
json_array = json.load(startnum_file)
lownum = int(json_array[0])
highnum = int(json_array[1])
startnum = random.randint(lownum, highnum)
previous_num = 0

def newround(previous_num):
    previous_num = previous_num
    while ans:
        print("The previous number was: '" + str(previous_num) + "' is the next number- higher(h), lower(l) or the same(s)?")
        nextnum = random.randint(1, 1000)
        player_input = input("Type your answer: ")
        if (player_input == " "): sys.exit()
    
        if (player_input == "h"):
            if(nextnum > previous_num):
                print("Correct! The number was: " + str(nextnum) + " Starting new round.\n\n\n")
                previous_num = nextnum
                newround(previous_num)
        elif (player_input == "l"):
            if(nextnum < previous_num):
                print("Correct! The number was: " + str(nextnum) + " Starting new round.\n\n\n")
                previous_num = nextnum
                newround(previous_num)
        elif (player_input == "s"):
            if(nextnum == previous_num):
                print("Correct! The number was: " + str(nextnum) + " Starting new round.\n\n\n")
                previous_num = nextnum
                newround(previous_num)
        else:
            print("Uh oh! You did not get it right! The number was: " + str(nextnum))
            sys.exit()

while ans:
    print("The starting number is: '" + str(startnum) + "' is the next number- higher(h), lower(l) or the same(s)?")
    nextnum = random.randint(1, 1000)
    player_input = input("Type your answer: ")
    if (player_input == " "): sys.exit()
    
    if (player_input == "h"):
        if(nextnum > startnum):
            print("Correct! The number was: " + str(nextnum) + " Starting new round.\n\n\n")
            previous_num = nextnum
            newround(previous_num)
    elif (player_input == "l"):
        if(nextnum < startnum):
            print("Correct! The number was: " + str(nextnum) + " Starting new round.\n\n\n")
            previous_num = nextnum
            newround(previous_num)
    elif (player_input == "s"):
        if(nextnum == startnum):
            print("Correct! The number was: " + str(nextnum) + " Starting new round.\n\n\n")
            previous_num = nextnum
            newround(previous_num)
    else:
        print("Uh oh! You did not get it right! The number was: " + str(nextnum))
        sys.exit()

