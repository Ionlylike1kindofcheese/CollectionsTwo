import random
from time import sleep

errormessage = "Error! Probeer opnieuw a.u.b"

def uitleg():
    print("We zullen effe beginnen met het uitleggen hoe de regels werken.")
    sleep(2)
    print("Voordat het spel begint worden alle kaarten geschud en wordt de bovenste kaart op de stapel gelegd. Deze bovenste kaart die wordt getrokken heeft geen effect in het begin")
    sleep(4)
    print("In het begin van het spel pakt iedereen 7 kaarten")
    sleep(2)
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
    # combineer 2 lists
    sortedCards = list(listColors) + list(listSpecial)
    # randomize de list en stop in nieuwe list
    randomizedCards = []
    randomizeProcess = False
    indexrange = 108
    while randomizeProcess == False:
        chosenCardNumber = random.randrange(0,int(indexrange))
        pickedCard = sortedCards[chosenCardNumber]
        randomizedCards.append(pickedCard)
        del sortedCards[chosenCardNumber]
        indexrange -= 1
        # indexrange check voor afbreken while loop
        if indexrange == 0:
            randomizeProcess = True
        else:
            None
    # voltooide resultaat terugsturen buiten de function
    return randomizedCards


def giveCards(players):
    # aanroepen andere function en results in variable stoppen
    cardList = createCards()
    # aanmaken van lists door dictionary
    ammoutPlayers = players
    ammouts = []
    ammoutPlayers += 1
    for numbers in range(1,ammoutPlayers):
        ammouts.append(numbers)
    dictionary = {}
    for playernummer in ammouts:
        dictionary['player%s' % playernummer] = []
    # uitdelen van de kaarten
    for givenCardCount in range(7):
        for key, value in dictionary.items():
            # aanpassing nodig!!!
            # dictionary[key].append(cardList[0])
            # aanpassing nodig!!!

            # idee misschien?
            # for key in dictionary:
            #     value = dictionary[key]
            # idee misschien?


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

giveCards(players)