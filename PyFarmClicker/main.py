from PyFarmClicker.maingame import *


class MAINMENU:
    def __init__(self):
        self.menu = Tk()
        self.menu.title("PyFarmClicker")
        self.menu.geometry("600x600")
        try:
            self.menu.iconbitmap(
                find_data_file("images/logo.ico"))
        except TclError:
            tkmessage.showwarning("Attention", "Vous avez supprimé le logo !")
            pass
        self.menu.resizable(False, False)
        gameTitle = Label(
            self.menu,
            text="PyFarmClicker",
            font=tkfont.Font(family="Helvetica", size=36, weight="bold"),
        )
        gameTitle.pack(anchor="n")
        play = Button(
            self.menu,
            text="Jouer",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=35,
        )
        play.pack(anchor="n", pady=10)

        play.bind("<Button-1>", self.onBtClick)
        self.menu.mainloop()

    def quit(self):
        """
        fonction permettant de quitter la fenêtre du menu principal
        :return:
        """
        self.menu.destroy()

    def onBtClick(self, event):
        """
        fonction executé lors de l'appuie sur l'un des boutons pour rediriger vers
        le mode avec le nombre de joueur(s) approprié(s)
        :param event:
        :return:
        """
        if str(event.widget) == ".!button":
            self.quit()
            MAINGAME()
