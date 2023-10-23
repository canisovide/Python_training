import tkinter as tk
import time


class ApplicationDeBase(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.buttonQuitter = None
        self.labelHoraire = None
        self.creer_label_horaire()

    def creer_label_horaire(self):
        heure = ""+time.strftime("%c")
        self.labelHoraire = tk.Label(self, text=heure)
        self.buttonQuitter = tk.Button(self, text="Quitter", fg="red", command=self.quit)
        self.labelHoraire.pack()
        self.buttonQuitter.pack()


app = ApplicationDeBase()
app.title("Application de Base")
app.mainloop()
