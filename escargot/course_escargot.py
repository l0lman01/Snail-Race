# La course d'excargots
 
from tkinter import *
from time import sleep
import random

def go():
    global x1, x2, x3, x4, x5, x6
    y = 1000
    while x1<1800 and x2<1800 and x3<1800 and x4<1800 and x5<1800 and x6<1800:
        x1 += 10.0
        can.coords(esca1, x1, y1)
        y = y1
        x2 += 10.0
        can.coords(esca2, x2, y2)
        y = y2
        x3 += 10.0
        can.coords(esca3, x3, y3)
        y = y3
        x4 += 10.0
        can.coords(esca4, x4, y4)
        y = y4
        x5 += 10.0
        can.coords(esca5, x5, y5)
        y = y5
        x6 += 10.0
        can.coords(esca6, x6, y6)
        y = y6
        sleep(0.05)  # délai de 1/100 de secondes
        can.update()
        return go()
    can.coords(vainqueur, 500, y)


 # liste puis tri puis index
 
class escargot:
    def __init__(self, vitesse_base, FAT, popeye, redbull, MK, cardio, tp, x1,x2,x3,x4,x5,x6):
        self.vitesse_base = +5
        self.popeye
        self.redbull
        self.MK 
        self.cardio
        self.tp


    def popeye(self, vitesse_base):
        apparition = 0.03
        for apparition in random.randrange(0.0, 1.0):
            sleep(1)
            if esca1 == apparition:
                x1 == 10.5
                return apparition == True
            else:
                return apparition == False
            
            if esca2 == apparition:
                x2 == 10.5
                return apparition == True
            else:
                return apparition == False
            
            if esca3 == apparition:
                x3 == 10.5
                return apparition == True
            else:
                return apparition == False
            
            if esca4 == apparition:
                x4 == 10.5
                return apparition == True
            else:
                return apparition == False
            
            if esca5 == apparition:
                x5 == 10.5
                return apparition == True
            else:
                return apparition == False
            
            if esca6 == apparition:
                x6 ==10.5
                return apparition == True
            else:
                return apparition == False

    def redbull(self,vitesse_base):
        esca = [x1,x2,x3,x4,x5,x6]
        apparition = 0.05
        random.choice(esca)
        if x1 == apparition:
            x1 = x1 + 11.5
            return apparition == True
        else:
            apparition = False
        
        if x2 == apparition:
            x2 = x2 + 11.5
            return apparition == True
        else:
            apparition = False
        
        if x3 == apparition:
            x3 = x3 + 11.5
            return apparition == True
        else:
            apparition = False

        if x4 == apparition:
            x4 = x4 + 11.5
            return apparition == True
        else:
            apparition = False

        if x5 == apparition:
            x5 = x5 + 11.5
            return apparition == True
        else:
            apparition = False

        if x6 == apparition:
            x6 = x6 + 11.5
            return apparition == True
        else:
            apparition = False
        
    
    def MK(self, vitesse_base):
        apparition = 0.1
        if apparition in random.randrange(0,1):
            apparition = True
            vitesse_base = 0
        else:
            apparition = False
        return sleep(2)

    def cardio(self,vitesse_base):
        apparition = 0.2
        if apparition in random.randrange(0.1):
            apparition = True
            vitesse_base = vitesse_base * 0.75
            return time.time(2)
        else:
            apparition = False
            return go()

    def tp(self):
        apparition = 0.01
        for apparition in random.randrange(0,1):
            apparition = True
            sleep(0)






def reinit():
    global x1, x2, x3, x4, x5, x6, y1, y2, y3, y4, y5, y6
    x1, y1  = 130, 75
    x2, y2  = 130, 225
    x3, y3  = 130, 375
    x4, y4  = 130, 525
    x5, y5  = 130, 675
    x6, y6  = 130, 825
    can.coords(esca1, x1, y1)
    can.coords(esca2, x2, y2)
    can.coords(esca3, x3, y3)
    can.coords(esca4, x4, y4)
    can.coords(esca5, x5, y5)
    can.coords(esca6, x6, y6)
    can.coords(vainqueur, 100, 1100)

x1, y1  = 130, 75
x2, y2  = 130, 225
x3, y3  = 130, 375
x4, y4  = 130, 525
x5, y5  = 130, 675
x6, y6  = 130, 825

fen = Tk()
fen.title("Course d'escargots")
can = Canvas(fen, width=1850, height=960, bg ='green')
can.pack(side=TOP, padx=5, pady=5)
b1 = Button(fen, text ='Nouvelle course', width=15, command=reinit)
b1.pack(side=LEFT)

b2 = Button(fen, text ='Partez !', width=15, command=go)
b2.pack(side=LEFT)

b3 = Button(fen, text ='Quitter', width=15, command=fen.quit)
b3.pack(side=RIGHT)


# décor
can.create_line(1800, 0, 1800, 900, width=5, fill="red") #ligne arrivé
can.create_line(250, 0, 250, 900, width=5, fill="blue") #ligne départ

can.create_line(0, 150, 1800, 150, width=5, fill="black")
can.create_line(0, 300, 1800, 300, width=5, fill="black")
can.create_line(0, 450, 1800, 450, width=5, fill="black")
can.create_line(0, 600, 1800, 600, width=5, fill="black")
can.create_line(0, 750, 1800, 750, width=5, fill="black")
can.create_line(0, 900, 1800, 900, width=5, fill="black")


# images
photo1 = PhotoImage(file ='snail.gif')
esca1 = can.create_image(x1, y1, image=photo1)

photo2 = PhotoImage(file ='snail 2.gif')
esca2 = can.create_image(x2, y2, image=photo2)

photo3 = PhotoImage(file ='snail 3.gif')
esca3 = can.create_image(x3, y3, image=photo3)

photo4 = PhotoImage(file ='snail 4.gif')
esca4 = can.create_image(x4, y4, image=photo4)

photo5 = PhotoImage(file ='snail 5.gif')
esca5 = can.create_image(x5, y5, image=photo5)

photo6 = PhotoImage(file ='snail 6.gif')
esca6 = can.create_image(x6, y6, image=photo6)

#photo7 = PhotoImage(file ='vainqueur.gif')
#vainqueur = can.create_image(100, 965, image=photo7) # en dehors de l'image

fen.mainloop()
fen.destroy()


#ouvrir tout le dossier