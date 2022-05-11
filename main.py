from tkinter import *  # Importation de tous les fichiers de la bibliothèque Tkinter
from tkinter import ttk
import random  # Importation de la bibliothèque random qui permettra de choisir un mot aléatoire dans le fichier XML
from tkinter import messagebox
import xml.dom.minidom  # importation de la bibliotheque minidom de xml
import time  # importation de la bibliotheque du temps pour le chrono
i = 0
tab_xml =["table", "chaise", "vide"]  # Déclaration de la zone tampons pour le xml (un tableau)
sec = 0  # Déclaration d'un timer pour les parties. Il aura une influence sur le score final
tab_temps = []  # Tableau qui récupère la valeur du temps écoulé sur une partie de pendu
doTick = True

def getEntry():  # fonction qui permet de recupérer le pseudo du joueur
    res = pseudoUser.get()
    return res


cpt = 0  # Déclaration d'un compteur d'erreurs lors d'une partie
secret = ""  # Déclaration du mot à trouver
windows = Tk()  # Déclaration de la fenêtre principale


def ouvrirLeave():  # Fonction permettant de fermer le jeu en appuyant sur le bouton "Quitter"
    print("Fermeture de la page")
    windows.destroy()  # Instruction permettant la fermeture du jeu


############################################################# Page Aide #############################################################
#### Cette page explique les règles du jeu du Pendu

def ouvrirAide():  # Cette fonction ouvre la page d'aide
    windows.withdraw()  # Elle cache la page principale
    aide = Tk()  # Puis elle déclare la page d'aide qui s'ouvrira un peu plus loin dans le code

    def fonctionRetour():  # Cette fonction permet de retourner sur la page principale. On appelle cette fonction sur un bouton retour qui sera placé sur la page d'aide
        aide.withdraw()  # Elle cache la fenêtre d'aide
        windows.deiconify()  # Et remet au premier plan la page principale

    aide.config(bg='#CAAEF0')  # Couleur de fond de la page d'aide
    aide.attributes('-fullscreen', True)  # On met la fenêtre en plein écran
    # Juste en dessous on crée et on place la zone de texte qui servira de titre à notre page
    Bienvenue = Label(aide, text="Bienvenue dans le menu d'aide " + pseudoUser.get(), font=("Arial, 40"), bg='#CAAEF0', fg='white')
    Bienvenue.place(relx=0.5, rely=0.1, anchor=CENTER)
    # Ici on crée et place tous les textes qui expliquent les règles
    texteRegles = "Le jeu du pendu consiste à deviner un mot. Pour cela, il suffit de proposer des lettres une par une. Si la lettre se trouve dans le mot, \nle mot commence à se révéler. Si la lettre se trouve plusieurs fois dans le mot, la lettre sera révélée plusieurs fois. \nATTENTION ! si la lettre que vous choisissez ne se trouve pas dans le mot, un compteur d'erreurs se lance. \nLa partie se termine de deux façons: Si vous trouvez toutes les lettres du mot, vous remportez la partie, sinon, si le nombre \nd'erreurs est trop élevé, vous avez perdu."
    reglesDuJeu = Label(aide, text="Règles du jeu du Pendu:", font="Arial, 40", bg='#CAAEF0', fg='white')
    reglesDuJeu.place(relx=0.1, rely=0.2)
    explicationRegles = Label(aide, text=texteRegles, font="Arial, 20", justify=LEFT, bg='#CAAEF0', fg='black')
    explicationRegles.place(relx=0.1, rely=0.27)
    texteChoixDiff = "Le choix de la difficulté va influer sur le score final ainsi que sur le nombre d'erreurs possibles. Il existe 4 niveaux de difficulté: \n- Facile: Vous pourrez vous tromper de lettres au maximum 8 fois. Chaque erreur enlève 2 points au score final et chaque seconde \nécoulée enlève 1 point.\n- Moyen: Vous pourrez vous tromper de lettre au maximum 6 fois. Chaque erreur enlève 3 points au score final et chaque seconde \nenlève 1 point.\n- Difficile: Vous pourrez vous tromper de lettre au maximum 4 fois. Chaque erreur enlève 5 points au score final et chaque seconde \nenlève 1 point.\n- M. Colin Mode: Vous pourrez vous tromper de lettre au maximum 2 fois. Chaque erreur enlève 10 points au score final et chaque \nseconde enlève 2 point."
    reglesChoixDiff = Label(aide, text="Le choix de la difficulté:", font="Arial, 40", bg='#CAAEF0', fg='white')
    reglesChoixDiff.place(relx=0.1, rely=0.45)
    explicationChoixDiff = Label(aide, text=texteChoixDiff, font="Arial, 20", justify=LEFT, bg='#CAAEF0', fg='black')
    explicationChoixDiff.place(relx=0.1, rely=0.52)
    # En dessous, on crée le bouton qui permettra de retourner à la page précédente
    boutonRetour = Button(aide, text="Retour", width=17, height=5, fg="#CAAEF0", bg="#FFFFFF", font=("Arial, 10"), command=fonctionRetour)
    boutonRetour.place(relx=0, rely=0, anchor=NW)

    aide.mainloop()  # C'est cette instruction qui permet de lancer la page d'aide

############################################################# Page WordList #############################################################
#### Cette page sert à la gestion des mots. On a la possibilité d'ajouter/supprimer un mot de la liste et aussi de visualiser les mots présents dans la liste

def ouvrirWordlist():  # Cette fonction ouvre la page de gestion des mots
    windows.withdraw()  # Elle cache la page principale
    wordList = Tk()  # Et déclare la page de gestion

    def fonctionRetourWordList():  # Cette fonction permet de retourner à la page principale grâce à un bouton retour
        wordList.withdraw()  # La fonction cache la page de gestion des mots
        windows.deiconify()  # Et réaffiche la page principale

    ###document xml
    def docXml():
        tab_xml.append(motAAjouter.get())##le tableau apprend le nouveau mot
        document = xml.dom.minidom.Document()##creation d'un document xml
        mot = document.createElement('mot')##creation d'un element xml

        ##parcours de la longueur du tableau pour pouvoir ajouter tout les mots  au document xml
        for i in range (len(tab_xml)):
            ajouter_Mot = document.createElement('Ajouter')
            ajouter_Mot.setAttribute('word', tab_xml[i])##permet de creer un element auquel on va lui affecter une valeur
            mot.appendChild(ajouter_Mot)##permet d'apprend a un element parent, un element enfant
            document.appendChild(mot)##permet au document d'apprendre l'element parent
            i = i+1
        ##va permettre d'ecrire le document xml dans le document que l'on creer
        with open('wordlist.xml', 'w') as out:
            document.writexml(out, encoding='utf-8')##ecriture du xml avec l'encodage utf-8

    ###permet de rafraichir la liste box a chaque fois qu'il y'a un changement
    def refresh():
        LB.delete(0, END)##permet de supprimer tous les elements de la list box

        ##va permettre de reinserer tous les element dans la list box avec les changements
        for i in range(len(tab_xml)):
            LB.insert(END, tab_xml[i])

    ##va permettre de supprimer un mot de la liste
    def deleteWord():
        M = LB.curselection()[0]##permet de donner l'index du mot viser avec le curseur
        item = LB.get(M)##permet de recuperer la valeur du mot a supprimer

        ##parcours du tableau pour pouvoir supprimer le mot que l'on souhaite
        for i in range (len(tab_xml)):
            if item == tab_xml[i]:
                tab_xml.remove(item)##permet de supprimer un element du tableau
        docXml()##appelle de la fonction docXml pour pouvoir réécrire le xml avec les changements

    wordList.config(bg='#CAAEF0')  # Couleur de fond de la page
    wordList.attributes('-fullscreen', True)  # Passage en mode plein écran

    ####creation des elements qui vont composer la page
    titrePageWordlist = Label(wordList, text="Gestion des mots", font=("Arial, 40"), bg='#CAAEF0', fg='white')
    titrePageWordlist.place(relx=0.5, rely=0.1, anchor=CENTER)
    soustitrePageWordlist = Label(wordList, text="Sur cette page, vous pouvez ajouter vous-même des mots dans la liste afin d'avoir plus de mots différents à deviner.", font=("Arial, 20"), bg='#CAAEF0', fg='white')
    soustitrePageWordlist.place(relx=0.5, rely=0.20, anchor=CENTER)
    ajoutMot = Label(wordList, text="Ecrivez ici le mot à ajouter dans la liste", font=("Arial, 14"), bg='#CAAEF0', fg='red')
    ajoutMot.place(relx=0.5, rely=0.30, anchor=CENTER)
    motAAjouter = Entry(wordList, font='Arial', fg='black')
    motAAjouter.place(relx=0.5, rely=0.35, anchor=CENTER)
    boutonValiderMot  =  Button(wordList , text = "Ajouter le mot" , width = 20 , height = 2 , bg = "#FFFFFF", command = docXml)
    boutonValiderMot.place(relx=0.65, rely=0.40, anchor=CENTER)
    boutonEnregistrerMot  = Button(wordList, text = "Enregistrer" , width = 20, height = 2, bg = "#FFFFFF", command = refresh)
    boutonEnregistrerMot.place(relx=0.65, rely=0.50, anchor=CENTER)
    boutonSupprimerMot  = Button(wordList, text = "Supprimer" , width = 20, height = 2, bg = "#FFFFFF", command = deleteWord)
    boutonSupprimerMot.place(relx=0.65, rely=0.45, anchor=CENTER)
    boutonRetourWordlist = Button(wordList, text="Retour", width=17, height=5, fg="#CAAEF0", bg="#FFFFFF", font=("Arial, 10"), command=fonctionRetourWordList)
    boutonRetourWordlist.place(relx=0, rely=0, anchor=NW)
    LB = Listbox(wordList)  ##creation de la list box

    ##parcours du tableau pour pouvoir creer la list box de base sans changement encore
    for i in range (len(tab_xml)):
        LB.insert(END, tab_xml[i])
    LB.place(relx=0.5, rely=0.5, anchor=CENTER)
    wordList.mainloop()

############################################################# Page Top #############################################################
### Cette page affiche le classement des meilleurs joueurs en fonction de chaque niveau de difficulté

def ouvrirTop():  # Fonction permettant d'ouvrir la page de classement
    windows.withdraw()  # On cache la fenêtre principale
    pageTop = Tk()  # On déclare la fenêtre de page d'aide

    def fonctionRetourTop():  # Fonction pour le bouton "Retour"
        pageTop.withdraw()  # On cache la page d'aide
        windows.deiconify()  # Et on réaffiche la page principale

    pageTop.config(bg='#CAAEF0')  # Couleur de fond de la page
    pageTop.attributes('-fullscreen', True)  # On met en plein écran
    # Création et placement du bouton permettant de retourner à la page principale
    boutonRetourTop = Button(pageTop, text="Retour", width=17, height=5, fg="#CAAEF0", bg="#FFFFFF", font=("Arial, 10"), command=fonctionRetourTop)
    boutonRetourTop.place(relx=0, rely=0, anchor=NW)
    # Création et placement du texte qui servira de titre à notre page
    maintenance = Label(pageTop, text="En maintenance...", font=("Arial, 40"), bg='#CAAEF0', fg='white')
    maintenance.place(relx=0.5, rely=0.1, anchor=CENTER)

    pageTop.mainloop()  # Génération de la page et affichage

############################################################# Page Jouer #############################################################


def verifNom(): # Fonction qui permet de lancer le jeu après quelques vérifications
    global tentatives, lettres_trouvees,valeurDiff
    valeurNom = pseudoUser.get()  # On récupère le pseudo entré par l'utilisateur
    valeurDiff = choixDifficulte.get()  # Ainsi que le niveau de difficulté selectionné

    if(len(valeurNom) == 0 or valeurDiff == "--sélectionner une difficulté--"):  # On vérifie qu'un nom est entré ET qu'un niveau de difficulté est sélectionné
        warningPseudo.config(fg='red')  # Si ce n'est pas le cas, on met la couleur du texte indiquant d'entrer son nom en rouge
        warningDifficulte.config(fg='red')  # Et aussi celui du choix de la difficulté
    else:  # Si les champs sont remplis correctement, le jeu démarre
        windows.withdraw()  # On cache la page principale
        pageJeu = Tk()  # On déclare la page jeu
        limite = 0  # On fixe ici une limite pour la partie

        secret = random.choice(tab_xml).upper()
        if(valeurDiff == "facile"):  # La limite change en fonction de la difficulté choisie
            limite = 9
        elif(valeurDiff == "moyen"):
            limite = 7
        elif(valeurDiff == "difficile"):
            limite = 5
        else:
            limite = 3

        def tick():  # Cette fonction permet de lancer le timer déclaré précédemment
            global sec
            if not doTick:
                return
            sec += 1  # On ajoute 1 à sec toutes les 1000ms (soit 1s)
            time['text'] = sec
            time.after(1000, tick)
        # Création et placement de tout ce qui sert à afficher le timer sur la page de jeu
        time = Label(pageJeu, width=8, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 40")
        time.place(relx=0.5, rely=0.1, anchor=CENTER)
        temps = Label(pageJeu,text="Temps:", width=6, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 40")
        temps.place(relx=0.42, rely=0.1, anchor=CENTER)
        tempsSecondes = Label(pageJeu, text="s", width=2, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 40")
        tempsSecondes.place(relx=0.54, rely=0.1, anchor=CENTER)
        tick()

        def stop():  # Cette fonction permet d'arrêter le timer
            global doTick
            doTick = False

        def fonctionRetourJeu():  # Fonction pour le bouton "Retour"
            global cpt
            pageJeu.withdraw()  # On cache la page jeu
            windows.deiconify()  # On remontre la page principale
            warningPseudo.config(fg='green')  # On remet les indications pour mettre un pseudo et une difficulté valide en vert
            warningDifficulte.config(fg='green')
            cpt = 0  # On réinitialise le compteur d'erreurs

        pageJeu.config(bg='#CAAEF0') # Couleur de fond de la page
        pageJeu.attributes('-fullscreen', True) # Plein écran
        # Création et placement du bouton permettant de retourner à la page principale
        boutonRetourJeu = Button(pageJeu, text="Retour", width=17, height=5, fg="#CAAEF0", bg="#FFFFFF", font="Arial, 10", command=fonctionRetourJeu)
        boutonRetourJeu.place(relx=0, rely=0, anchor=NW)

        def maj_mot_en_progres(mot_en_progres, lettre, secret):  # Cette fonction permet de vérifier si la lettre choisie par l'utilisateur se trouve dans le mot
            n = len(secret)  # On récupère la longueur du mot à trouver
            for i in range(n):  # En fonction de sa longueur, on parcours le mot
                if secret[i] == lettre:  # Si la lettre choisie se trouve dans le mot
                    mot_en_progres[i] = lettre  # On change l'affichage

        def score(lettre,secret):  # Cette fonction permet de gérer la fin de partie
            if lettre not in secret:  # Si la lettre choisie n'est pas dans le mot à trouver
                global cpt
                cpt = cpt + 1  # On ajoute 1 au compteur d'erreurs
                annonce["text"] = cpt  # Permet d'afficher la valeur du compteur pendant la partie
                if cpt >= limite:  # Lorsque la limite dépasse ou égalise la limite, l'utilisateur peut utiliser les boutons pour rejouer et quitter
                    boutonRejouer.config(state=NORMAL)  # On débloque l'accès à ces boutons
                    boutonQuitter.config(state=NORMAL)
                    stop()  # On arrête le timer
                    tab_temps.append(sec)  # On ajoute au tableau le temps qu'a mit l'utilisateur pour jouer
                    annonce["text"] = "Perdu !"  # On remplace le nombre d'erreurs de l'utilisateur par un message
                    boutonLettreA.config(state=DISABLED)  # Et on désactive tous les boutons du clavier numérique
                    boutonLettreB.config(state=DISABLED)
                    boutonLettreC.config(state=DISABLED)
                    boutonLettreD.config(state=DISABLED)
                    boutonLettreE.config(state=DISABLED)
                    boutonLettreF.config(state=DISABLED)
                    boutonLettreG.config(state=DISABLED)
                    boutonLettreH.config(state=DISABLED)
                    boutonLettreI.config(state=DISABLED)
                    boutonLettreJ.config(state=DISABLED)
                    boutonLettreK.config(state=DISABLED)
                    boutonLettreL.config(state=DISABLED)
                    boutonLettreM.config(state=DISABLED)
                    boutonLettreN.config(state=DISABLED)
                    boutonLettreO.config(state=DISABLED)
                    boutonLettreP.config(state=DISABLED)
                    boutonLettreQ.config(state=DISABLED)
                    boutonLettreR.config(state=DISABLED)
                    boutonLettreS.config(state=DISABLED)
                    boutonLettreT.config(state=DISABLED)
                    boutonLettreU.config(state=DISABLED)
                    boutonLettreV.config(state=DISABLED)
                    boutonLettreW.config(state=DISABLED)
                    boutonLettreX.config(state=DISABLED)
                    boutonLettreY.config(state=DISABLED)
                    boutonLettreZ.config(state=DISABLED)
            elif mot_en_progres == list(secret):  # OU alors, si le mot à trouver est découvert, la partie s'arrête aussi
                boutonRejouer.config(state=NORMAL)  # On change donc le statut des boutons rejouer et quitter
                boutonQuitter.config(state=NORMAL)
                stop()  # On arrête aussi le timer
                tab_temps.append(sec)  # On met dans le tableau le temps qu'a mit l'utilisateur pour réussir à trouver le mot
                print(calculScore())  # DEBUG pour afficher le score de l'utilisateur
                annonce.config(text="Bien joué !")  # On change le texte qui affichait le nombre d'erreurs
                boutonLettreA.config(state=DISABLED)  # Et on désactive aussi les boutons du clavier numérique
                boutonLettreB.config(state=DISABLED)
                boutonLettreC.config(state=DISABLED)
                boutonLettreD.config(state=DISABLED)
                boutonLettreE.config(state=DISABLED)
                boutonLettreF.config(state=DISABLED)
                boutonLettreG.config(state=DISABLED)
                boutonLettreH.config(state=DISABLED)
                boutonLettreI.config(state=DISABLED)
                boutonLettreJ.config(state=DISABLED)
                boutonLettreK.config(state=DISABLED)
                boutonLettreL.config(state=DISABLED)
                boutonLettreM.config(state=DISABLED)
                boutonLettreN.config(state=DISABLED)
                boutonLettreO.config(state=DISABLED)
                boutonLettreP.config(state=DISABLED)
                boutonLettreQ.config(state=DISABLED)
                boutonLettreR.config(state=DISABLED)
                boutonLettreS.config(state=DISABLED)
                boutonLettreT.config(state=DISABLED)
                boutonLettreU.config(state=DISABLED)
                boutonLettreV.config(state=DISABLED)
                boutonLettreW.config(state=DISABLED)
                boutonLettreX.config(state=DISABLED)
                boutonLettreY.config(state=DISABLED)
                boutonLettreZ.config(state=DISABLED)

        def calculScore():  # Cette fonction permet de calculer le score de l'utilisateur
            global cpt
            scoreTotal = 100  # En début de partie, le score est de 100
            nbErreurs = cpt  # On récupère le nombre d'erreurs qu'a fait l'utilisateur
            tempsRealise = tab_temps[0]  # Ainsi que le temps qu'il a mit
            if(valeurDiff == "facile"):  # On vérifie la difficulté que l'utilisateur à choisi puisque le score final dépend en grande partie de ça
                scoreTotal = scoreTotal - (nbErreurs * 2) - tempsRealise  # Le calcul des points est expliqué dans la page d'aide du jeu
            elif(valeurDiff == "moyen"):
                scoreTotal = scoreTotal - (nbErreurs * 3) - tempsRealise
            elif(valeurDiff == "difficile"):
                scoreTotal = scoreTotal - (nbErreurs * 5) - tempsRealise
            else:
                scoreTotal = scoreTotal - (nbErreurs * 10) - (tempsRealise * 2)

            return scoreTotal

        def choisir_lettre(event):  # Cette fonction permet de récupérer la lettre choisie puisque elle est appelée par tous les boutons
            mon_btn = event.widget  # Evenement lorsque le bouton est cliqué
            mon_btn.config(state=DISABLED)  # On désactive le bouton pour que l'utilisateur ne puisse sélectionner 2 fois la même lettre
            lettre = mon_btn["text"]  # Lettre récupère la valeur "text" du bouton
            maj_mot_en_progres(mot_en_progres,lettre,secret)  # On appelle une fonction 
            motATrouver["text"] = "".join(mot_en_progres) 
            score(lettre,secret)  # On appelle une seconde fonction


        mot_en_progres = list("*" * len(secret))  # Ceci permet de générer l'affichage du mot de manière masquée dans un tableau
        stars = "".join(mot_en_progres)  # Permet de transformer le tableau juste au dessus en chaîne de caractères

        # Création des 26 boutons du clavier numérique, avec leurs caractéristiques, leurs positions et aussi l'appel de la fonction "coisir-lettre" lorsque l'on clique sur le bouton
        boutonLettreA = Button(pageJeu, text="A", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreA.place(relx=0.275, rely=0.65, anchor=CENTER)
        boutonLettreA.bind("<Button-1>", choisir_lettre)
        boutonLettreB = Button(pageJeu, text="B", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreB.place(relx=0.475, rely=0.83, anchor=CENTER)
        boutonLettreB.bind("<Button-1>", choisir_lettre)
        boutonLettreC = Button(pageJeu, text="C", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreC.place(relx=0.375, rely=0.83, anchor=CENTER)
        boutonLettreC.bind("<Button-1>", choisir_lettre)
        boutonLettreD = Button(pageJeu, text="D", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreD.place(relx=0.375, rely=0.74, anchor=CENTER)
        boutonLettreD.bind("<Button-1>", choisir_lettre)
        boutonLettreE = Button(pageJeu, text="E", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreE.place(relx=0.375, rely=0.65, anchor=CENTER)
        boutonLettreE.bind("<Button-1>", choisir_lettre)
        boutonLettreF = Button(pageJeu, text="F", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreF.place(relx=0.425, rely=0.74, anchor=CENTER)
        boutonLettreF.bind("<Button-1>", choisir_lettre)
        boutonLettreG = Button(pageJeu, text="G", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreG.place(relx=0.475, rely=0.74, anchor=CENTER)
        boutonLettreG.bind("<Button-1>", choisir_lettre)
        boutonLettreH = Button(pageJeu, text="H", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreH.place(relx=0.525, rely=0.74, anchor=CENTER)
        boutonLettreH.bind("<Button-1>", choisir_lettre)
        boutonLettreI = Button(pageJeu, text="I", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreI.place(relx=0.625, rely=0.65, anchor=CENTER)
        boutonLettreI.bind("<Button-1>", choisir_lettre)
        boutonLettreJ = Button(pageJeu, text="J", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreJ.place(relx=0.575, rely=0.74, anchor=CENTER)
        boutonLettreJ.bind("<Button-1>", choisir_lettre)
        boutonLettreK = Button(pageJeu, text="K", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreK.place(relx=0.625, rely=0.74, anchor=CENTER)
        boutonLettreK.bind("<Button-1>", choisir_lettre)
        boutonLettreL = Button(pageJeu, text="L", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreL.place(relx=0.675, rely=0.74, anchor=CENTER)
        boutonLettreL.bind("<Button-1>", choisir_lettre)
        boutonLettreM = Button(pageJeu, text="M", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreM.place(relx=0.725, rely=0.74, anchor=CENTER)
        boutonLettreM.bind("<Button-1>", choisir_lettre)
        boutonLettreN = Button(pageJeu, text="N", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreN.place(relx=0.525, rely=0.83, anchor=CENTER)
        boutonLettreN.bind("<Button-1>", choisir_lettre)
        boutonLettreO = Button(pageJeu, text="O", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreO.place(relx=0.675, rely=0.65, anchor=CENTER)
        boutonLettreO.bind("<Button-1>", choisir_lettre)
        boutonLettreP = Button(pageJeu, text="P", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreP.place(relx=0.725, rely=0.65, anchor=CENTER)
        boutonLettreP.bind("<Button-1>", choisir_lettre)
        boutonLettreQ = Button(pageJeu, text="Q", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreQ.place(relx=0.275, rely=0.74, anchor=CENTER)
        boutonLettreQ.bind("<Button-1>", choisir_lettre)
        boutonLettreR = Button(pageJeu, text="R", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreR.place(relx=0.425, rely=0.65, anchor=CENTER)
        boutonLettreR.bind("<Button-1>", choisir_lettre)
        boutonLettreS = Button(pageJeu, text="S", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreS.place(relx=0.325, rely=0.74, anchor=CENTER)
        boutonLettreS.bind("<Button-1>", choisir_lettre)
        boutonLettreT = Button(pageJeu, text="T", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreT.place(relx=0.475, rely=0.65, anchor=CENTER)
        boutonLettreT.bind("<Button-1>", choisir_lettre)
        boutonLettreU = Button(pageJeu, text="U", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreU.place(relx=0.575, rely=0.65, anchor=CENTER)
        boutonLettreU.bind("<Button-1>", choisir_lettre)
        boutonLettreV = Button(pageJeu, text="V", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreV.place(relx=0.425, rely=0.83, anchor=CENTER)
        boutonLettreV.bind("<Button-1>", choisir_lettre)
        boutonLettreW = Button(pageJeu, text="W", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreW.place(relx=0.275, rely=0.83, anchor=CENTER)
        boutonLettreW.bind("<Button-1>", choisir_lettre)
        boutonLettreX = Button(pageJeu, text="X", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreX.place(relx=0.325, rely=0.83, anchor=CENTER)
        boutonLettreX.bind("<Button-1>", choisir_lettre)
        boutonLettreY = Button(pageJeu, text="Y", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreY.place(relx=0.525, rely=0.65, anchor=CENTER)
        boutonLettreY.bind("<Button-1>", choisir_lettre)
        boutonLettreZ = Button(pageJeu, text="Z", width=3, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 25", relief='ridge')
        boutonLettreZ.place(relx=0.325, rely=0.65, anchor=CENTER)
        boutonLettreZ.bind("<Button-1>", choisir_lettre)
        # Ici on indique le niveau de difficulté choisi par l'utilisateur
        niveauDiff = Label(pageJeu, text="Difficulté: " + valeurDiff, font="Arial, 20", bg='#CAAEF0', fg='#FFFFFF')
        niveauDiff.place(relx=0.02, rely=0.98, anchor=SW)
        # Ici, c'est l'affichage du mot de manière masquée ("**********")
        motATrouver = Label(pageJeu, text=stars, font="Arial, 80", bg='#CAAEF0', fg='#FFFFFF')
        motATrouver.place(relx=0.5, rely=0.30, anchor=CENTER)
        # Ici, on affiche le nombre d'erreurs commises par l'utilisateur ou alors le message de fin si il a gagné ou non
        annonce = Label(pageJeu, width=30, text=cpt, font="Arial, 30", bg='#CAAEF0', fg='#FFFFFF')
        annonce.place(relx = 0.5, rely=0.45, anchor=CENTER)

        def fonctionRejouer():  # Cette fonction s'exécute lorsque l'utilisateur appuie sur le bouton rejouer
            global cpt, sec, scoreTotal
            cpt = 0  # On remet le compteur d'erreurs à 0
            pageJeu.destroy()  # On détruit la page de jeu
            verifNom()  # On relance la page de jeu
            sec = 0  # On remet le timer à 0
            scoreTotal = 100  # On remet le score à 100
            tick()  # On relance le timer

        def fonctionQuitter():  # La fonction quitter s'exécute lorsque l'utilisateur clique sur le bouton quitter
            pageJeu.destroy()  # Cela détruit la page de jeu
        # Placement du bouton pour rejouer
        boutonRejouer = Button(pageJeu, text="Rejouer", width=10, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 20", relief='ridge', state=DISABLED, command=fonctionRejouer)
        boutonRejouer.place(relx=0.45 ,rely=0.52 , anchor=CENTER)
        # Placement du bouton pour quitter le jeu
        boutonQuitter = Button(pageJeu, text="Quitter", width=10, height=1, fg="#FFFFFF", bg="#CAAEF0", font="Arial, 20", relief='ridge', command=fonctionQuitter)
        boutonQuitter.place(relx=0.55, rely=0.52, anchor=CENTER)

        pageJeu.mainloop()  # Génération et affichage de la page de jeu


############################################################# Page Menu #############################################################

windows.config(bg='#CAAEF0')  # Couleur de fond de la page
windows.attributes('-fullscreen', True)  # Plein écran
# Création des différents boutons qui seront présents sur la page principale
boutonJOUER = Button(windows, text="JOUER", width=53, height=3, fg="#CAAEF0", bg="#FFFFFF", font="Arial, 10", command=verifNom, state=NORMAL)  # Création boutons + design
boutonTOP = Button(windows, text="Top 10", width=17, height=5, fg="#CAAEF0", bg="#FFFFFF", font="Arial, 10", command=ouvrirTop)
boutonWordlist = Button(windows, text="Liste des mots", width=17, height=5, fg="#CAAEF0", bg="#FFFFFF", font="Arial, 10", command=ouvrirWordlist)
boutonAide = Button(windows, text="Aide", width=17, height=5, fg="#CAAEF0", bg="#FFFFFF", font="Arial, 10", command=ouvrirAide)
boutonLeave =Button(windows, text="Quitter", width=53, height=3, fg="#CAAEF0", bg="#FFFFFF", font="Arial, 10", command=ouvrirLeave)
# Création d'un canvas permettant de placer une image sur la page
mon_canvas=Canvas(windows, bg="#CAAEF0", height=500, width=500, cursor='exchange', highlightthickness=0)  # IMAGE
mon_canvas.place(relx=0.30, rely=0.118, anchor=NW)  # Placement du canvas
mainPicture = PhotoImage(file="penduAccueil.png")  # Choix de l'image dans le canvas
mon_canvas.create_image(150, 150, image=mainPicture)
# Placement de tous les boutons sur la page principale
boutonJOUER.place(relx=0.5, rely=0.80, anchor=CENTER)
boutonTOP.place(relx=1.0, rely=1.0, anchor=SE)
boutonWordlist.place(relx=0.0, rely=1.0, anchor=SW)
boutonAide.place(relx=1.0, rely=0.0, anchor=NE)
boutonLeave.place(relx=0.5, rely=0.92, anchor=S)
# Création et placement du titre de la page
Titre = Label(windows, text="Jeu du Pendu", font="Arial, 60", bg='#CAAEF0', fg='white')
Titre.place(relx=0.58, rely=0.273, anchor=CENTER)
# Création et placement des éléments pour le nom et le choix de la difficulté
warningPseudo = Label(windows, text="Veuillez entrer un pseudo pour jouer", font="Arial, 14", bg='#CAAEF0', fg='green')
warningPseudo.place(relx=0.5, rely=0.50, anchor=CENTER)
textePseudo = Label(windows, text="Entrez votre pseudo")
pseudoUser = Entry(windows, font="Arial", fg='black')
pseudoUser.place(relx=0.5, rely=0.55, anchor=CENTER)
warningDifficulte = Label(windows, text="Veuillez sélectionner une difficulté", font="Arial, 14", bg='#CAAEF0', fg='green')
warningDifficulte.place(relx=0.5, rely=0.60, anchor=CENTER)
listeDifficulte = ['--sélectionner une difficulté--','facile', 'moyen', 'difficile', 'M. Colin Mode']
choixDifficulte = ttk.Combobox(windows, values=listeDifficulte, width=30, state='readonly')
choixDifficulte.current(0)
choixDifficulte.place(relx=0.5, rely=0.65, anchor=CENTER)

creditsCreateurs = Label(windows, text="Ce jeu du Pendu a été réalisé par Léo T. et Amaury D.", font="Arial, 14", bg='#CAAEF0', fg='#FFFFFF')
creditsCreateurs.place(relx=0.5, rely=0.98, anchor=CENTER)

windows.mainloop()  # Génération de la page principale dès le lancement du programme