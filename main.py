import time
import random
import os
import copy
import title_printer

##Utilitaire :

def pretty_list(liste, NbProp, NbPions) : #Affiche la liste de l'avancement de
    l = len(liste)//2                     #la partie avec mise en forme
    for i in range(NbProp) :
        if i<l :
            print(liste[2*i], "  ", liste[2*i + 1])
        else :
            if NbPions == 4 :
                print("[          ]    [(    )]")
            else :
                print("[                ]    [(    )]")

def pretty_list_2(liste, NbProp, NbPions) : #Affiche la liste de recap de la partie
    l = len(liste)//2
    for i in range(NbProp) :
        if i<l :
            print(liste[2*i], "  ", liste[2*i + 1])

def doublons(liste) : #Regarde si une liste comporte des doublons
    l = len(liste)    #et renvoie un booléen
    doub = False
    for i in range(l) :
        if liste[i] in liste[i+1 :] :
            doub = True
    return(doub)

##Fonctions de menus

def print_title(): #Affiche le titre
    print("___  ___          _           ___  ____           _ ")
    print("|  \/  |         | |          |  \/  (_)         | |")
    print("| .  . | __ _ ___| |_ ___ _ __| .  . |_ _ __   __| |")
    print("| |\/| |/ _` / __| __/ _ | '__| |\/| | | '_ \ / _` |")
    print("| |  | | (_| \__ | ||  __| |  | |  | | | | | | (_| |")
    print("\_|  |_/\__,_|___/\__\___|_|  \_|  |_|_|_| |_|\__,_|")
    print("                                                    ")

#Les fonctions qui suivent affichent des sous-menus et du texte
def start_menu():
    print_title()
    print("")
    print("")
    print("  PROJET D'INFORMATIQUE - MPSI 2")
    print("")

def main_menu():
    start_menu()
    print("")
    print("")
    print("  MENU PRINCIPAL : ")
    print("")
    print("")
    print("    1) JOUEUR CONTRE JOUEUR ")
    print("    2) JOUEUR CONTRE MACHINE ")
    print("    3) MACHINE CONTRE JOUEUR ")
    print("    4) MACHINE CONTRE MACHINE ")
    print("    5) INDICATIONS ")
    print("    6) CREDITS ")
    print("    7) QUITTER ")
    print("")

def reglesdujeu() :
    print_title()
    print("")
    print("")
    print("   LE MASTERMIND EST UN JEU DE REFLEXION")
    print("   DANS LEQUEL UN CODEUR CHOISIT UNE")
    print("   COMBINAISON DE 4 OU 6 CHIFFRES DIFFERENTS")
    print("")
    print("   LE DECODEUR DOIT ENSUITE RETROUVER CETTE COMBINAISON")
    print("   EN FAISANT DES PROPOSITIONS DE COMBINAISONS")
    print("")
    print("   LE CODEUR L'AIDE EN LUI DONNANT DES INFORMATIONS SUR ")
    print("   LE NOMBRE DE CHIFFRES JUSTES, BIENS OU MAL PLACES")
    print("")
    print("APPUYEZ SUR ENTRER")

def indic_1() :
    print_title()
    print("")
    print("LE PLATEAU DE JEU S'AFFICHE DE LA MANIERE SUIVANTE :")
    print("")
    print("      [1, 4, 6, 2]    [(1, 2)]")
    print("")
    print("   A GAUCHE, LES PROPOSITIONS")
    print("   SUCCESSIVES DU DECODEUR")
    print("")
    print("APPUYEZ SUR ENTRER")

def indic_2() :
    print_title()
    print("")
    print("")
    print("")
    print("      [1, 4, 6, 2]    [(1, 2)]")
    print("")
    print("   A DROITE, LES INDICATIONS DU CODEUR")
    print("")
    print("   LE PREMIER CHIFFRE CORRESPOND")
    print("   AU NOMBRE DE CHIFFRES JUSTES ET BIEN PLACES")
    print("")
    print("APPUYEZ SUR ENTRER")

def indic_3() :
    print_title()
    print("")
    print("")
    print("")
    print("      [1, 4, 6, 2]    [(1, 2)]")
    print("")
    print("   A DROITE, LES INDICATIONS DU CODEUR")
    print("")
    print("   LE DEUXIEME CHIFFRE CORRESPOND")
    print("   AU NOMBRE DE CHIFFRES JUSTES MAIS MAL PLACES")
    print("")
    print("APPUYEZ SUR ENTRER")

def indic_4() :
    print_title()
    print("")
    print("")
    print("   VOUS DEVEZ ENTRER LES COMBINAISONS DE")
    print("   LA MANIERE SUIVANTE SOUS FORME D'UN NOMBRE")
    print("   A 4 ou 6 CHIFFRES. EX : 2476")
    print("")
    print("   LES CHIFFRES DOUIVENT COMPRIS ENTRE 1 ET 6 OU")
    print("   ENTRE 1 ET 8")
    print("")
    print("APPUYEZ SUR ENTRER")

##Certaines Fonctions sont parfois utilisées hors de leur mode d'origine

##Fonctions mode 1 :

def titre_mode_1() :
    print("")
    print("")
    print("+-----------------------------+")
    print("|                             |")
    print("|  MODE JOUEUR CONTRE JOUEUR  |")
    print("|                             |")
    print("+-----------------------------+")
    print("")
    print("")

def code_create(NbPions, code_base) : #Transforme un nombre de 4 ou 6 chiffres
    if NbPions == 4 :                 #en liste de 4 ou 6 éléments
        Na = code_base // 1000
        inter_1 = code_base - (1000*Na)
        Nb =  inter_1 // 100
        Nc = (inter_1 - (100*Nb)) // 10
        inter_2 = inter_1 - (100*Nb)
        Nd = (inter_2 - (10*Nc)) // 1
        combj = [Na, Nb, Nc, Nd]
    if NbPions == 6 :
        Na = code_base // 100000
        inter_1 = code_base - (100000*Na)
        Nb =  inter_1 // 10000
        inter_2 = inter_1 - 10000*Nb
        Nc = inter_2 // 1000
        inter_3 = inter_2 - (1000*Nc)
        Nd = inter_3 // 100
        inter_4 = inter_3 - (100*Nd)
        Ne = inter_4 // 10
        Nf = inter_4 - (10*Ne)
        combj = [Na, Nb, Nc, Nd, Ne, Nf]

    return(combj)

##Fonctions mode 2 :

def titre_mode_2() :
    print("")
    print("")
    print("+------------------------------+")
    print("|                              |")
    print("|  MODE JOUEUR CONTRE MACHINE  |")
    print("|                              |")
    print("+------------------------------+")
    print("")
    print("")

def comb(NbPions, NbTot) :     #Crée un code aléatoire sans doublons
    combinaison = []
    for i in range(NbPions):
        ele = random.randint(1, NbTot)
        while ele in combinaison :
            ele = random.randint(1, NbTot)
        combinaison.append(ele)
    return(combinaison)

def place(combj, NbPions, combinaison) : #Donne le nombre de chiffres justes ou mal placés
    nbrb = 0
    nbrm = 0
    for i in range(NbPions) :
        for j in range(NbPions) :
            if combinaison[i] == combj[j] and i == j :
                nbrb = nbrb + 1
            if combinaison[i] == combj[j] and i != j :
                    nbrm = nbrm + 1
    return(nbrb, nbrm)

##Fonctions mode 3 :

def titre_mode_3() :
    print("")
    print("")
    print("+------------------------------+")
    print("|                              |")
    print("|  MODE MACHINE CONTRE JOUEUR  |")
    print("|                              |")
    print("+------------------------------+")
    print("")
    print("")

def list_create(NbPions, NbTot) : #Créé la liste de toutes les codes possibles sous forme de
    possibilites = []             #sous-listes

    if NbPions == 4 : #pour une combinaison à 4 chiffres
        index = [1, 1, 1, 1]
        for i in range(NbTot) :
            index[1] = 1
            for j in range(NbTot) :
                index[2] = 1
                for k in range(NbTot) :
                    index[3] = 1
                    for l in range(NbTot) :
                        if not doublons(index) :
                           possibilites.append(copy.deepcopy(index))
                        index[3] = index[3] + 1
                    index[2] = index[2] + 1
                index[1] = index[1] + 1
            index[0] = index[0] + 1

    if NbPions == 6 : #pour une combinaison à 6 chiffres
        index = [1, 1, 1, 1, 1, 1]
        for i in range(NbTot) :
            index[1] = 1
            for j in range(NbTot) :
                index[2] = 1
                for k in range(NbTot) :
                    index[3] = 1
                    for l in range(NbTot) :
                        index[4] = 1
                        for m in range(NbTot) :
                            index[5] = 1
                            for n in range(NbTot) :
                                if not doublons(index) :
                                    possibilites.append(copy.deepcopy(index))
                                index[5] = index[5] + 1
                            index[4] = index[4] + 1
                        index[3] = index[3] + 1
                    index[2] = index[2] + 1
                index[1] = index[1] + 1
            index[0] = index[0] + 1

    return(possibilites)

##Fonctions mode 4 :


def titre_mode_4() :
    print("")
    print("")
    print("+-------------------------------+")
    print("|                               |")
    print("|  MODE MACHINE CONTRE MACHINE  |")
    print("|                               |")
    print("+-------------------------------+")
    print("")
    print("")

def moyenne(liste) : #Fait la moyenne des valeurs d'une liste (d'entiers ou de flottants)
    l = len(liste)
    moy = 0
    for i in liste :
        moy = moy + i
    moy = moy / l
    return(moy)

##Crédits :

def titre_credits() :
    print("")
    print("")
    print("+-----------+")
    print("|  CREDITS  |")
    print("+-----------+")
    print("")

##Main Game :

def main_game() : #fonction principale, son action dépend de ce qu'entre le joueur
    title_printer.name_printer()
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()
    quit = True

    try : #tant qu'il n'y a pas d'erreur
        choix = int(input("CHOIX DU MODE : "))
        print("")

        if choix in [1,2,3,4] : #action à réaliser uniquement dans les modes de jeu
            os.system('cls' if os.name == 'nt' else 'clear')
            start_menu()
            print("")
            print("CHOIX DU NOMBRE DE CHIFFRES DES PROPOSITIONS")
            NbPions = int(input("(4 ou 6) : "))
            print("")
            print("CHOIX NOMBRE DE CHIFFRES TOTAL")
            NbTot = int(input("(De 6 à 8 -conseillé-) : "))
            print("")
            print("CHOIX DU NOMBRE MAXIMAL DE PROPOSITIONS ")
            NbProp = int(input("(Entre 10 et 20) : "))
            if NbTot < NbPions :    #Fait entrer le programme en erreur
                _ = int(erreur)     #pour éviter une boucle infinie

        if choix == 1 : #Mode joueur contre joueur
            os.system('cls' if os.name == 'nt' else 'clear')
            print_title()
            titre_mode_1()
            liste_partie = []
            print("")

            if NbPions == 4 or NbPions == 6 :

                code_base = int(input("CODEUR : ENTREZ LE CODE SECRET : "))
                print("")
                combinaison = code_create(NbPions, code_base)
                print("")
                print("VOTRE COMBINAISON EST ", combinaison, " RETENEZ-LA")
                print("")
                print("APPUYEZ SUR ENTRER")
                _ = input()
                os.system('cls' if os.name == 'nt' else 'clear')
                print_title()
                print("")
                print("DECODEUR : C'EST A VOTRE TOUR")
                print("")
                code_essai = int(input("   ENTREZ UN CODE : "))
                combj = code_create(NbPions, code_essai)
                coups = 1
                liste_partie.append(combj)
                print("")
                print("   VOTRE CODE EST ", combj)
                print("")
                print("AIDE DU CODEUR :")
                print("")
                nbrb = int(input("   CHIFFRES JUSTES ET BIEN PLACES : "))
                print("")
                nbrm = int(input("   CHIFFRES JUSTES MAIS MAL PLACES : "))
                liste_partie.append([(nbrb, nbrm)])
                os.system('cls' if os.name == 'nt' else 'clear')
                print_title()
                print("")
                pretty_list(liste_partie, NbProp, NbPions)

                while ((nbrb, nbrm) != (NbPions, 0)) and (coups < NbProp) :
                    print("")
                    print("Nombres Biens placés / présents mais mal placés : ", (nbrb, nbrm))
                    print("")
                    print("COUPS RESTANTS : ", NbProp - coups)
                    print("")
                    print("")
                    print("NOUVELLE PROPOSITION : ")
                    print("")
                    code_essai = int(input("   ENTREZ UN CODE : "))
                    combj = code_create(NbPions, code_essai)
                    coups = coups + 1
                    liste_partie.append(combj)
                    print("")
                    print("   VOTRE CODE EST ", combj)
                    print("")
                    print("AIDE DU CODEUR :")
                    print("")
                    nbrb = int(input("   CHIFFRES JUSTES ET BIEN PLACES : "))
                    print("")
                    nbrm = int(input("   CHIFFRES JUSTES MAIS MAL PLACES : "))
                    liste_partie.append([(nbrb, nbrm)])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_title()
                    print("")
                    pretty_list(liste_partie, NbProp, NbPions)

                if (nbrb, nbrm) == (NbPions, 0) :
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_title()
                    print("")
                    print("VOUS AVEZ TROUVE EN ", coups, " COUPS !")
                    print("")
                    print("")
                    print("RECAPITULATIF DE LA PARTIE :")
                    print("")
                    print(combinaison)
                    if NbPions == 4 :
                        print("[__________]")
                    else :
                        print("[_______________]")
                    pretty_list_2(liste_partie, NbProp, NbPions)
                    print("")
                    print("APPUYEZ SUR ENTRER")
                else :
                    print("")
                    print("LE CODEUR A GAGNE !")
                    print("")
                    print("LA COMBINAISON ETAIT : ")
                    print(combinaison)
                    print("")
                    print("APPUYEZ SUR ENTRER")

            if NbPions != 4 and NbPions != 6 :
                print("")
                print("!!! NOMBRE INCORRECT !!!")
                print("")
                print("APPUYEZ SUR ENTRER")

            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')


        if choix == 2 : #mode joueur contre machine

            os.system('cls' if os.name == 'nt' else 'clear')
            print_title()
            titre_mode_2()
            liste_partie = []

            if NbPions == 4 or NbPions == 6 :

                combinaison = comb(NbPions, NbTot)
                print("")
                print("   C'EST A VOTRE TOUR")
                print("")
                code_essai = int(input("   ENTREZ UN CODE : "))
                combj = code_create(NbPions, code_essai)
                coups = 1
                print("")
                coups = 1
                liste_partie.append(combj)
                liste_partie.append([place(combj, NbPions, combinaison)])
                os.system('cls' if os.name == 'nt' else 'clear')
                print_title()
                print("")
                pretty_list(liste_partie, NbProp, NbPions)

                while (place(combj, NbPions, combinaison) != (NbPions, 0)) and (coups < NbProp) :
                    print("")
                    print("Nombres Biens placés / présents mais mal placés : ", place(combj, NbPions, combinaison))
                    print("")
                    print("COUPS RESTANTS : ", NbProp - coups)
                    print("")
                    print("")
                    print("DECODEUR : NOUVELLE PROPOSITION : ")
                    print("")
                    code_essai = int(input("   ENTREZ UN CODE : "))
                    combj = code_create(NbPions, code_essai)
                    print("")
                    coups = coups + 1
                    liste_partie.append(combj)
                    liste_partie.append([place(combj, NbPions, combinaison)])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_title()
                    print("")
                    pretty_list(liste_partie, NbProp, NbPions)

                if place(combj, NbPions, combinaison) == (NbPions, 0) :
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_title()
                    print("")
                    print("VOUS AVEZ TROUVE EN ", coups, " COUPS !")
                    print("")
                    print("")
                    print("RECAPITULATIF DE LA PARTIE :")
                    print("")
                    print(combinaison)
                    if NbPions == 4 :
                        print("[__________]")
                    else :
                        print("[_______________]")
                    pretty_list_2(liste_partie, NbProp, NbPions)
                    print("")
                    print("APPUYEZ SUR ENTRER")
                else :
                    print("")
                    print("VOUS AVEZ PERDU !")
                    print("")
                    print("LA COMBINAISON ETAIT : ")
                    print(combinaison)
                    print("")
                    print("APPUYEZ SUR ENTRER")

            if NbPions != 4 and NbPions != 6 :
                print("")
                print("!!! NOMBRE INCORRECT !!!")
                print("")
                print("APPUYEZ SUR ENTRER")

            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')


        if choix == 3 : #mode machine contre joueur

            os.system('cls' if os.name == 'nt' else 'clear')
            print_title()
            titre_mode_3()
            liste_partie = []
            print("")

            if NbPions == 4 or NbPions == 6 :
                code_base = int(input("CODEUR : ENTREZ LE CODE SECRET : "))
                print("")
                combinaison = code_create(NbPions, code_base)
                print("")
                print("VOTRE COMBINAISON EST ", combinaison, " RETENEZ-LA")
                print("")
                print("APPUYEZ SUR ENTRER")
                _ = input()
                os.system('cls' if os.name == 'nt' else 'clear')
                print_title()
                print("")
                if NbPions == 4 :
                    combj = [1, 2, 3, 4]
                if NbPions == 6 :
                    combj = [1, 2, 3, 4, 5, 6]
                print("PROPOSITION DE LA MACHINE : ", combj)
                coups = 1
                liste_partie.append(combj)
                print("")
                print("AIDE DU CODEUR :")
                print("")
                nbrb = int(input("   CHIFFRES JUSTES ET BIEN PLACES : "))
                print("")
                nbrm = int(input("   CHIFFRES JUSTES MAIS MAL PLACES : "))
                liste_partie.append([(nbrb, nbrm)])
                os.system('cls' if os.name == 'nt' else 'clear')
                print_title()
                print("")
                pretty_list(liste_partie, NbProp, NbPions)
                toute_prop = list_create(NbPions, NbTot)

                while ((nbrb, nbrm) != (NbPions, 0)) and (coups < NbProp) :

                    list_garder = []
                    l = len(toute_prop)
                    for i in range(l) :
                        if place(toute_prop[i], NbPions, combj) == (nbrb, nbrm) :
                            list_garder.append(toute_prop[i])

                    toute_prop = list_garder
                    l = len(toute_prop)
                    print("")
                    print("COUPS RESTANTS : ", NbProp - coups)
                    print("")
                    print("")
                    print("NOUVELLE PROPOSITION DE LA MACHINE : ")
                    print("")
                    combj = toute_prop.pop(random.randint(0, l-1))
                    print("   ", combj)
                    coups = coups + 1
                    liste_partie.append(combj)
                    print("")
                    print("AIDE DU CODEUR :")
                    print("")
                    nbrb = int(input("   CHIFFRES JUSTES ET BIEN PLACES : "))
                    print("")
                    nbrm = int(input("   CHIFFRES JUSTES MAIS MAL PLACES : "))
                    liste_partie.append([(nbrb, nbrm)])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_title()
                    print("")
                    pretty_list(liste_partie, NbProp, NbPions)

                if (nbrb, nbrm) == (NbPions, 0) :
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_title()
                    print("")
                    print("LA MACHINE A TROUVE EN ", coups, " COUPS !")
                    print("")
                    print("")
                    print("RECAPITULATIF DE LA PARTIE :")
                    print("")
                    print(combinaison)
                    if NbPions == 4 :
                        print("[__________]")
                    else :
                        print("[_______________]")
                    pretty_list_2(liste_partie, NbProp, NbPions)
                    print("")
                    print("APPUYEZ SUR ENTRER")
                else :
                    print("")
                    print("LE CODEUR A GAGNE !")
                    print("")
                    print("LA MACHINE N'A PAS TROUVE")
                    print("")
                    print("APPUYEZ SUR ENTRER")

            if NbPions != 4 and NbPions != 6 :
                print("")
                print("!!! NOMBRE INCORRECT !!!")
                print("")
                print("APPUYEZ SUR ENTRER")

            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')


        if choix == 4 : #mode machine contre machine
            if NbPions == 4 or NbPions == 6 :
                os.system('cls' if os.name == 'nt' else 'clear')
                print_title()
                titre_mode_4()
                print("")
                print("CE MODE PERMET DE REALISER DES PARTIES")
                print("DE MACHINE CONTRE MACHINE POUR VOIR L'EFFICACITE")
                print("DE LA STRATEGIE DE L'ALGORITHME DE RECHERCHE")
                print("")
                NbPart = int(input("   NOMBRE DE PARTIES : "))
                toute_prop_stock = list_create(NbPions, NbTot)
                list_efficace = []
                rate = 0
                print("")
                print("CELA PEUT PRENDRE UN CERTAIN TEMPS")

                for i in range(NbPart) : #nombre de parties à faire
                    toute_prop = copy.deepcopy(toute_prop_stock)
                    combinaison = comb(NbPions, NbTot)
                    if NbPions == 4 :
                        combj = [1, 2, 3, 4]
                    if NbPions == 6 :
                        combj = [1, 2, 3, 4, 5, 6]
                    (nbrb, nbrm) = place(combj, NbPions, combinaison)
                    coups = 1
                    while ((nbrb, nbrm) != (NbPions, 0)) and (coups < NbProp) :
                        list_garder = []
                        l = len(toute_prop)
                        for i in range(l) :
                            if place(toute_prop[i], NbPions, combj) == (nbrb, nbrm) :
                                list_garder.append(toute_prop[i])

                        toute_prop = list_garder
                        l = len(toute_prop)
                        combj = toute_prop.pop(random.randint(0, l-1))
                        coups = coups + 1
                        (nbrb, nbrm) = place(combj, NbPions, combinaison)
                    if (nbrb, nbrm) == (NbPions, 0) :
                        list_efficace.append(coups)
                    else :
                        rate = rate + 1

                os.system('cls' if os.name == 'nt' else 'clear')
                print_title()
                print("")
                print("   L'ORDINATEUR A TROUVE LE CODE EN FAISANT")
                print("   EN MOYENNE ", moyenne(list_efficace), " PROPOSITIONS")
                print("")
                print("   L'ORDINATEUR N'A PAS TROUVE LE ")
                print("   CODE ", rate, " FOIS")
                print("")
                print("")
                print("APPUYEZ SUR ENTRER")

            if NbPions != 4 and NbPions != 6 :
                print("")
                print("!!! NOMBRE INCORRECT !!!")
                print("")
                print("APPUYEZ SUR ENTRER")

            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')


        if choix == 5 : #indications et règles du jeu
            os.system('cls' if os.name == 'nt' else 'clear')
            reglesdujeu()
            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')
            indic_1()
            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')
            indic_2()
            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')
            indic_3()
            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')
            indic_4()
            _ = input()
            os.system('cls' if os.name == 'nt' else 'clear')


        if choix == 6 : #Crédits
            os.system('cls' if os.name == 'nt' else 'clear')
            start_menu()
            titre_credits()
            print("")
            print("   REALISE PAR JULIEN LALANNE ")
            print("")
            print("")
            print("   AMUSEZ-VOUS BIEN")
            print("")
            print("LE MENU VA FERMER DANS 5 SECONDES")

            TempsFin = time.time()
            close = TempsFin + 5
            while time.time() < close :
                NeFaitRien = True
            os.system('cls' if os.name == 'nt' else 'clear')


        if choix == 7 : #Quitter le jeu, fait passer un booléen à False

            quit = False
            os.system('cls' if os.name == 'nt' else 'clear')
            print_title()
            print("")
            print("")
            print("+----------------------+")
            print("|                      |")
            print("|  MERCI D'AVOIR JOUE  |")
            print("|  A NOTRE MASTERMIND  |")
            print("|                      |")
            print("+----------------------+")
            print("")
            print("")
            print("LE JEU VA FERMER DANS 3 SECONDES")

            TempsFin = time.time()
            close = TempsFin + 3
            while time.time() < close :
                NeFaitRien = True
            os.system('cls' if os.name == 'nt' else 'clear')

    except : #boucle d'erreur
        os.system('cls' if os.name == 'nt' else 'clear')
        print_title()
        print("")
        print("  VOUS AVEZ ENTRE UNE TOUCHE NON AUTORISEE")
        print("  RETOURNEZ AU MENU PRINCIPAL")
        print("")
        print("APPUYEZ SUR ENTRER")
        _ = input()

    return(quit)

##BOUCLE PRINCIPALE

end = True
while end == True :
    end = main_game()

os.system('cls' if os.name == 'nt' else 'clear')
