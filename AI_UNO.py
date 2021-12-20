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
    players = input("Hoeveel spelers wilt u dat er meedoen? (Geef een nummer op) ")
    if players > 1 and players < 9:
        setup = True
    elif players == 1:
        print("Te weinig spelers")
    elif players > 8:
        print("Te veel spelers")
    else:
        print(errormessage)