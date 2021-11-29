boodschappenlijst = {}

completion = False

print("A.U.B typ alles in kleine letters.")
print()

def addAndcheck(givenboodschap, givenhoeveelheid):
    if givenboodschap in boodschappenlijst:
        boodschappenlijst[givenboodschap] += givenhoeveelheid
    else:
        boodschappenlijst[str(givenboodschap)] = int(givenhoeveelheid)

while completion == False:
    boodschap = str(input("Wat wilt u aan de boodschappenlijst toevoegen? "))
    currentboodschap = boodschap
    hoeveelheid = int(input("Hoeveel wilt u van dit product? (Ingevuld product: " + str(currentboodschap) + ") "))
    currenthoeveelheid = hoeveelheid
    addAndcheck(currentboodschap, currenthoeveelheid)
    anwsered = False
    while anwsered == False:
        askCompletion = input("Wilt u nog meer toevoegen? (antwoord met ja of nee) ")
        if askCompletion == "ja":
            anwsered = True
        elif askCompletion == "nee":
            completion = True
            anwsered = True
        else:
            None

if completion == True:
    print(boodschappenlijst)
