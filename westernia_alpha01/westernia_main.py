#charger modules
import codecs
from prettytable import PrettyTable
import random

#definir classes
class Approbation:
    def __init__(self,apPeuple,apParti,apMonde,apGouv):
        self.apPeuple = apPeuple
        self.apParti = apParti
        self.apMonde = apMonde
        self.apGouv = apGouv
    def update(self,pe,pa,mo,go):
        self.apPeuple+=pe
        if self.apPeuple > 100:
            self.apPeuple = 100
        self.apParti+=pa
        if self.apParti > 100:
            self.apParti = 100
        self.apMonde+=mo
        if self.apMonde > 100:
            self.apMonde = 100
        self.apGouv+=go
        if self.apGouv > 100:
            self.apGouv = 100
    def affiche(self):
        ap_table = PrettyTable()
        ap_table.title = 'APPROBATION'
        ap_table.field_names = ["Peuple", "Parti", "Communauté Internationale", "Gouvernement"]
        ap_table.add_row([self.apPeuple,self.apParti,self.apMonde,self.apGouv])
        print(ap_table)

class Parti:
    def __init__(self,id,nom,abrege,societe,economie,diplomatie):
        self.id = id
        self.nom = nom
        self.abrege = abrege
        self.societe = societe
        self.economie = economie
        self.diplomatie = diplomatie
    def affiche(self):
        parti_tab = PrettyTable()
        parti_tab.title = self.nom
        parti_tab.field_names = ["Société", "Economie", "Diplomatie"]
        parti_tab.add_row([self.societe,self.economie,self.diplomatie])
        print(parti_tab)

class Carte:
    def __init__(self,id,categorie,type,caracteristique,titre,description,special,collection,pixabay,texteChoixA,texteChoixB, \
    peupleChoixA,peupleMatchChoixA,partiChoixA,partiMatchChoixA,mondeChoixA, \
    mondeMatchChoixA, gouvChoixA,gouvMatchChoixA,peupleChoixB,peupleMatchChoixB, \
    partiChoixB,partiMatchChoixB,mondeChoixB,mondeMatchChoixB,gouvChoixB,gouvMatchChoixB,specialChoixA,specialChoixB):
        self.id = id
        self.categorie = categorie
        self.type = type
        self.caracteristique = caracteristique
        self.titre = titre
        self.description = description
        self.special = special
        self.collection = collection
        self.pixabay = pixabay
        self.texteChoixA = texteChoixA
        self.texteChoixB = texteChoixB
        self.peupleChoixA = peupleChoixA
        self.peupleMatchChoixA = peupleMatchChoixA
        self.partiChoixA = partiChoixA
        self.partiMatchChoixA = partiMatchChoixA
        self.mondeChoixA = mondeChoixA
        self.mondeMatchChoixA = mondeMatchChoixA
        self.gouvChoixA = gouvChoixA
        self.gouvMatchChoixA = gouvMatchChoixA
        self.peupleChoixB = peupleChoixB
        self.peupleMatchChoixB = peupleMatchChoixB
        self.partiChoixB = partiChoixB
        self.partiMatchChoixB = partiMatchChoixB
        self.mondeChoixB = mondeChoixB
        self.mondeMatchChoixB = mondeMatchChoixB
        self.gouvChoixB = gouvChoixB
        self.gouvMatchChoixB = gouvMatchChoixB
        self.specialChoixA = specialChoixA
        self.specialChoixB = specialChoixB
    def affiche(self):
        print(self.id,"[",self.categorie,"]",self.titre.upper())
        carte_sep="+------------------------------------------------------------------+"
        print(self.description)
        print(carte_sep)
        print("A. "+self.texteChoixA)
        print("B. "+self.texteChoixB)
        print(carte_sep)
#les fonctions
def check_approbation(sonApprobation):
    if sonApprobation.apParti<=0:
        print("\n    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")
        print("                      Le PARTI vous désapprouve !                          ")
        print("                           -----------------                             ")
        print("Un de vos ministres qui est aussi président du parti, a démissionné\n\
         pour former un nouveau parti soit disant plus en accord avec ses idéaux.\n\
         Etrangement l’ensemble des membres du parti l’ont rejoint, vous laissant seul\n\
         et sans soutien pour les prochaines élections.")
        return(1)
    elif sonApprobation.apPeuple<=0:
        print("\n    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")
        print("                      Le PEUPLE vous désapprouve !                          ")
        print("                           -----------------                             ")
        print("Le peuple considère que vous êtes le pire président de l’Histoire de WESTERNIA.\n\
Malheureusement, vous devez déclarer que vous ne vous présenterez pas aux\n\
prochaines élections pour calmer les esprits.")
        return(1)
    elif sonApprobation.apMonde<=0:
        print("\n    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")
        print("               La COMMUNAUTE INTERNATIONALE vous désapprouve !             ")
        print("                           -----------------                             ")
        print("Toutes les nations du monde rient de WESTERNIA. Lors du dernier referendum,\n\
        les westerniens se sont prononcés en faveur du retrait de WESTERNIA de la communauté internationale\n\
        pour rejoindre une coalition avec la Corée du Nord.\n\
        De honte, vous avez démissionné de vos fonctions présidentielles.")
        return(1)
    elif sonApprobation.apGouv<=0:
        print("\n    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")
        print("                  Le GOUVERNEMENT vous désapprouve !                          ")
        print("                           -----------------                             ")
        print("Plusieurs régions de WESTERNIA ont proclamées leur indépendance suite à votre politique désastreuse.\n\
        Le président du Sénat avec le soutien de l’armée vous force à signer la dislocation de la république.")
        return(1)
    else:
        return(0)
def modif_modif(modificateur):
    if modificateur < 0:
        modificateur = modificateur*7
    else:
        modificateur = modificateur*3
    return(modificateur)

def applique_choix(sonChoix, sonApprobation, saCarte, sonParti):
    if saCarte.type == "societe":
        if saCarte.caracteristique == sonParti.societe:
            if sonChoix == "A":
                modifPeuple = saCarte.peupleMatchChoixA
                modifParti = saCarte.partiMatchChoixA
                modifMonde = saCarte.mondeMatchChoixA
                modifGouv = saCarte.gouvMatchChoixA
            else:
                modifPeuple = saCarte.peupleMatchChoixB
                modifParti = saCarte.partiMatchChoixB
                modifMonde = saCarte.mondeMatchChoixB
                modifGouv = saCarte.gouvMatchChoixB
        else:
            if sonChoix == "A":
                modifPeuple = saCarte.peupleChoixA
                modifParti = saCarte.partiChoixA
                modifMonde = saCarte.mondeChoixA
                modifGouv = saCarte.gouvChoixA
            else:
                modifPeuple = saCarte.peupleChoixB
                modifParti = saCarte.partiChoixB
                modifMonde = saCarte.mondeChoixB
                modifGouv = saCarte.gouvChoixB
    elif saCarte.type == "economie":
        if saCarte.caracteristique == sonParti.economie:
            if sonChoix == "A":
                modifPeuple = saCarte.peupleMatchChoixA
                modifParti = saCarte.partiMatchChoixA
                modifMonde = saCarte.mondeMatchChoixA
                modifGouv = saCarte.gouvMatchChoixA
            else:
                modifPeuple = saCarte.peupleMatchChoixB
                modifParti = saCarte.partiMatchChoixB
                modifMonde = saCarte.mondeMatchChoixB
                modifGouv = saCarte.gouvMatchChoixB
        else:
            if sonChoix == "A":
                modifPeuple = saCarte.peupleChoixA
                modifParti = saCarte.partiChoixA
                modifMonde = saCarte.mondeChoixA
                modifGouv = saCarte.gouvChoixA
            else:
                modifPeuple = saCarte.peupleChoixB
                modifParti = saCarte.partiChoixB
                modifMonde = saCarte.mondeChoixB
                modifGouv = saCarte.gouvChoixB
    elif saCarte.type == "diplomatie":
        if saCarte.caracteristique == sonParti.diplomatie:
            if sonChoix == "A":
                modifPeuple = saCarte.peupleMatchChoixA
                modifParti = saCarte.partiMatchChoixA
                modifMonde = saCarte.mondeMatchChoixA
                modifGouv = saCarte.gouvMatchChoixA
            else:
                modifPeuple = saCarte.peupleMatchChoixB
                modifParti = saCarte.partiMatchChoixB
                modifMonde = saCarte.mondeMatchChoixB
                modifGouv = saCarte.gouvMatchChoixB
        else:
            if sonChoix == "A":
                modifPeuple = saCarte.peupleChoixA
                modifParti = saCarte.partiChoixA
                modifMonde = saCarte.mondeChoixA
                modifGouv = saCarte.gouvChoixA
            else:
                modifPeuple = saCarte.peupleChoixB
                modifParti = saCarte.partiChoixB
                modifMonde = saCarte.mondeChoixB
                modifGouv = saCarte.gouvChoixB
    else:
        if sonChoix == "A":
            modifPeuple = saCarte.peupleChoixA
            modifParti = saCarte.partiChoixA
            modifMonde = saCarte.mondeChoixA
            modifGouv = saCarte.gouvChoixA
        else:
            modifPeuple = saCarte.peupleChoixB
            modifParti = saCarte.partiChoixB
            modifMonde = saCarte.mondeChoixB
            modifGouv = saCarte.gouvChoixB
    modifPeuple = modif_modif(modifPeuple)
    modifParti = modif_modif(modifParti)
    modifMonde = modif_modif(modifMonde)
    modifGouv = modif_modif(modifGouv)
    sonApprobation.update(modifPeuple,modifParti,modifMonde,modifGouv)
    return(sonApprobation)

#charger les donnees
##partis
partis_all = []
with codecs.open('donnees/partis.csv', encoding='utf-8') as parti_file:
    for line in parti_file.readlines()[1:]:
        lineSplit=line.split('\t')
        line_id = int(lineSplit[0])
        line_nom = str(lineSplit[1])
        line_abrege = str(lineSplit[2])
        line_societe = str(lineSplit[3])
        line_economie = str(lineSplit[4])
        line_diplomatie = str(lineSplit[5])
        line_parti=Parti(line_id,line_nom,line_abrege,line_societe,line_economie,line_diplomatie)
        partis_all.append(line_parti)
parti_file.closed

##cartes
cartes_all=[]
with codecs.open('donnees/cartes.csv', encoding='utf-8') as carte_file:
    for line in carte_file.readlines()[1:]:
        lineSplit=line.split('\t')
        l_id=int(lineSplit[0])
        l_categorie = str(lineSplit[1])
        l_type = str(lineSplit[2])
        l_caracteristique = str(lineSplit[3])
        l_titre = str(lineSplit[4])
        l_description = str(lineSplit[5])
        l_special = str(lineSplit[6])
        l_collection = str(lineSplit[7])
        l_pixabay = str(lineSplit[8])
        l_texteChoixA = str(lineSplit[9])
        l_texteChoixB = str(lineSplit[10])
        l_peupleChoixA = int(lineSplit[11])
        try:
            l_peupleMatchChoixA = int(lineSplit[12])
        except ValueError:
            l_peupleMatchChoixA = None
        l_partiChoixA = int(lineSplit[13])
        try:
            l_partiMatchChoixA = int(lineSplit[14])
        except ValueError:
            l_partiMatchChoixA = None
        l_mondeChoixA = int(lineSplit[15])
        try:
            l_mondeMatchChoixA = int(lineSplit[16])
        except ValueError:
            l_mondeMatchChoixA = None
        l_gouvChoixA = int(lineSplit[17])
        try:
            l_gouvMatchChoixA = int(lineSplit[18])
        except ValueError:
            l_gouvMatchChoixA = None
        l_peupleChoixB = int(lineSplit[19])
        try:
            l_peupleMatchChoixB = int(lineSplit[20])
        except ValueError:
            l_peupleMatchChoixB = None
        l_partiChoixB = int(lineSplit[21])
        try:
            l_partiMatchChoixB = int(lineSplit[22])
        except ValueError:
            l_partiMatchChoixB = None
        l_mondeChoixB = int(lineSplit[23])
        try:
            l_mondeMatchChoixB = int(lineSplit[24])
        except ValueError:
            l_mondeMatchChoixB = None
        l_gouvChoixB = int(lineSplit[25])
        try:
            l_gouvMatchChoixB = int(lineSplit[26])
        except ValueError:
            l_gouvMatchChoixB = None
        l_specialChoixA = str(lineSplit[27])
        l_specialChoixB = str(lineSplit[28])
        line_carte=Carte(l_id,l_categorie,l_type,l_caracteristique,l_titre,l_description, \
        l_special,l_collection,l_pixabay,l_texteChoixA,l_texteChoixB, l_peupleChoixA, \
        l_peupleMatchChoixA,l_partiChoixA,l_partiMatchChoixA,l_mondeChoixA,l_mondeMatchChoixA, \
        l_gouvChoixA,l_gouvMatchChoixA,l_peupleChoixB,l_peupleMatchChoixB,l_partiChoixB, \
        l_partiMatchChoixB,l_mondeChoixB,l_mondeMatchChoixB,l_gouvChoixB,l_gouvMatchChoixB, \
        l_specialChoixA,l_specialChoixB)
        cartes_all.append(line_carte)
carte_file.closed

#Disclaimer
print("\n    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")
print("                           W E S T E R N I A                             ")
print("                           -----------------                             \n")
print("Vous incarnez le président nouvellement élu de la république de WESTERNIA.\n\
C'est un pays imaginaire, archétype de la moyenne puissance occidental type.\n\
Votre but est de mener une politique arriviste afin d’être réélu\n\
président de la république aux prochaines élections.\n\n\
Pendant toute la durée de votre mandat, on vous demandera de réagir par des choix\n\
à des évènements majeurs, qui impacteront votre popularité et\n\
votre réseau de soutiens.\n\n\
Pour rester président et vous assurez votre réélection,\n\
vous devrez impérativement vous assurez de maintenir l’approbation du peuple,\n\
de votre parti, de la communauté internationale et du gouvernement.\n\
Faîtes les bons choix !\n\n")
monStart=None
while(monStart == None):
    monStart = input("Commencez une partie [ appuyer sur ENTER ]")


print("\n    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")


#set up
##choix du parti
partis_table = PrettyTable()
partis_table.field_names = ["  #  ", "Parti", "Société", "Economie", "Diplomatie"]
for i in partis_all:
    sidl="  "+str(i.id)
    partis_table.add_row([sidl, i.nom, i.societe, i.economie, i.diplomatie])
print(partis_table)
monNumeroParti=-1
while(monNumeroParti not in range(1,len(partis_all)+1)):
    try:
        monNumeroParti = int(input("Choisissez votre parti politique [ entrer le numero correspondant ]"))
    except ValueError:
        print("Merci d'entrer un numero")
monParti = partis_all[monNumeroParti-1]
print("Votre parti politique est `",monParti.nom,"`.")
print("Ses caracteristiques sont les suivantes :")
monParti.affiche()


monApprobation=Approbation(100,100,100,100)

Maduree=16
#Piocher une carte
categories_all=["economie","societe","international","politique","culture","sport","planete"]
categories_tour= categories_all
categories_counter=int(len(categories_all))
deck = [carte for carte in cartes_all if carte.collection == "normal"]
for tour in range(1,Maduree):
    if categories_counter < 2:
        categories_counter=int(len(categories_all))
        categories_tour= []
        categories_tour= categories_all
    selectedCategorie=random.choice(categories_tour)
    categories_tour = [c for c in categories_tour if c!=selectedCategorie]
    categories_counter-=1
    categorieCartes= []
    for carte in deck:
        if carte.categorie == selectedCategorie:
            categorieCartes.append(carte)
    selectedCarte=random.choice(categorieCartes)
    indexcartesall=0
    for carte in deck:
        if carte.id == selectedCarte.id:
            del deck[indexcartesall]
            break
        indexcartesall+=1
    print("\n    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")
    print("             Vous êtes au pouvoir depuis",tour,"tour sur",Maduree)
    print("                           -----------------                             \n")
    monApprobation.affiche()
    selectedCarte.affiche()
    monChoix=-1
    while(monChoix not in ["A","B"]):
        try:
            monChoix = str(input("Faîtes votre choix [ entrer \"A \" ou \"B\" ]"))
        except ValueError:
            print("Merci d'entrer la lettre A ou B")
    tmpApprobation=applique_choix(monChoix, monApprobation, selectedCarte, monParti)
    monApprobation=tmpApprobation
    if check_approbation(monApprobation):
        break
#fin
print("    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")
print("La partie est finie, merci d'avoir jouer à WESTERNIA\n")
print("    ^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^W^    \n")
