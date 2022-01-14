import random
from time import sleep

errormessage = "Error! Probeer opnieuw a.u.b"

def uitleg():
    print("We zullen effe beginnen met het uitleggen hoe de regels werken.")
    sleep(2)
    print("Voordat het spel begint worden alle kaarten geschud en gegeven. De bovenste kaart op de stapel gelegd. Deze bovenste kaart die wordt getrokken heeft geen effect in het begin")
    sleep(4)
    print("In het begin van het spel krijgt iedereen 7 kaarten")
    sleep(2)
    print("Als u aan de beurt bent dan moet uw de positienummer van uw kaart benoemen (Waar de kaart van links naar rechts staat in uw deck)")
    sleep(4)
    print("Je hebt normale kaarten en speciale kaarten (We komen daar later op terug)")
    sleep(3)
    print("In totaal zijn er 108 kaarten in het spel op gebied van inhoud")
    sleep(2)
    print("Er zijn in totaal 4 kleuren: rood, blauw, geel en groen")
    sleep(3)
    print("Normale kaarten gaan van 0 tot 9. In totaal is dat 19 kaarten van elke kleur (1x een 0-kaart en 2x een 1 t/m 9 kaart)")
    sleep(5)
    print("Je kan alleen normale kaarten boven op elkaar gooien als de kleur of het nummer hetzelfde zijn")
    sleep(4)
    print("En nu de speciale kaarten")
    sleep(2)
    print(" - Neem-twee kaart - ")
    sleep(1)
    print("Als er een neem-twee kart op de stapel gegooid wordt dan moet een speler 2 kaarten erbij pakken.")
    sleep(4)
    print("Deze kaart kan alleen gespeeld worden wanneer op de stapel dezelfde kleur van de kaart ligt of een andere +2 of +4 kaart.")
    sleep(5)
    print("In totaal zijn er 8 kaarten hievan (2 kaarten van elke kleur)")
    sleep(3)
    print(" - Keer-om kaart - ")
    sleep(1)
    print("Wanneer er bijvoorbeeld linksom wordt gespeeld en je legt de kaart op de stapel dan draait de volgorde om en wordt er rechtsom gespeeld")
    sleep(4)
    print("Deze kaart kan alleen gespeeld worden wanneer er een dezelfde kleur op de stapel ligt of als er een andere keer-om kaart op de stapel ligt")
    sleep(5)
    print("In totaal zijn er 8 kaarten hievan (2 kaarten van elke kleur)")
    sleep(3)
    print(" - Sla-beurt-over kaart - ")
    sleep(1)
    print("Als er een sla-beurt-over kaart op de stapel gegooit wordt dan moet de speler na de speler die de kaart neerlegt een beurt overslaan.")
    sleep(5)
    print("Deze kaart kan alleen gespeeld worden wanneer er een dezelfde kleur op de stapel ligt of als er een andere sla-beurt-over kaart op de stapel ligt")
    sleep(5)
    print("In totaal zijn er 8 kaarten hievan (2 kaarten van elke kleur)")
    sleep(3)
    print(" - Keuzekaart - ")
    sleep(1)
    print("De speler die de kaart neerlegt mag een kleur kiezen waarin het spel verder gespeeld wordt")
    sleep(3)
    print("De speler mag ongeacht de kleur op de stapel de kaart spelen")
    sleep(3)
    print("In totaal zijn er 4 kaarten hievan (1 van elke kleur)")
    sleep(3)
    print(" - Neem-4 kaart - ")
    sleep(1)
    print("Als de speler deze kaart neerlegt dan moet de volgende speler 4 kaarten pakken en mag de speler die de kaarten heb gepakt de kleur kiezen")
    sleep(4)
    print("Deze kaart mag ongeacht de kleur of kaart gespeeld worden")
    sleep(3)
    print("In totaal zijn er 4 kaarten hievan (1 van elke kleur)")
    sleep(3)


def createCards():
    # belangrijke lists
    listColors = ['blauwe 0', 'rode 0', 'gele 0', 'groene 0']
    listSpecial = []
    # hulp materiaal
    colorsGiven = ['blauwe ', 'rode ', 'gele ', 'groene ']
    eightSpecial = ['neem-twee', 'keer-om', 'sla-beurt-over']
    fourSpecial = ['keuzekaart', 'neem-vier']
    # uitvoer opvulling lists
    for kleur in colorsGiven:
        for repeat in range(2):
            for nummers in range(1,10):
                listColors.append(str(kleur) + str(nummers))
    for kleur in colorsGiven:
        for repeat in range(2):
            for achteenheden in eightSpecial:
                listSpecial.append(str(kleur) + str(achteenheden))
        for viereenheden in fourSpecial:
            listSpecial.append(str(viereenheden))
    # combineer 2 lists en buiten de function sturen
    sortedCards = list(listColors) + list(listSpecial)
    return sortedCards


def randomizeCards(currentCardlist):
    # randomize de list en stop in nieuwe list
    randomizedCards = []
    randomizeProcess = False
    indexrange = 108
    while randomizeProcess == False:
        chosenCardNumber = random.randrange(0,int(indexrange))
        pickedCard = currentCardlist[chosenCardNumber]
        randomizedCards.append(pickedCard)
        del currentCardlist[chosenCardNumber]
        indexrange -= 1
        # indexrange check voor afbreken while loop
        if indexrange == 0:
            randomizeProcess = True
        else:
            None
    # voltooide resultaat terugsturen buiten de function
    return randomizedCards


def giveCards(playerammout):
    # deelt de top kaart uit aan iedereen 7 keer
    for cardrounds in range(7):
        for playercount in range(0,playerammout):
            currentcard = currentCardlist[0]
            del currentCardlist[0]
            playerlist[playercount].append(currentcard)
    # creërt een local variable voor de speelstapel en legt de eerste kaart op de speelstapel
    speelstapel = []
    currentcard = currentCardlist[0]
    del currentCardlist[0]
    speelstapel.append(currentcard)
    # return de huidige speelstapel buiten de function
    return speelstapel


def playableCard(checkingcard):
    cardColours = ['blauwe', 'rode', 'gele', 'groene']
    specialColoured = ['neem-twee', 'keer-om', 'sla-beurt-over']
    withoutColours = ['keuzekaart', 'neem-vier']
    canBePlayed = False
    # Kaart heeft een kleur?
    if canBePlayed == False:
        for colour in cardColours:
            if colour in checkingcard:
                if colour in topcard:
                    canBePlayed = True
    # De kaart heeft een waarschijnlijk een andere kleur dan de topkaart. Zijn de nummers gelijk aan de topkaart?
    elif canBePlayed == False:
        for number in range(0,10):
            if str(number) in checkingcard:
                if str(number) in topcard:
                    canBePlayed = True
    # De kaart heeft geen nummer? Is het een speciale kaart?
    elif canBePlayed == False:
        for specialColour in specialColoured:
            if specialColour in checkingcard:
                if specialColour in topcard:
                    canBePlayed == True
    # Het kan een kaart zonder kleur zijn?
    elif canBePlayed == False:
        for noColour in withoutColours:
            if noColour in checkingcard:
                canBePlayed = True
    # De kaart kan gewoon niet gespeeld worden en variable canBePlayed blijft False.
    else:
        None
    return canBePlayed


# --------------------------------------------------- Functions above --------------------------------------------------------------------------

print("Welkom bij Uno!")
startup = False
while startup == False:
    explain = input("Wilt u een uitleg van het spel? Antwoord met 'ja' of 'nee' (Aangeraden om te doen als je nog nooit dit programma heb gebruikt) ")
    if explain == "ja":
        uitleg()
        startup = True
    elif explain == "nee":
        startup = True
    else:
        print(errormessage)

setup = False
while setup == False:
    players = int(input("Hoeveel spelers wilt u dat er meedoen? (Geef een nummer op) "))
    if players > 1 and players < 9:
        setup = True
    elif players == 1:
        print("Te weinig spelers")
    elif players > 8:
        print("Te veel spelers")
    else:
        print(errormessage)

# aanmaken van lists gebaseerd op aantal spelers en dan alle individuele lijsten in 1 lijst stoppen tussen blokhaakjes
playerlist = [[] for i in range(players)]
# aanroepen function voor kaarten aanmaken eenmalig en het randomizen van de kaarten
sortedcardList = createCards()
currentCardlist = randomizeCards(sortedcardList)
# aanroepen function waar aan iedereen 7 kaarten wordt gegeven in het begin en de eerste kaart op de speelstapel legt. Deze eerste kaart heeft verder geen effect als het spel begint.
gespeeldekaarten = giveCards(players)
# belangrijke onderdelen voor het programma om functioneel te werken
currentplayer = 0
winnerknown = False
deckcount = 7
# ----------------------------------------------------- Setup installation above --------------------------------------------------------------------
while winnerknown == False:
    topcard = gespeeldekaarten[0]
    print("Huidige kaart boven op de speelstapel:", topcard)

    if currentplayer == 0:
        print("Uw deck:", playerlist[0])
        chosencardposition = int(input("Welke kaart wilt u spelen? "))
        if chosencardposition > 0 and chosencardposition <= deckcount:
            chosencardposition -= 1
            chosencard = playerlist[0][chosencardposition]
            playablecardstatus = playableCard(chosencard)
            print(playablecardstatus)
        else:
            print(errormessage)
    else:
        ...
