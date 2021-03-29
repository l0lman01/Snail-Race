def go():
    global x1, x2, x3, x4, x5, x6
    y = 1000
    while x1<1800 and x2<1800 and x3<1800 and x4<1800 and x5<1800 and x6<1800:
        no = random.randint(1,6)
            x1 += random.randint(10,25)
            can.coords(esca1, x1, y1)
            y = y1
            x2 += random.randint(10,25)
            can.coords(esca2, x2, y2)
            y = y2
            x3 += random.randint(10,25)
            can.coords(esca3, x3, y3)
            y = y3
            x4 += random.randint(10,25)
            can.coords(esca4, x4, y4)
            y = y4
            x5 += random.randint(10,25)
            can.coords(esca5, x5, y5)
            y = y5
            x6 += random.randint(10,25)
            can.coords(esca6, x6, y6)
            y = y6
        sleep(0.05)  # délai de 1/100 de secondes
        can.update()
        return go()
    can.coords(vainqueur, 500, y)


#fonction recursive c'est enlevé le boucle while

def go():
    global x1, x2, x3, x4, x5, x6
    y = 1000
    while x1<1800 and x2<1800 and x3<1800 and x4<1800 and x5<1800 and x6<1800:
        no = random.randint(1,6)
        if no == 1:
            x1 += random.randint(10,25)
            can.coords(esca1, x1, y1)
            y = y1
        elif no == 2:
            x2 += random.randint(10,25)
            can.coords(esca2, x2, y2)
            y = y2
        elif no == 3:
            x3 += random.randint(10,25)
            can.coords(esca3, x3, y3)
            y = y3
        elif no == 4:
            x4 += random.randint(10,25)
            can.coords(esca4, x4, y4)
            y = y4
        elif no == 5:
            x5 += random.randint(10,25)
            can.coords(esca5, x5, y5)
            y = y5
        else:
            x6 += random.randint(10,25)
            can.coords(esca6, x6, y6)
            y = y6
        sleep(0.05)  # délai de 1/100 de secondes
        can.update()
        return go()
    can.coords(vainqueur, 500, y)