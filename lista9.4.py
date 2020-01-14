import time
import pickle

lista = []

try:
    tiedosto = open("muistio.dat", "rb")
    lue = pickle.load(tiedosto)
    for i in lue:
        lista.append(i)
    tiedosto.close()
except IOError:
    tiedosto = open("muistio.dat", "wb")
    print("Virhe tiedostossa, luodaan uusi muistio.dat.")
    tiedosto.close()

jatka = True
while jatka:
    print("(1) Lue muistikirjaa")
    print("(2) Lisää merkintä")
    print("(3) Muokkaa merkintää")
    print("(4) Poista merkintä")
    print("(5) Tallenna ja lopeta")
    try:
        valinta = int(input("Mitä haluat tehdä?: "))
        if valinta == 1:
            for i in lista:
                print(i)
        elif valinta == 2:
            merkinta = input("Kirjoita uusi merkintä: ")
            aika = time.strftime("%X %x")
            lisays = merkinta+":::"+aika
            lista.append(lisays)
        elif valinta == 3:
            alkiot = len(lista)
            print("Listalla on ",alkiot," merkintää.")
            muutos = int(input("Mitä niistä muutetaan?: "))
            muutos = muutos -1
            print(lista[muutos])
            lista.pop(muutos)
            uusimerkinta = input("Anna uusi teksti: ")
            aika = time.strftime("%X %x")
            uusilisays = uusimerkinta+":::"+aika
            lista.insert(muutos,uusilisays)
        elif valinta == 4:
            alkiot = len(lista)
            print("Listalla on ",alkiot," merkintää.")
            poisto = int(input("Mitä niistä poistetaan?: "))
            poisto = poisto -1
            print("Poistettiin merkintä", lista[poisto])
            lista.pop(poisto)
        elif valinta == 5:
            tiedosto = open("muistio.dat","wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
            print("Lopetetaan.")
            jatka = False
            break
    except Exception:
        print("Tuntematon valinta.")