"""App de creation de code python 3"""
#IMPORT
from tkinter import *
from tkinter.scrolledtext import *
import tkinter.simpledialog

#VARS ANS CONST
pass

#FONCT
pass

#CLASS
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


        self.okbutton = Button(self.toolsframe, text="OK", command=self.add_cmd)
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

        mainloop()

    def add_cmd(self, event=None):
        for i in self.sugg.curselection():
            m = MessageBox(i)
            print(m.get())
            self.lstcmd.append(i)
            print(self.sugg.get(i) + ' (id {0}) a ete ajoute dans la liste.'.format(i))

class PyBundler(object):
    """Classe du constructeur du projet .py à partir du projet .pycrea"""
    def __init__(self, data=None, file=None):
        "constructeur de la classe Bundler(). Arguments : data : les données et file, le fichier. Si il y a un fichier, il sera convertit en data."
        if data == None and not(file == None):
            with open(file, "r") as f:
                self.data = f.read()
        elif not(data == None) and file == None:
            self.data = data
        else:
            try:
                raise Exception
            except Exception as e:
                raise RuntimeError("Il faut au min et max un argument entre file et data !") from e


class MessageBox(object):
    def __init__(self, id):
        self.id = id

        self.root = Tk()
        self.root.title("Arguments pour l'element selectionne")

        if self.id == 0:
            self.id0()
        elif self.id == 1:
            self.id1()

        mainloop()

    def get(self):
        self.entree.get()

    def id0(self):
        Label(self.root, text="Choississez les valeurs pour l'agument 'texte' :").pack()

        Label(self.root, text="Choississez le type de l'argument :").pack()
        self.choose = StringVar()
        self.b1 = Radiobutton(self.root, text="Texte fixe", value="txt", variable=self.choose)
        self.b1.pack()

        self.b2 = Radiobutton(self.root, text="Variable personnalisée", value="var", variable=self.choose)
        self.b2.pack()

        Label(self.root, text="Choississez le nom de la variable ou le contenu du texte :").pack()
        self.entree = Entry(self.root, width=50)
        self.entree.pack()

        Button(self.root, text="OK").pack()



    def id1(self):
        pass

#MAIN
if __name__ == "__main__":
    a = App()