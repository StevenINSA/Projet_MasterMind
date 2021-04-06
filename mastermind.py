import math
import sys
from random import randint

# Les variables globales que nous allons utiliser

COULEURS = ["Rouge", "Jaune", "Bleu", "Orange", "Vert", "Blanc", "Violet", "Rose"]
NB_PIONS = 4
NB_MAX_COUP = 10
COMBINAISON_SECRETE = [] #servia à stocker la combinaison recherchée par l'algo
HISTORIQUE = [] #tableau qui stocke l'ensemble des coups joués. L'indice 0 sera la première combinaison de 4 couleurs, etc..

# Les fonctions

def genere_combinaison_secrete(): #fonction qui génère une combinaison secrete
    combinaison = []
    for i in range (NB_PIONS):
        random = randint(0, 7)
        combinaison.append(COULEURS[random])

    return combinaison

def compare(combinaison1, combinaison2):
#cette fonction servira à comparer deux combinaison entre elles.
#elle retournera le nombre de pion bien placés et le nombre de pion mal placés mais de la bonne couleur

    pc = 0 #nombre de couleur correctement placées
    mc = 0 #nombre de couleur présentes mais mal placées
    tab_indice1 = [i for i in range (NB_PIONS)] #servira à calculer pc
    tab_indice2 = [i for i in range (NB_PIONS)] #servira à calculer mc

    #Première étape, on regarde le nombre de pion bien placés
    #Si on a effectivement une ou plusieurs couleurs, on va supprimer les indices des tables
    #afin de ne pas les prendres en compte lors du calcul des mc
    for i in range (NB_PIONS):
        if combinaison1[i] == combinaison2[i]:
            tab_indice1.remove(i)
            tab_indice2.remove(i)
            pc+=1

    #Deuxième étape, on regarde le nombre de pion de la bonne couleur, mais mal placés.
    #Il est important de supprimer les indices de la table une nouvelle fois pour ne pas
    #compter plusieurs fois une couleur de la combinaison2.
    #Le "break" sert à arrêter de comparer les couleurs de la combinaison1, et de passer à la suivante
    for i in tab_indice1:
        for j in tab_indice2:
            if combinaison1[i] == combinaison2[j]:
                tab_indice2.remove(j)
                mc+=1
                break

    #On retourne le nombre de pion bien ou mal placés
    return pc, mc

def score(pc,mc):
    if pc<0 or mc<0:
        return -1
    elif pc==0 and mc==0:
        return 0
    else:
        return 3*pc+mc

def eval(candidat, candidat_precedent):

#cf compte rendu pour l'explication

    candidat_precedent_pc, candidat_precedent_mc = compare(COMBINAISON_SECRETE, candidat_precedent)
    candidat_precedent_score = score(candidat_precedent_pc, candidat_precedent_mc)

    virtuel_pc, virtuel_mc = compare(candidat, candidat_precedent)
    virtuel_score = score(virtuel_pc, virtuel_mc)

    return abs(virtuel_score - candidat_precedent_score)

def Fitness(candidat):
    eval_moyenne = 0

    for i in range (len(HISTORIQUE)):
        eval_moyenne += eval(candidat, HISTORIQUE[i])

    return eval_moyenne/len(HISTORIQUE)




# Le main

if __name__ == "__main__":
    COMBINAISON_SECRETE = genere_combinaison_secrete()
    #COMBINAISON_SECRETE = ['Bleu', 'Bleu', 'Rose', 'Bleu']
    print("combinaison : ", COMBINAISON_SECRETE)

    candidat = ['Rouge', 'Rouge', 'Bleu', 'Vert']
    print("candidat : ", candidat)
    print(compare(COMBINAISON_SECRETE, candidat))

    candidat_precedent = ['Rouge', 'Violet', 'Blanc', 'Vert']
    evaluation = eval(candidat, candidat_precedent)
    print("eval : ", evaluation)

    HISTORIQUE = [candidat_precedent, candidat]
    print("historique : ", HISTORIQUE)
    candidat2 = ['Blanc', 'Rouge', 'Bleu', 'Jaune']

    print("Fitness : ", Fitness(candidat2))
