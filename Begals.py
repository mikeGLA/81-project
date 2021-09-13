#Begals
import random

answer = random.randint(000,999)

#Create anscheck function
def answerCheck(guessNum):
    for guessNum in answer:
        if guessNum == answer:
            print("Begals")
            break
        elif guessNum != answer:
            print("Yedmae")
        else:
            print("Fermi")
    return

#Create tries count
def guessCount(count):
    for i in range(10):
        print("Try number: ", count, "You can guess only 10 times.")

#test
guessNum = int(input("Enter your guess: "))

Checking = answerCheck(guessNum)

print("Your answer check is: ", Checking)
dasfadfafdfsdfasdfdasfasdfasdcvzvxcadfadfdfasdfdfsdfasdfefafasdf
dfadfadsfdasfacvzcdaf