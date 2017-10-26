from tkinter import *
from random import randrange



class Player:  # working ATM
    
    def __init__(self,name,dex,wits,celer,master):
        self.name = name
        self.dex = dex
        self.wits = wits
        self.celer = celer
        self.initiative = 0
        self.speed = self.celer + self.wits + self.dex
        self.master = master

    def add1speed(self):
        self.speed += 1
        self.master.populate_list()

    def sub1speed(self):
        self.speed -= 1
        self.master.populate_list()


    def add1init(self):
        self.initiative += 1
        self.master.populate_list()


    def sub1init(self):
        self.initiative -= 1
        self.master.populate_list()

    def add5init(self):
        self.initiative += 5
        self.master.populate_list()

    def sub5init(self):
        self.initiative -= 5
        self.master.populate_list()

    def add10init(self):
        self.initiative += 10
        self.master.populate_list()

    def sub10init(self):
        self.initiative -= 10
        self.master.populate_list()

    def action(self):
        self.initiative -= 50
        self.master.populate_list()

    def roll_init(self):
        self.initiative = randrange(1,51)
        self.master.populate_list()

    def die(self):
        self.name = 'Dead'
        self.speed = 0
        self.initiative = 0
        self.master.populate_list()






class Wind:

    def __init__(self,master):  # working ATM
        self.master=master
        self.players=[]
        self.players.append(Player('Round',0,0,5,self))
        self.init_window()


    def init_window(self):  # working ATM
        self.master.title("Initiative")
        self.init_addbutton()
        self.battle_buttons()
        self.player_canvas = Canvas(self.master, width = 700)
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
        self.players.append(Player(name,dex,wits,celer,self))
        self.populate_list()
        print(self.players) # this is to test add button
        # print(self.players['Jon'].initiative)


    def battle_buttons(self):
        self.battle_canvas = Canvas(self.master)
        self.battle_canvas.grid(row=1,column=0)

        self.battle_button = Button(self.battle_canvas, text="Initiative Sweep",command=self.init_pass)
        self.battle_button.grid(row=0,column=2)

    def populate_list(self):
        
        #pass   
        for i in range(0,len(self.players)):
            xloc = 0
            yloc = i*27           
            self.players[i].canvas = Canvas(self.player_canvas)
            self.players[i].canvas.configure(borderwidth = 2)
            self.player_canvas.create_window(xloc, yloc, anchor = NW, window=self.players[i].canvas)
            player_name = "Name: " + self.players[i].name
            player_speed = "Speed: " + str(self.players[i].speed)
            player_init = "Initiative: " + str(self.players[i].initiative)

            break1 = '  |  '
            break1L = Label(self.players[i].canvas, text = break1)
            break2L = Label(self.players[i].canvas, text = break1)
            break3L = Label(self.players[i].canvas, text = break1)
            break4L = Label(self.players[i].canvas, text = break1)
            break5L = Label(self.players[i].canvas, text = break1)

            if self.players[i].initiative > 50:
                self.players[i].canvas.configure(background='green')
            
            pname=Label(self.players[i].canvas, text = player_name)
            pname.grid(row=0,column=0)

            break1L.grid(row=0,column=1)

            pspeedadd1_button = Button(self.players[i].canvas, text = '+1', command = self.players[i].add1speed)
            pspeedadd1_button.grid(row=0,column=2)
            pspeed=Label(self.players[i].canvas, text = player_speed)
            pspeed.grid(row=0,column=3)
            pspeedsub1_button = Button(self.players[i].canvas, text = '-1', command = self.players[i].sub1speed)
            pspeedsub1_button.grid(row=0,column=4)

            break2L.grid(row=0,column=5)

            pinitadd10_button = Button(self.players[i].canvas, text = '+10', command = self.players[i].add10init)
            pinitadd10_button.grid(row=0,column=6)
            pinitadd5_button = Button(self.players[i].canvas, text = '+5', command = self.players[i].add5init)
            pinitadd5_button.grid(row=0,column=7)
            pinitadd1_button = Button(self.players[i].canvas, text = '+1', command = self.players[i].add1init)
            pinitadd1_button.grid(row=0,column=8)


            pinit=Label(self.players[i].canvas, text = player_init)
            pinit.grid(row=0,column=9)
            pinitsub1_button = Button(self.players[i].canvas, text = '-1', command = self.players[i].sub1init)
            pinitsub1_button.grid(row=0,column=10)
            pinitsub5_button = Button(self.players[i].canvas, text = '-5', command = self.players[i].sub5init)
            pinitsub5_button.grid(row=0,column=11)
            pinitsub10_button = Button(self.players[i].canvas, text = '-10', command = self.players[i].sub10init)
            pinitsub10_button.grid(row=0,column=12)

            break3L.grid(row=0,column=13)

            action_button = Button(self.players[i].canvas, text = 'Action', command = self.players[i].action)
            action_button.grid(row=0,column=14)

            break4L.grid(row=0,column=15)

            roll_button = Button(self.players[i].canvas, text = "Roll Initiative", command = self.players[i].roll_init)
            roll_button.grid(row=0,column=16)

            break5L.grid(row=0,column=17)

            drop_button = Button(self.players[i].canvas, text = "Dead", command = self.players[i].die)
            drop_button.grid(row=0,column=18)




    def init_pass(self):
        for i in range(0,len(self.players)):
            self.players[i].initiative += self.players[i].speed
            self.populate_list()







def main():

    
    mainwindow = Tk()
    disp_wind=Wind(mainwindow)

    mainwindow.mainloop()


if __name__=="__main__":
    main()