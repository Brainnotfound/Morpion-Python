from MorpionCode import *


def JvsIA():
        jouer = 'oui'
        while jouer == 'oui':
            # Initialisation des variables nécessaires à chaque parties
            compteur = 0
            symbJoueur = 'O'
            numJoueur = 2
            victoire = False
            tabCalc = tabCalcInit
            # tabVisu = tabVisuInit

            while victoire is not True and compteur <= 9:

                # Initialisation des variables nécessaires à chaque tours
                compteur += 1
                if symbJoueur == 'O':
                    symbJoueur = 'X'
                    numJoueur -= 1
                else:
                    symbJoueur = 'O'
                    numJoueur += 1
                clearPrompt()  # Nettoie l'écran avant d'afficher la grille
                PrintTabVisu()

                if symbJoueur == 'X':
                    # Saisie des coordonnées où placer le symbole du joueur (avec vérifications)
                    verif = False
                    while verif is False:
                        tabVisu, tabCalc, verif = SetInTable(symbJoueur)
                        if verif is False:
                            print('Cette case est déjà prise!')
                else:
                    tabVisu, tabCalc = TourIA(symbJoueur)

                victoire = CalcVictoire()
            clearPrompt()
            PrintTabVisu()

            # En cas de victoire d'un joueur
            if victoire is True:
                print('Le joueur ' + str(numJoueur) + ' remporte la partie!')
            # En cas d'égalité
            else:
                print('Égalité entre les deux joueurs')

            # Demande si le(s) joueurs souhaitent rejouer
            continuer = True
            while continuer:
                try:
                    rep = input('Désirez-vous continuer à jouer contre l\'ordinateur ? (oui/non) : ')
                    if rep.lower() == "oui":
                        jouer = rep.lower()
                        break
                    elif rep.lower() == "non":
                        clearPrompt()
                        jouer = rep.lower()
                        break
                    else:
                        print("Entrez une réponse valide ...")
                except Exception:
                    print("Entrez une réponse valide ...")
                    continue


if __name__ == "__main__":  # Permet de lancer uniquement ce fichier si c'est celui-ci qui est explicitement exécuté (Afin de tester).
    JvsIA()