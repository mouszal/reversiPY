
#!/usr/bin/env python
#
#
# A quoi ca va servir ce script
# reversi
#
#
import string
import random
def creationmatrice(ligne,colonne,valeur):
        """
        creation d'une matrice remplis de valeur donnees
        """
        listes = []
        if ligne%2 == 0 and colonne % 2 == 0 and ligne == colonne and  ligne>= 8:
                for i in range(ligne):
                        liste= []
                        for j in range(colonne):
                                liste.append(valeur)
                        listes.append(liste)
                return listes
        else:
                return False


def positionDebut(matrice,pion):
    """
    permet le placement des premieres pion
    """
    matrice[len(matrice)//2][len(matrice)//2] = pion[1]
    matrice[len(matrice)//2-1][len(matrice)//2] = pion[1]
    matrice[len(matrice)//2-1][len(matrice)//2-1] = pion[0]
    matrice[len(matrice)//2][len(matrice)//2-1] = pion[0]
    print( "Le plateau as bien ete creer")
def regle():
        """
        explique les regles
        """
        print("""
                Le but du jeu est d'avoir plus de pions de sa couleur que l'adversaire à la fin de la partie,
                celle-ci s'achevant lorsque aucun des deux joueurs ne peut plus jouer de coup légal,
                généralement lorsque les 64 cases sont occupées.

                Chacun à son tour, les joueurs vont poser un pion de leur couleur sur une case vide,
                adjacente à un pion adverse. Chaque pion posé doit obligatoirement encadrer un ou
                plusieurs pions adverses avec un autre pion de sa couleur, déjà placé.

                Il retourne alors le ou les pions adverse(s) qu'il vient d'encadrer. Les pions ne sont ni
                retirés de l'othellier, ni déplacés d'une case à l'autre.

                On peut encadrer des pions adverses dans les huit directions et plusieurs pions peuvent être encadrés dans chaque direction.
                """)

def affichermatrice(matrice):
        """
        Affichage du jeu
        """
        ligne, colonne = len(matrice), len(matrice[0])
        _alpha = list(string.ascii_lowercase)
        tests , coupure =  '    |','----+'
        for _pre in range(colonne):
                coupure += '----+'
                tests +=  "{:^4}|".format(_alpha[_pre])
        print(tests)
        print(coupure)
        for i in range(1,ligne+1):
                test=''
                test += "{:^4}|".format(i)
                for j in range(0,colonne):
                        test += "{:^4}|".format(matrice[i-1][j])
                print (test)
                print(coupure)
def compter(matrice,pion):
    nombre1,nombre2 = 0,0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j]== pion[0]:
                nombre1+=1
            elif matrice[i][j]== pion[1]:
                nombre2+=1
    return nombre1,nombre2
def changement(matrice,_j):
        """
        effectue les changements des pions conformement aux regles
        """
        liste = []
        for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                try:
                    if verification(matrice,i,j,_j)[1] >= 1 and matrice[i][j] == _j:
                        for _p in verification(matrice,i,j,_j)[2]:
                            _case = True
                            _cases = 1
                            while _case==True:
                                if matrice[_p[0]+_cases*(_p[0]-i) ][_p[1]+_cases*(_p[1]-j )] == _j:
                                    _case = False
                                    for _te in range(_cases):
                                        liste.append([_p[0]+ _te *(_p[0]-i),_p[1]+ _te *(_p[1]-j)])
                                elif matrice[_p[0]+_p[0]-i+ _cases][_p[1]+_p[1]-j + _cases] == 0:
                                    break
                                _cases += 1
                except:
                    pass
        return liste
def coupPossible(matrice,_j):
        """
        recense tous les coups possibles
        """
        liste = []
        for i in range(len(matrice)):
                for j in range(len(matrice[0])):
                        try:
                                if verification(matrice,i,j,_j)[1] >= 1 and matrice[i][j] == _j:
                                        for _p in verification(matrice,i,j,_j)[2]:
                                                _case = True
                                                _cases = 1
                                                while _case==True:
                                                        if matrice[_p[0]+_cases*(_p[0]-i) ][_p[1]+_cases*(_p[1]-j )]  == 0:
                                                                _case = False
                                                                liste.append([_p[0]+ _cases *(_p[0]-i),_p[1]+ _cases *(_p[1]-j)])
                                                        elif matrice[_p[0]+_p[0]-i+ _cases][_p[1]+_p[1]-j + _cases] == _j:
                                                                break
                                                        _cases += 1
                        except:
                                pass
        return liste

def afficherPossible(matrice,liste):
        """
        affiche les coups possible sous forme de tableau
        """
        _matrichetest= matrice
        for index,_co in liste:
                matrice[_co[0]][_co[1]] = index
        return _matrichetest

def verification(matrice,ligne,colonne,_j):
        """
        verifie s'il y des pions autour
        """
        nombre = 0
        emplacement = []
        for i in range(3):
                for j in range(3):
                        try:
                                if ligne-1+i == ligne and colonne-1+j == colonne or matrice[ligne-1+i][colonne-1+j] == 0:
                                        pass
                                elif matrice[ligne-1+i][colonne-1+j] != _j:
                                        nombre += 1
                                        emplacement.append([ligne-1+i,colonne-1+j])
                        except:
                                pass
        test = nombre == 0
        if test != True:
                return True,nombre,emplacement
        else:
                return "il faut qu'un pion enemie soit adjacente"
def jouerOrdis(matrice,_j):
        """
        donne les possibilites de jeu
        """
        choix = random.choice(coupPossible(matrice,_j))
        matrice[choix[0]][choix[1]] = _j

def jouer(matrice,_j):
        """
        donne les possibilites de jeu
        """
        print("possibilites de jeu:")
        print(coupPossible(matrice,_j))
        try :
            choix=int(input('        ////////////////////////QUELLE NUMERO VOULEZ VOUS ////////////////////////////'))
            choix = coupPossible(matrice,_j)[choix]
            matrice[choix[0]][choix[1]] = _j
        except:
            print('//////////////////  VEUILLEZ DONNER UN NOMBRE  ////////////////////////////')
            jouer(matrice,_j)


def jouer2joueur(joueur1,joueur2,victoire1 =0,victoire2 = 0):
        """
        jeu en mode 1 contre 1
        """
        matriceVoulu=input("""        ////////////////////////CHOISIR LA TAILLE DU PLATEAU//////////////////////////
        /////////////////////////////(LIGNE*COLONNE)//////////////////////////////////""")
        try :
                matriceVoulu = matriceVoulu.split('*')
                _matrice = creationmatrice(int(matriceVoulu[0]),int(matriceVoulu[1]),0)
                if _matrice == False:
                        print("        ////////////////////LE PLATEAU DOIT ETRE CARRE ET PAIRE////////////////////////")
                        jouer2joueur(joueur1,joueur2)
        except:
                print("        ////////////////////////LE PLATEAU N'EST PAS VALIDE//////////////////////////")
                jouer2joueur(joueur1,joueur2)
        pion1,pion2 = 'couleur1','couleur2'
        while len(pion1) != 1 and len(pion2) !=1:
            pion1 = input(' ////////////////////////////CHOISIR LE PION1///////////////////////////////')
            pion2 = input(' ////////////////////////////CHOISIR LE PION2///////////////////////////////')
        pion = pion1,pion2
        positionDebut(_matrice,pion)
        _jeuTermine = False
        nombredepassage = 0
        while not _jeuTermine :
                for _j in pion :
                        if len(coupPossible(_matrice,_j)) == 0:
                                print('0 possibilites votre tour est passer')
                                nombredepassage += 1
                                _jeuTermine = nombredepassage == 2
                        else:
                                nombredepassage = 0

                                if _j == pion1:
                                        print("        ////////////////////////TOUR DE "+joueur1+"//////////////////////////")
                                if _j == pion2:
                                        print("        ////////////////////////TOUR DE "+joueur2+"//////////////////////////")
                                affichermatrice(_matrice)
                                jouer(_matrice, _j)
                                while len(changement(_matrice,_j)) != 0:
                                        for i in changement(_matrice,_j):
                                                _matrice[i[0]][i[1]] = _j

        nombredepion = compter(_matrice,pion)
        if nombredepion[0] > nombredepion[1]:
                print(joueur1 +'a gagner la partie')
                victoire1 +=1
        elif nombredepion[0] == nombredepion[1]:
                print('EGALITER')
        else:
                print(joueur2 + 'a gagner la partie')
                victoire2 += 1
        print('        //////////1.REJOUER////////////////////////////////2.MENUPRINCIPAL////////////')
        try:
                _selection = int(input('        ////////////////////////QUELLE NUMERO VOULEZ VOUS ////////////////////////////'))
        except:
                MenuDebut()
        if _selection == 1:
                jouer2joueur(joueur1,joueur2,victoire1,victoire2)
        else :
                MenuDebut()
def jouerOrdi(joueur,victoire1 =0,victoire2 = 0):
        """
        permet le bon fonctionnement du jeu
        """
        matriceVoulu=input("""        ////////////////////////CHOISIR LA TAILLE DU PLATEAU//////////////////////////
        /////////////////////////////(LIGNE*COLONNE)//////////////////////////////////""")
        try :
                matriceVoulu = matriceVoulu.split('*')
                _matrice = creationmatrice(int(matriceVoulu[0]),int(matriceVoulu[1]),0)
                if _matrice == False:
                        print("        ////////////////////LE PLATEAU DOIT ETRE CARRE ET PAIRE////////////////////////")
                        jouerOrdi(joueur)
        except:
                print("        ////////////////////////LE PLATEAU N'EST PAS VALIDE//////////////////////////")
                jouerOrdi(joueur)
        pion1,pion2 = 'couleur1','couleur2'
        while len(pion1) != 1 and len(pion2) !=1:
            pion1 = input(' ////////////////////////////CHOISIR LE PION1///////////////////////////////')
            pion2 = input(' ////////////////////////////CHOISIR LE PION2///////////////////////////////')
        pion = pion1,pion2
        positionDebut(_matrice,pion)
        nombredepassage = 0
        _jeuTermine = False
        while not _jeuTermine :
            for _j in pion :
                if len(coupPossible(_matrice,_j)) == 0:
                        print('0 possibilites votre tour est passer')
                        nombredepassage += 1
                        _jeuTermine = nombredepassage != 2
                else:
                    nombredepassage = 0
                    if _j == pion1:
                            print("        ////////////////////////TOUR DE "+joueur+"//////////////////////////")
                            affichermatrice(_matrice)
                            jouer(_matrice, _j)
                    if _j == pion2:
                            print("        ////////////////////////   TOUR DE ORDI  ////////////////////////////")
                            affichermatrice(_matrice)
                            jouerOrdis(_matrice, _j)
                    while len(changement(_matrice,_j)) != 0:
                            print(changement(_matrice,_j))
                            affichermatrice(_matrice)
                            for i in changement(_matrice,_j):
                                    _matrice[i[0]][i[1]] = _j
        nombredepion = compter(_matrice,pion)
        if nombredepion[0] > nombredepion[1]:
                print(joueur +'a gagner la partie')
                victoire1 +=1
        elif nombredepion[0] == nombredepion[1]:
                print('EGALITER')
        else:
                print( "l'ordi a gagner la partie")
                victoire2 += 1
        print('        //////////1.REJOUER////////////////////////////////2.MENUPRINCIPAL////////////')
        try:
                _selection = int(input('        ////////////////////////QUELLE NUMERO VOULEZ VOUS ////////////////////////////'))
        except:
                MenuDebut()
        if _selection == 1:
                jouerOrdi(joueur,victoire1,victoire2)
        else :
                MenuDebut()
                        #_jeuTermine = detecterFinJeu(_matrice)
        jouer(matrice,_j)
def MenuDebut():
        """
        affiche le menu de debut de jeu
        """
        print("""
        //////////////////////////////////////////////////////////////////////////////
        //////////////////////////////////////////////////////////////////////////////
        ///////      ////      //  ////////        ////      /////     ///      //////
        //////  ////  ///  //////  ///////  /  ///////  ////  ///  /////////  ////////
        //////  ////  ///  ///////  /////  //  ///////  ////  ///  /////////  ////////
        //////       ////      ///  ////  ///      ///       /////    //////  ////////
        //////  ///  ////  //////// ///  ////  ///////  ///  ////////  /////  ////////
        //////  //// ////  ////////  /  /////  ///////  //// ////////  /////  ////////
        //////  ////  ///       ///    //////      ///  ////  ///     ////      //////
        //////////////////////////////////////////////////////////////////////////////
        //////////////////////////////////////////////////////////////////////////////
        //////////////////////////////////////////////////////////////////////////////
        //////////1.JOUER2JOUEUR//////2.JOUERORDI/////////3.REGLE//////4.QUIT/////////""")
        try:
                _selection = int(input('        ////////////////////////QUELLE NUMERO VOULEZ VOUS ////////////////////////////'))
        except:
                MenuDebut()
        if _selection == 1:
                joueur1 = input('        ///////////////////////indiquer votre pseudo joueur1//////////////////////////')
                joueur2 = input('        ///////////////////////indiquer votre pseudo joueur2//////////////////////////')
                jouer2joueur(joueur1,joueur2)
        elif _selection == 2:
                joueur= input('        ///////////////////////indiquer votre pseudo joueur ///////////////////////////')
                jouerOrdi(joueur)
        elif _selection == 3:
                regle()
                MenuDebut()
        elif _selection == 4:
                exit(0)
        else:
                print('        //////////////////VEUILLEZ DONNER UN NOMBRE ENTRE 1 ET 4 /////////////////////')
                MenuDebut()

# fonction principale
def main():
        """
        C'est la fonction principale
        """
        MenuDebut()

if __name__ == "__main__" :
        main()
