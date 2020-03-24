import re
import tkinter.font as tkfont
import tkinter.messagebox as tkmessage
import tkinter.ttk as ttk
from functools import partial
from tkinter import *

from PyFarmClicker.plante import *


class MAINGAME:
    def __init__(self):
        self.game = Tk()
        self.game.title("PyFarmClicker")
        self.game.geometry("600x600")
        self.game.resizable(False, False)
        self.topframe = Frame(self.game)
        self.topframe.pack()
        self.pactole = Label(self.topframe, text="100 €")
        self.pactole.pack(side="left")
        self.saison = Label(self.topframe, text="Saison 1")
        self.saison.pack(side="right")
        self.diff = Label(self.topframe, text="")
        self.diff.pack(side="right")
        self.items = []
        self.frame = Frame(self.game)
        self.frame.pack()
        self.centerframe = Frame(self.game)
        self.centerframe.pack()
        self.centerbottomframe = Frame(self.game)
        self.centerbottomframe.pack()
        self.bottomframe = Frame(self.game)
        self.bottomframe.pack(side=BOTTOM)
        self.PriceLabel = ""
        self.listeCombobox = ""
        self.buyBt = ""
        plantes = Button(
            self.frame,
            text="Plantes",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=35,
        )
        plantes.pack(side="left")
        animaux = Button(
            self.frame,
            text="Animaux",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=35,
        )
        animaux.pack(side="left")
        finir = Button(
            self.bottomframe,
            text="Finir la saison",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=35,
        )
        finir.pack(side="bottom")
        plantes.bind("<Button-1>", self.onBtPlantesClick)
        animaux.bind("<Button-1>", self.onBtAnimauxClick)
        finir.bind("<Button-1>", self.onBtFinirClick)
        self.game.mainloop()

    def quit(self):
        """
        fonction permettant de quitter la fenêtre du menu principal
        :return:
        """
        self.game.destroy()

    def onBtPlantesClick(self, *_event):
        for child in self.centerframe.winfo_children():
            child.unbind("<Button-1>")
            child.destroy()
        for child in self.centerbottomframe.winfo_children():
            child.unbind("<Button-1>")
            child.destroy()
        LegumesBt = Button(
            self.centerframe,
            text="Légumes",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=20,
        )
        LegumesBt.pack(side="left")

        FleursBt = Button(
            self.centerframe,
            text="Fleurs",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=20,
        )
        FleursBt.pack(side="left")
        LegumesBt.bind("<Button-1>", self.onBtLegumesClick)
        FleursBt.bind("<Button-1>", self.onBtFleursClick)

    def onBtAnimauxClick(self, *_event):
        for child in self.centerframe.winfo_children():
            child.unbind("<Button-1>")
            child.destroy()
        for child in self.centerbottomframe.winfo_children():
            child.unbind("<Button-1>")
            child.unbind("<<ComboboxSelected>>")
            child.destroy()

    def onBtFinirClick(self, *_event):
        if not self.items:
            tkmessage.showwarning(
                "Attention", "Vous n'avez pas acheté de plantes et/ou d'animaux !"
            )
            return
        pactolenb = re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+", self.pactole["text"])
        pactolenb = float(f"{float(pactolenb[0]):.2f}")
        fashionflowercolor = getFashionFlowerColor()
        diff = 0
        for item in self.items:
            if isinstance(item, Fleur) and item.getCouleur() == fashionflowercolor:
                itemprice = item.vendre()
                pactolenb += float(itemprice) * 2
                diff = float(diff) + float(itemprice) * 2
            else:
                itemprice = item.vendre()
                pactolenb += itemprice
                diff = float(diff) + float(itemprice)
        self.pactole.configure(text=str(f"{pactolenb:.2f}") + " €")
        season = re.findall(r"[-+]?\d*\.?\d+|[-+]?\d+", self.saison["text"])
        season = int(season[0]) + 1
        self.saison.configure(text="Saison " + str(season))
        self.items.clear()
        if diff >= 0:
            self.diff.configure(text="+" + str(f"{diff:.2f}") + " €")
        else:
            self.diff.configure(text=str(f"{diff:.2f}") + " €")

    def onComboboxChange(self, typeCombo, *_event):
        if typeCombo == "legumes":
            for legume in Legumes:
                if legume.getNom() == self.listeCombobox.get():
                    self.PriceLabel["text"] = str(legume.getPrixAchat()) + " €"
        elif typeCombo == "fleurs":
            for fleur in Fleurs:
                if fleur.getNom() == self.listeCombobox.get():
                    self.PriceLabel["text"] = str(fleur.getPrixAchat()) + " €"

    def onBtLegumesClick(self, *_event):
        for child in self.centerbottomframe.winfo_children():
            child.unbind("<Button-1>")
            child.unbind("<<ComboboxSelected>>")
            child.destroy()
        self.listeCombobox = ttk.Combobox(
            self.centerbottomframe, values=getLegumesNames(), state="readonly"
        )
        self.listeCombobox.pack()
        self.listeCombobox.current(0)
        self.PriceLabel = Label(self.centerbottomframe, text="0.5 €")
        self.PriceLabel.pack()
        self.buyBt = Button(
            self.centerbottomframe,
            text="Acheter",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=20,
        )
        self.buyBt.pack(pady="10")
        self.listeCombobox.bind(
            "<<ComboboxSelected>>", partial(self.onComboboxChange, "legumes")
        )
        self.buyBt.bind("<Button-1>", partial(self.onBtBuyClick, "legumes"))

    def onBtFleursClick(self, *_event):
        for child in self.centerbottomframe.winfo_children():
            child.unbind("<Button-1>")
            child.unbind("<<ComboboxSelected>>")
            child.destroy()
        self.listeCombobox = ttk.Combobox(
            self.centerbottomframe, values=getFlowersNames(), state="readonly"
        )
        self.listeCombobox.pack()
        self.listeCombobox.current(0)
        self.PriceLabel = Label(self.centerbottomframe, text="2.0 €")
        self.PriceLabel.pack()
        self.buyBt = Button(
            self.centerbottomframe,
            text="Acheter",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=20,
        )
        self.buyBt.pack(pady="10")
        self.listeCombobox.bind(
            "<<ComboboxSelected>>", partial(self.onComboboxChange, "fleurs")
        )
        self.buyBt.bind("<Button-1>", partial(self.onBtBuyClick, "fleurs"))

    def onBtBuyClick(self, typeCombo, *_event):
        if typeCombo == "legumes":
            for legume in Legumes:
                if legume.getNom() == self.listeCombobox.get():
                    self.items.append(legume)
                    pactolenumber = re.findall(
                        r"[-+]?\d*\.?\d+|[-+]?\d+", self.pactole["text"]
                    )
                    pactolenumber[0] = float(pactolenumber[0])
                    pactolenumber = float(f"{pactolenumber[0]:.2f}")
                    if pactolenumber - legume.getPrixAchat() < 0:
                        tkmessage.showwarning(
                            "Attention", "Vous n'avez plus assez de flouz !"
                        )
                        break
                    pactolenumber -= legume.getPrixAchat()
                    self.pactole["text"] = str(f"{pactolenumber:.2f}") + " €"
        elif typeCombo == "fleurs":
            for fleur in Fleurs:
                if fleur.getNom() == self.listeCombobox.get():
                    self.items.append(fleur)
                    pactolenumber = re.findall(
                        r"[-+]?\d*\.?\d+|[-+]?\d+", self.pactole["text"]
                    )
                    pactolenumber[0] = float(pactolenumber[0])
                    pactolenumber = float(f"{pactolenumber[0]:.2f}")
                    if pactolenumber - fleur.getPrixAchat() < 0:
                        tkmessage.showwarning(
                            "Attention", "Vous n'avez plus assez de flouz !"
                        )
                        break
                    pactolenumber -= fleur.getPrixAchat()
                    self.pactole["text"] = str(f"{pactolenumber:.2f}") + " €"
