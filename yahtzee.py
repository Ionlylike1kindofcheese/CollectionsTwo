import random

def firstdobbelwerp():
    dobbelstenen = []
    for x in range(5):
        currentdobbel = random.randrange(1,7)
        dobbelstenen.append(currentdobbel)
    return dobbelstenen


def rerollingnumbers(rerollpositions, previouslist):
    for z in rerollpositions:
        currentreroll = random.randrange(1,7)
        z -= 1
        previouslist[z] = currentreroll
    return previouslist


def calculatelowernumbercount(checkinglist):
    for c in range(1,7):
        numberCount = 0
        for b in range(5):
            if checkinglist[b] == c:
                numberCount += 1
            else:
                None
        if numberCount >= 3:
            valueogen = c
            return numberCount, valueogen


def calculatelowerstraight(checkinglist):
    followupcount = 0
    for d in range(1,7):
        print("D =", d)
        securitylayer = 0
        for e in range(5):
            if securitylayer >= 2:
                break
            elif checkinglist[e] == d:
                followupcount += 1
                securitylayer += 1
            else:
                None
        if securitylayer == 0:
            print("proceed")
            followupcount = 0
    return followupcount
        
                

totaalpunten = 0
# cheats
dobbelstenenlist = [6, 1, 3, 4, 5]
# cheats

# turn off if cheat enabled
# dobbelstenenlist = firstdobbelwerp()
# turn off if cheat enabled
werpcompletion = False
rerollpogingen = 2
while werpcompletion == False:
    if rerollpogingen == 0:
        print("Uw dobbelstenen =", dobbelstenenlist)
        werpcompletion = True
    else:
        print("Uw dobbelstenen =", dobbelstenenlist)
        OpzijOfRollen = input("Wilt u bepaalde dobbelstenen opnieuw rollen? (Antwoord met ja of nee) ")
        if OpzijOfRollen == "ja":
            rerollpogingen -= 1
            freezecurrentnumbers = False
            while freezecurrentnumbers == False:
                rerolls = []
                rerollposition = input("Welke dobbelstenen wilt u opnieuw gooien? (Schrijf de bepaalde dobbelstenen als nummers aan elkaar) ")
                for x in rerollposition:
                    x = int(x)
                    rerolls.append(x)
                freezecurrentnumbers = True
                dobbelstenenlist = rerollingnumbers(rerolls, dobbelstenenlist)
        elif OpzijOfRollen == "nee":
            werpcompletion = True
        else:
            None


punten = 0

straightcountresult = calculatelowerstraight(dobbelstenenlist)
if straightcountresult == 4:
    print("Small straight!!!")
    punten += 30
    print(punten)
elif straightcountresult == 5:
    print("Large straight!!!")
    punten += 40
    print(punten)

# numbercountresult, valueogen = calculatelowernumbercount(dobbelstenenlist)
# if numbercountresult == 3:
#     print("Three of a kind!!!")
#     punten = punten + (3 * valueogen)
#     print(punten)
# elif numbercountresult == 4:
#     print("Four of a kind!!!")
#     punten = punten = (4 * valueogen)
#     print(punten)
# elif numbercountresult == 5:
#     print("Yahtzee!!!")
#     punten += 50
#     print(punten)
# else: 
#     None

