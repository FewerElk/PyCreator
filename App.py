#IMPORT
from tkinter import *
from tkinter.scrolledtext import *
import tkinter.simpledialog
import Messagebox as Msg

class App(object):
    """Classe de l'application"""
    def __init__(self, name="Nouveau projet PyCreator"):
        "constructeur de la classe App(). name : nom du projet."
        self.name = name
        self.lstcmd = []

        self.root = Tk()     #Création de la fenetre
        self.root.title("PyCreator | {0}".format(self.name))    #Création du titre

        self.searchframe = Frame(self.root)         #cadre pour la recherche d'action
        self.searchframe.pack(side=TOP)
        
        self.suggestframe = Frame(self.root)        #cadre pour les suggestions
        self.suggestframe.pack(side=LEFT)

        self.projectframe = Frame(self.root)        #cadre pour le projet
        self.projectframe.pack(side=LEFT)

        self.toolsframe = Frame(self.root)          #cadre pour les bouttons
        self.toolsframe.pack(side=LEFT)

        #########################BUTTONS#############################


        self.okbutton = Button(self.toolsframe, text="AJOUTER", command=self.add_cmd)
        self.okbutton.pack()

        self.delbutton = Button(self.toolsframe, text="SUPPRIMER")
        self.delbutton.pack()

        self.quitbutton = Button(self.toolsframe, text="QUITTER", command=self.root.destroy)
        self.quitbutton.pack()


        ######################AUTRES##################################

        self.search = Entry(self.searchframe, width=80)
        self.search.pack()

        self.LISTSUGG = ["Afficher le texte [texte] dans le terminal", 
        "Demander [texte] dans le terminal", 
        "Créer la variable [variable] avec la valeur [valeur]", 
        "Assembler le texte [texte] avec [texte]"]
        self.listsugg = StringVar(value=self.LISTSUGG)

        self.sugg = Listbox(self.suggestframe, listvariable=self.listsugg, width=50, height=20)
        self.sugg.pack()

        self.project = Listbox(self.projectframe, width=50, height=20)
        self.project.pack()

        self.root.mainloop()

    def add_cmd(self, event=None):
        for i in self.sugg.curselection():  #1 boucle seulemnt, c obligé. Sinon, c qu'il y a bug de logique
            print("---------Messagebox---------------")
            m = Msg.MessageBox(i)           #Exécuté normalement à vu d'oeil (?). Est censé s'arrêter quand la fenetre est fermée
            print("On est revenu à add_cmd, mais on va vers m.get()")
            print(m.get())              #NON exécuté en tant réel
            print("--------Fin de Messagebox---------")
            self.lstcmd.append(i)       #idem...
            print(self.lstcmd)
            print(self.sugg.get(i) + ' (id {0}) a ete ajoute dans la liste.'.format(i))