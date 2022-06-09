
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

    question_2=input("""Do you like the mountains?
            yes
            no
            >""")
    if question_2=="yes":
        Alaska+=1
        break
    if question_2=="yes":
        Cabo+=1
        break
    if question_2=="no":
        Bahamas+=1
        break
    else:
        print("that wasn't a choice")

    question_3=input("""Do you want lots of people?
            yes
            no
            >""")
    if question_3=="yes":
        Alaska+=0
        break
    if question_3=="yes":
        Cabo+=1
        break
    if question_3=="no":
        Bahamas+=0
        break
    else:
        print("that wasn't a choice")

    question_4=input("""Do you like the sand?
            yes
            no
            >""")
    if question_4=="yes":
        Alaska+=0
        break
    if question_4=="yes":
        Cabo+=1
        break
    if question_4=="no":
        Bahamas+=1
        break
    else:
        print("that wasn't a choice")

    destinations = {'Alaska': A, 'Bahamas': B, 'Cabo': C}

    winner = max(destinations, key=destinations.get)
print(winner, 'enjoy your vacation, nerd!')
