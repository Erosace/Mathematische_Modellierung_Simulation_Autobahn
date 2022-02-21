from graphics import *#graphics.py ist eine Zeichenbibliothek


class Graphic:
    _window = None


    rechtecke = []
    upDown = None
    leftRight = None
    anzeigetafeln = None
    abschnitte = None

    anzeigesystem = ["" for x in range(14)]#die ersten 7 sind die Höchstgeschwindigkeit, die letzten 7 die Anzahl der Autos

    #eine Zeile in der Legende ist ca 17 hoch
    legende = [Rectangle(Point(35,15), Point(300,150)), Text(Point(70,25),"Legende"),Text(Point(46,45),"X"), Text(Point(57,45),"Y"),
               Text(Point(165,60),"X = erlaubte Höchstgeschwindigkeit"), Text(Point(112,75), "Y = Anzahl der Autos"),
               Text(Point(70,89), "7 = vmax"), Text(Point(88,105),"p = Pausieren"), Text(Point(77,120), "s = Starten"),
               Text(Point(70, 135), "Farbe(v):"),
               Rectangle(Point(110,130), Point(120,140)), Rectangle(Point(150,130), Point(160,140)), Rectangle(Point(190,130), Point(200,140)),
               Rectangle(Point(230,130), Point(240,140)),
               Text(Point(135, 135), "0,1"), Text(Point(175, 135), "2,3"), Text(Point(215, 135), "4,5"), Text(Point(255, 135), "6,7")]
    legende[1].setTextColor("blue")
    legende[2].setTextColor("red")
    legende[3].setTextColor("red")

    legende[10].setFill("red")
    legende[11].setFill("brown")
    legende[12].setFill("DodgerBlue4")
    legende[13].setFill("turquoise3")


    def __init__(self, windowWidth, windowHeight, leftRight, upDown):
        self.upDown = upDown
        self.leftRight = leftRight
        self._window = GraphWin("Autobahnsimulation", windowWidth, windowHeight, autoflush=False)

        # Ecken Breite berechnen:
        # 2 * eckeY + upDown * zellenHöhe = windowHeight
        # Aber eckeY muss auch genauso groß sein wie zellenHöhe, damit es gut aussieht
        # also 2 * zellenHöhe + upDown * zellenHöhe = windowHeight
        # zellenHöhe = windowHeight / (upDown + 2)
        # zellenBreite = windowWidth / (leftRight + 2)

        self.zellenHöhe = windowHeight / (leftRight + 2)
        self.zellenBreite = windowWidth / (upDown + 2)
        zellenHöhe = windowHeight / (leftRight + 2)#erspart Arbeit, ansonsten muss überall self. for jedem zellenHöhe/-Breite
        zellenBreite = windowWidth / (upDown + 2)

        # Autobahn in E-Schlangenform mit 200 Zellen, 7 Abschnitte, Fensterbreite 1400, Fensterhöhe 1000
        #erste obere Reihe
        for i in range(200):
            self.rechtecke.append(Rectangle(Point(zellenBreite + i * zellenBreite, 0), Point(zellenBreite + (i + 1) * zellenBreite, zellenHöhe)))
        #zweite Reihe (rechts,Knick)
        for i in range(40):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite, zellenHöhe + i * zellenHöhe), Point(windowWidth, zellenHöhe + (i+1) * zellenHöhe)))
        #zweite Reihe (Horizontale)
        for i in range(40,190):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite*(i-38), zellenHöhe + 39 * zellenHöhe), Point(windowWidth - zellenBreite*(i-39), zellenHöhe + (40) * zellenHöhe)))
        #zweite Reihe links
        for i in range(190,200):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite*(190-38), zellenHöhe + (39+i-190) * zellenHöhe), Point(windowWidth - zellenBreite*(190-39), zellenHöhe + (40+i-190) * zellenHöhe)))
        #dritte Reihe links
        for i in range(0,30):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite*(190-38), zellenHöhe + (39+i+10) * zellenHöhe), Point(windowWidth - zellenBreite*(190-39), zellenHöhe + (40+i+10) * zellenHöhe)))
        #dritte Reihe horizontal
        for i in range(30,180):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite*(190-38-(i-29)), zellenHöhe + (39+29+10) * zellenHöhe), Point(windowWidth - zellenBreite*(190-39-(i-29)), zellenHöhe + (40+29+10) * zellenHöhe)))
        #dritte Reihe rechts
        for i in range(180,200):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite, zellenHöhe + (39+29+10+i-180) * zellenHöhe), Point(windowWidth, zellenHöhe + (40+29+10+i-180) * zellenHöhe)))
        #vierte Reihe rechts
        for i in range(0,20):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite, zellenHöhe + (39+30+10+20+i) * zellenHöhe), Point(windowWidth, zellenHöhe + (40+30+10+20+i) * zellenHöhe)))
        #vierte Reihe horizontal
        for i in range(20,170):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite*(i-18), zellenHöhe + (39+29+10+20+20) * zellenHöhe), Point(windowWidth - zellenBreite*(i-19),  zellenHöhe + (40+29+10+20+20) * zellenHöhe)))
        #vierte Reihe links
        for i in range(170,200):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite*(190-38), zellenHöhe + (39+29+10+20+20+i-170) * zellenHöhe), Point(windowWidth - zellenBreite*(190-39),  zellenHöhe + (40+29+10+20+20+i-170) * zellenHöhe)))
        #fünfte Reihe links
        for i in range(0,10):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite*(190-38), zellenHöhe + (39+29+10+20+20+30+i) * zellenHöhe), Point(windowWidth - zellenBreite*(190-39), zellenHöhe + (40+29+10+20+20+30+i) * zellenHöhe)))
        #fünfte Reihe horizontal
        for i in range(10,160):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite*(190-38-(i-9)), zellenHöhe + (39+29+10+20+20+30+9) * zellenHöhe), Point(windowWidth - zellenBreite*(190-38-(i-10)), zellenHöhe + (40+29+10+20+20+30+9) * zellenHöhe)))
        #fünfte Reihe rechts
        for i in range(160,200):
            self.rechtecke.append(Rectangle(Point(windowWidth - zellenBreite, zellenHöhe + (39+29+10+20+20+30+9+i-160) * zellenHöhe), Point(windowWidth, zellenHöhe + (40+29+10+20+20+30+9+i-160) * zellenHöhe)))
        #sechste Reihe horizontal
        for i in reversed(range(200)):
            self.rechtecke.append(Rectangle(Point(zellenBreite+i*zellenBreite, windowHeight - zellenHöhe), Point(zellenBreite+(i+1)*zellenBreite, windowHeight)))
        #siebte Reihe links
        for i in reversed(range(leftRight)):
            self.rechtecke.append(Rectangle(Point(0, zellenHöhe + i * zellenHöhe), Point(zellenBreite, zellenHöhe + (i+1) * zellenHöhe)))

        self.anzeigetafeln = [Rectangle(Point(98 * zellenBreite, 2 * zellenHöhe), Point(106 * zellenBreite, 6 * zellenHöhe)),
                              Rectangle(Point(126 * zellenBreite, 47 * zellenHöhe), Point(134 * zellenBreite, 51 * zellenHöhe)),
                              Rectangle(Point(126 * zellenBreite, 68 * zellenHöhe), Point(134 * zellenBreite, 72 * zellenHöhe)),
                              Rectangle(Point(126 * zellenBreite, 124 * zellenHöhe), Point(134 * zellenBreite, 128 * zellenHöhe)),
                              Rectangle(Point(126 * zellenBreite, 152 * zellenHöhe), Point(134 * zellenBreite, 156 * zellenHöhe)),
                              Rectangle(Point(98 * zellenBreite, 194 * zellenHöhe), Point(106 * zellenBreite, 198 * zellenHöhe)),
                              Rectangle(Point(4 * zellenBreite, 96 * zellenHöhe), Point(12 * zellenBreite, 100 * zellenHöhe)),
                              Line(Point(102 * zellenBreite, 2 * zellenHöhe), Point(102 * zellenBreite, 6 * zellenHöhe)),
                              Line(Point(130 * zellenBreite, 47 * zellenHöhe), Point(130 * zellenBreite, 51 * zellenHöhe)),
                              Line(Point(130 * zellenBreite, 68 * zellenHöhe), Point(130 * zellenBreite, 72 * zellenHöhe)),
                              Line(Point(130 * zellenBreite, 124 * zellenHöhe), Point(130 * zellenBreite, 128 * zellenHöhe)),
                              Line(Point(130 * zellenBreite, 152 * zellenHöhe), Point(130 * zellenBreite, 156 * zellenHöhe)),
                              Line(Point(102 * zellenBreite, 194 * zellenHöhe), Point(102 * zellenBreite, 198 * zellenHöhe)),
                              Line(Point(8 * zellenBreite, 96 * zellenHöhe), Point(8 * zellenBreite, 100 * zellenHöhe))]

        self.abschnitte = [Rectangle(Point(0,0), Point(zellenBreite * 3, zellenHöhe * 3)), Line(Point((self.upDown + 2) * zellenBreite - 4 * self.zellenBreite, 4 * self.zellenHöhe), Point((self.upDown + 2) * zellenBreite, 0)),
                      Line(Point(48 * self.zellenBreite, 50 * zellenHöhe), Point(54 * self.zellenBreite, 50 * zellenHöhe)),
                      Line(Point((self.upDown + 2) * zellenBreite - 4 * self.zellenBreite, 99.5 * zellenHöhe), Point((self.upDown + 2) * zellenBreite, 99.5 * zellenHöhe)),
                      Line(Point(48 * self.zellenBreite, 149 * zellenHöhe), Point(54 * self.zellenBreite, 149 * zellenHöhe)),
                      Line(Point((self.upDown + 2) * zellenBreite - 4 * self.zellenBreite, (self.upDown + 2) * zellenHöhe - 4 * self.zellenHöhe), Point((self.upDown + 2) * zellenBreite, (self.upDown + 2) * zellenHöhe)),
                      Line(Point(0, (self.upDown + 2) * zellenHöhe), Point(4 * self.zellenBreite, (self.upDown + 2) * zellenHöhe - 4 * self.zellenHöhe))]

        self.abschnitte[0].setFill("black")

        #Initialisieren
        for x in self.rechtecke:
            x.setFill("white")
            x.setOutline("gray")
            x.draw(self._window)

        for x in self.legende:
            x.draw(self._window)

        for x in self.anzeigetafeln:
            x.draw(self._window)

        for x in self.abschnitte:
            x.draw(self._window)

    #Alles auf weiß zurücksetzen
    def clearAll(self):
        for x in self.rechtecke:
            x.setFill("white")
            x.setOutline("gray")
        for x in self.anzeigesystem:
            x.setTextColor("white")

    def getZellen(self):
        return len(self.rechtecke)

    def activateCar(self, zelle):
        if zelle < 0 or zelle >= self.getZellen():
            raise IndexError('Diese Zelle gibt es nicht!')
        self.rechtecke[zelle].setFill("red")

    def showCars(self, Autobahn,  geschwindigkeitsbegrenzung):
        for i in range(len(Autobahn)):
            if Autobahn[i][0] == 1:
                self.rechtecke[i].setFill(Farbe(Autobahn, i))

        self.anzeigesystem[0] = (Text(Point(100*self.zellenBreite, 4*self.zellenHöhe), "{}".format(geschwindigkeitsbegrenzung[0])))
        self.anzeigesystem[1] = (Text(Point(128*self.zellenBreite, 49*self.zellenHöhe), "{}".format(geschwindigkeitsbegrenzung[1])))
        self.anzeigesystem[2] = (Text(Point(128*self.zellenBreite, 70*self.zellenHöhe), "{}".format(geschwindigkeitsbegrenzung[2])))
        self.anzeigesystem[3] = (Text(Point(128*self.zellenBreite, 126*self.zellenHöhe), "{}".format(geschwindigkeitsbegrenzung[3])))
        self.anzeigesystem[4] = (Text(Point(128*self.zellenBreite, 154*self.zellenHöhe), "{}".format(geschwindigkeitsbegrenzung[4])))
        self.anzeigesystem[5] = (Text(Point(100*self.zellenBreite, 196*self.zellenHöhe), "{}".format(geschwindigkeitsbegrenzung[5])))
        self.anzeigesystem[6] = (Text(Point(6*self.zellenBreite, 98*self.zellenHöhe), "{}".format(geschwindigkeitsbegrenzung[6])))

        self.anzeigesystem[7] = (Text(Point(104*self.zellenBreite, 4*self.zellenHöhe), "{}".format(AutosZählen(Autobahn, 0,200))))
        self.anzeigesystem[8] = (Text(Point(132*self.zellenBreite, 49*self.zellenHöhe), "{}".format(AutosZählen(Autobahn,200,400))))
        self.anzeigesystem[9] = (Text(Point(132*self.zellenBreite, 70*self.zellenHöhe), "{}".format(AutosZählen(Autobahn,400,600))))
        self.anzeigesystem[10] = (Text(Point(132*self.zellenBreite, 126*self.zellenHöhe), "{}".format(AutosZählen(Autobahn,600,800))))
        self.anzeigesystem[11] = (Text(Point(132*self.zellenBreite, 154*self.zellenHöhe), "{}".format(AutosZählen(Autobahn,800,1000))))
        self.anzeigesystem[12] = (Text(Point(104*self.zellenBreite, 196*self.zellenHöhe), "{}".format(AutosZählen(Autobahn,1000,1200))))
        self.anzeigesystem[13] = (Text(Point(10*self.zellenBreite, 98*self.zellenHöhe), "{}".format(AutosZählen(Autobahn,1200,1400))))

        for i in range(len(geschwindigkeitsbegrenzung*2)):
            self.anzeigesystem[i].setSize(int(2.5*self.zellenHöhe)+1)
            self.anzeigesystem[i].draw(self._window)

    #färbt die Zellen weiß, welche auf der neuen Bahn nicht mehr belegt sind
    def setWhite(self, alteAutobahn, neueAutobahn):
        for i in range(len(alteAutobahn)):
            if alteAutobahn[i][0] != neueAutobahn[i][0]:
                self.rechtecke[i].setFill("white")
                self.rechtecke[i].setOutline("gray")
        for x in self.anzeigesystem:
            x.setTextColor("white")


def AutosZählen(Autobahn, ersteZelle, letzteZelle):
    a = 0
    for i in range(ersteZelle, letzteZelle):
        if Autobahn[i][0] == 1:
            a += 1
    return (a)

def Farbe(Autobahn, Zelle):
    a = Autobahn[Zelle][1]
    if a == 0 or a == 1:
        return("red")
    if a == 2 or a == 3:
        return("brown")
    if a == 4 or a == 5:
        return("DodgerBlue4")
    if a == 6 or a == 7:
        return("turquoise3")