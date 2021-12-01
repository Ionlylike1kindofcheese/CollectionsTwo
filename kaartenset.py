import random

kleuren = ["klaveren ", "schoppen ", "harten ", "ruiten "]
waardes = ["aas", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer"]

def generateCards():
    randomcompletion = False
    kaarten = []
    randomizedcards = []
    indexrange = 53
    for i in range(4):
        for u in range(13):
            kaarten.append(kleuren[i] + waardes[u])
    for j in range(2):
        kaarten.append("joker")   
    while randomcompletion == False:
        listpick = random.randrange(0,indexrange)
        randomizedcards.append(kaarten[listpick])
        del kaarten[listpick]
        indexrange = indexrange - 1
        if indexrange == 0:
            randomcompletion = True
    return randomizedcards


kaartenlist = generateCards()
for x in range(1,8):
    print("Kaart " + str(x) + ":", str(kaartenlist[1]))
    del kaartenlist[1]
print()
print("deck (47 kaarten):", kaartenlist)