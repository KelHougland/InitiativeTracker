from tkinter import *
from random import randrange



class Player:  # working ATM
    
    def __init__(self,name,dex,wits,celer):
        self.name = name
        self.dex = dex
        self.wits = wits
        self.celer = celer
        self.initiative = 0
        self.speed = self.celer + self.wits + self.dex


def init_pass(adict):
    for player in adict:
        player.initiative += player.speed




class Wind:

    def __init__(self,master):  # working ATM
        self.master=master
        round_count = Player('Round',0,0,5)
        self.players={}
        self.players['Round']=round_count
        self.init_window()


    def init_window(self):  # working ATM
        self.master.title("Initiative")
        self.init_addbutton()
        self.battle_buttons()
        self.player_canvas = Canvas(self.master)
        self.player_canvas.grid(row=2,column=0)

    def init_addbutton(self):  # working ATM
        self.add_canvas = Canvas(self.master)
        self.add_canvas.grid(row=0,column=0)
       
        name_v=StringVar()
        self.name_entry = Entry(self.add_canvas, textvariable=name_v)
        self.name_entry.grid(row=0,column=0)
        name_v.set('Name')

        wits_v=StringVar()
        self.wits_entry = Entry(self.add_canvas, textvariable=wits_v)
        self.wits_entry.grid(row=0,column=1)
        wits_v.set('Wits')

        dex_v=StringVar()
        self.dex_entry = Entry(self.add_canvas, textvariable=dex_v)
        self.dex_entry.grid(row=0,column=2)
        dex_v.set('Dexterity')

        celer_v=StringVar()
        self.celer_entry = Entry(self.add_canvas, textvariable=celer_v)
        self.celer_entry.grid(row=0,column=3)
        celer_v.set('Celerity')

        self.create_button = Button(self.add_canvas,text='Add Player',command=self.add_player)
        self.create_button.grid(row=0,column=4)

    def add_player(self):  # working ATM
        if not self.name_entry.get() or self.name_entry.get()=='Name' or len(self.name_entry.get())==0:
            return None
        elif not self.dex_entry.get() or self.dex_entry.get()=='Dexterity' or len(self.dex_entry.get())==0 or not self.dex_entry.get().isdigit():
            return None
        elif not self.wits_entry.get() or self.wits_entry.get()=='Wits' or len(self.wits_entry.get())==0 or not self.wits_entry.get().isdigit():
            return None
        elif not self.celer_entry.get() or self.celer_entry.get()=='Celerity' or len(self.celer_entry.get())==0 or not self.celer_entry.get().isdigit():
            return None

        name = self.name_entry.get()
        dex = int(self.dex_entry.get())
        wits = int(self.wits_entry.get())
        celer = int(self.celer_entry.get())
        self.players[name]=Player(name,dex,wits,celer)
        self.players[name].initiative=randrange(1,51)
        self.populate_list()
        print(self.players.keys()) # this is to test add button
        # print(self.players['Jon'].initiative)

    def battle(self):
        pass

    def battle_buttons(self):
        self.battle_canvas = Canvas(self.master)
        self.battle_canvas.grid(row=1,column=0)

        self.battle_button = Button(self.battle_canvas, text="Fight!",command=self.battle)
        self.battle_button.grid(row=0,column=2)

    def populate_list(self):   
        for player in range(self.players):
            player.canvas = Canvas(self.player_canvas)
            self.player_canvas.create_window(0,0,window=player.canvas)
            name=Label(player.canvas,text=player.name)
            name.grid(row=0,column=0)
            # for each player, i need to list: name, speed, initiative 
            # for each player, i need buttons to effect player speed and initiative
            # for each player, i need an action button that subtracts 50 from initiative



def main():
    
    mainwindow = Tk()
    disp_wind=Wind(mainwindow)

    mainwindow.mainloop()


if __name__=="__main__":
    main()