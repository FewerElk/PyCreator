from tkinter import *
from tkinter.scrolledtext import *
import tkinter.simpledialog

class MessageBox(object):
    response = ""
    response_type = ""
    def __init__(self, id):
        self.id = id

        self.root = Tk()
        self.root.attributes("-alpha", True)
        self.root.title("Arguments pour l'element selectionne")

        if self.id == 0:        #en cours de code.
            self.id0()
        elif self.id == 1:      #non codé et non testé
            self.id1()
        print("end of init of gui")
        self.root.mainloop()      #le fameux mainloop()
        print("end")

    def get(self):
        return (self.response, self.response_type)

    def id0(self):          #le bug est surement ici
        Label(self.root, text="Choississez les valeurs pour l'agument 'texte' :").pack()

        Label(self.root, text="Choississez le type de l'argument :").pack()
        self.choose = StringVar()
        self.choose.set("txt")
        self.b1 = Radiobutton(self.root, text="Texte fixe", variable=self.choose, value="txt", command=self.txt)
        self.b1.pack(anchor=W)

        self.b2 = Radiobutton(self.root, text="Variable personnalisée", variable=self.choose, value="var", command=self.var)
        self.b2.pack(anchor=W)

        self.b1.select()

        Label(self.root, text="Choississez le nom de la variable ou le contenu du texte :").pack()
        self.entree = Entry(self.root, width=50)
        self.entree.pack()

        Button(self.root, text="OK", command=self.ok).pack()

    def actualite(self):
        print("Actualisation")
        self.response = self.entree.get()
        print("Réponse : {0}".format(self.response))
        print("Réponse_type : {0}".format(self.response_type))

    def id1(self):
        pass

    def ok(self):
        self.actualite()
        self.root.destroy()

    def var(self):
        self.response_type = "var"

    def txt(self):
        self.response_type = "txt"