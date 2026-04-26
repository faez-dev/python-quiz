#python quiz

print("WELCOME to this simple EGC quiz")
score=0

QUESION=1
answer1=input("\n1.will the functions get better anytime soon:").strip() .lower()
if answer1=="qu estionable":
    print("you are goddam right!!")
    score+=1
else:
    print("WRONG,the answer is questionable")

QUESTION=2
answer2=input("\n2.will sir rashid ever take ICS again:").strip().lower()
if answer2=="never":
    print("you are goddam right!!")
    score+=1
else:
    print("delusion sy nikllo answer is HELLNO ")

QUESION=3
answer3=input("\n3.will the net worth of our boy moiz ever increase:").strip().lower()
if answer3=="inshallah!":
    print("you are goddam right!!")
    score+=1
else:
    print("get some help")

print("your score is {}/3".format(score))
if score==3:
    print("GREAT JOB")
elif score>=0:
    print("nice try and work harder")

    print("THANKS FOR ATTEMPTING THIS QUIZ")
