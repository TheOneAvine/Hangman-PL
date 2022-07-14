import resources as r
import random

input("Gramy w wisielca. Komputer wybiera słowo, a my zgadujemy. Kliknij Enter, aby rozpocząć!\n")
#this chooses a random word from a list in a separate file

while True:

    słowo = random.choice(r.słowa)

    #this counts the number of letters to later display blanks
    litery = len(słowo)

    #this creates a list of letters in the word
    lista_litery = list(słowo)
    #this creates the blank spaces 
    luki = list(litery * '_')

    #the hanging
    szubienica_po_kolei = [r.baza, r.słup, r.szubienica2, r.sznur, r.głowa, r.ręce, r.powieszony]
    wykorzystane_litery = []
   

    #this will be the actual game
    while True:
        if szubienica_po_kolei == []:
                print("Skończyły ci się próby. Wisisz!")
                print("Słowo to było", słowo)
                break
        luki_litery = ' '.join(luki)
        print(luki_litery, '\n')
        zgaduj = input("Zgaduj literkę!\n")

        if zgaduj in lista_litery:
            print("Zgadłeś!")

            for i in range(len(lista_litery)):
                if lista_litery[i] == zgaduj:
                    luki[i] = zgaduj
        else:
            print("Tej litery nie ma!")
            wykorzystane_litery.append(zgaduj)
            print(szubienica_po_kolei[0])
            del szubienica_po_kolei[0]
            print("Litery, które już wykorzystałeś, to: "+ ' '.join(wykorzystane_litery))
    
        luki_litery_bez = ''.join(luki)
        if luki_litery_bez == słowo:
            print("Wygrałeś! Brawo!")
            print("Hasło to:", luki_litery_bez)
            break

    
    gramy_dalej = input("Czy chcesz spróbować ponownie? T/N")
    gramy_dalej.lower()
    if gramy_dalej == "n": break

            




