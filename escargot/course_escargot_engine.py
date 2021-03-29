import random
from time import sleep
import course_escargot


class escargot:
    def __init__(self, vitesse_base, FAT, popeye, redbull, MK, cardio, tp, esca1,esca2,esca3,esca4,esca5,esca6):
        self.vitesse_base = +5
        self.popeye
        self.redbull
        self.MK 
        self.cardio
        self.tp


    def popeye(self, vitesse_base):
        apparition = 0.03
        for apparition in random.randrange(0.0,1.0):
            
            if esca1 == apparition:
                return apparition == True
            else:
                return apparition == False
            
            if esca2 == apparition:
                return apparition == True
            else:
                return apparition == False
            
            if esca3 == apparition:
                return apparition == True
            else:
                return apparition == False
            
            if esca4 == apparition:
                return apparition == True
            else:
                return apparition == False
            
            if esca5 == apparition:
                return apparition == True
            else:
                return apparition == False
            
            if esca6 == apparition:
                return apparition == True
            else:
                return apparition == False

    def redbull(self,vitesse_base):
        apparition = 0.05
        if apparition in random.randrange(0,1):
            apparition = True
            for i in vitesse_base:
                i =  3
                vitesse_base = vitesse_base + 0.15
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
#if pour chaque escargot
        if esca1 == apparition:
            return True

