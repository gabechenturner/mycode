
#use the code to guess your ideal vacation spot
Alaska=0
Bahamas=0
Cabo=0

while True:

    question_1=input("""What temperature do you want?
            hot 
            cold 
            wild
            >""")
    if question_1=="hot":
        Bahamas+=1
        break 
    elif question_1=="cold":
        Alaska+=1
        break    
    elif question_1=="wild":
        Cabo+=1
        break
    else:
        print("that wasn't a choice")

while True:

    question_2=input("""Do you like the mountains?
            yes
            no
            >""")
    if question_2=="yes":
        Alaska+=1
        Cabo+=1
        break  
    elif question_2=="no":
        Bahamas+=1
        break
    else:
        print("that wasn't a choice")
        break

while True:
    question_3=input("""Do you want lots of people?
            yes
            no
            >""")

    if question_3=="yes":
        Cabo+=1
        break
    elif question_3=="no":
        Bahamas+=1
        Alaska+=1
    else:
        print("that wasn't a choice")

while True:
    question_4=input("""Do you like the sand?
            yes
            no
            >""")
    if question_4=="yes":
        Cabo+=1
        Bahamas+=1
    elif question_4=="no":
        Alaska+=1
        break
    else:
        print("that wasn't a choice")


