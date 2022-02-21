from AutobahnGrafik_SiebenSpuren import *
import random
import time


def neueSpur(Fahrbahnlänge, Geschwindigkeitsbegrenzung):
    a = [[0, 3, 0] for x in range(Fahrbahnlänge)] #3 damit die Autos nicht aus dem Stand aus anfahren
    a = GeschwindigkeitsbegrenzungEinführen(a, Geschwindigkeitsbegrenzung)
    return (a)

def neueFahrzeuge(Fahrbahn, AnzahlFahrzeuge):
    b = int(len(Fahrbahn) / AnzahlFahrzeuge)
    for i in range(AnzahlFahrzeuge):
        Fahrbahn[b * i][0] = 1
    return (Fahrbahn)

def AbstandzumVordermann(Spur, Autoindizes):
    a = len(Spur)
    counter = 0
    for i in range(1, a + 1):
        if (Autoindizes + i) % a == 0:
            return 100
        if Spur[(Autoindizes + i) % a][0] == 1:
            counter += 1
            return (counter)
        else:
            counter += 1

def Fahrbahnkopieren(Autobahn):
    return [Autobahn[x] for x in range(len(Autobahn))]

def nächsteZeiteinheit(Autobahn, p, vmax, Geschwindigkeitsbegrenzung):
    neueS = neueSpur(len(Autobahn), Geschwindigkeitsbegrenzung)
    for i in range(len(Autobahn)):
        if Autobahn[i][0] == 1:
            b = AbstandzumVordermann(Autobahn, i) - 1
            c = random.uniform(0, 1)
            d = p[Autobahn[i][1]]
            if Autobahn[i][1] != 0 and c <= d:  # Trödeln
                Autobahn[i][1] = Autobahn[i][1] - 1
            elif c > d and b > Autobahn[i][1] and Autobahn[i][1] < vmax and Autobahn[i][1] < Autobahn[i][
                2]:  # Schnellestmögliches Fahren
                Autobahn[i][1] = Autobahn[i][1] + 1

            if b < Autobahn[i][1]:  # Sicherheitsabstand
                Autobahn[i][1] = b
            if (i + Autobahn[i][1]) >= len(Autobahn):#sorgt dafür, dass Autos die Fahrbahn verlassen
                continue
            else:
                neueS[i + Autobahn[i][1]] = Autobahn[i]
    a = random.uniform(0, 1)#Wahrscheinlichkeit, dass ein neues Auto nach kommt
    if a >= 0.475:
        b = AbstandzumVordermann(Autobahn, 0) - 1
        if b != 0:
            neueS[0][0] = 1
            neueS[0][1] = min(b, neueS[0][2], vmax)
    return (neueS)

def AutosZählen(Autobahn, ersteZelle, letzteZelle):
    a = 0
    for i in range(ersteZelle, letzteZelle):
        if Autobahn[i][0] == 1:
            a += 1
    return (a)

def Höchstgeschwindigkeit(Dichte):
    # bestimmt die Höchstgeschwindigkeit eines Abschnittes anhand der Verkehrsdichte
    if Dichte == 0:
        return 100
    else:
        return ((int((1 / Dichte) - 1 )))

def neueGeschwindigkeitsbegrenzung(Autobahn):#Höchstgeschw. des letzten Abschnittes auf 10 gesetzt, da die Fahrbahn danach nicht bekannt ist.
    #berechnet die Dichte Autos/Zelle
    a = AutosZählen(Autobahn, 0, int(len(Autobahn) / 7)) / (len(Autobahn) / 7)
    b = AutosZählen(Autobahn, int(len(Autobahn) / 7), int(2 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    c = AutosZählen(Autobahn, int(2 * len(Autobahn) / 7), int(3 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    d = AutosZählen(Autobahn, int(3 * len(Autobahn) / 7), int(4 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    e = AutosZählen(Autobahn, int(4 * len(Autobahn) / 7), int(5 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    f = AutosZählen(Autobahn, int(5 * len(Autobahn) / 7), int(6 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    g = AutosZählen(Autobahn, int(6 * len(Autobahn) / 7), int(7 * len(Autobahn) / 7)) / (len(Autobahn) / 7)
    return ([Höchstgeschwindigkeit(b), Höchstgeschwindigkeit(c), Höchstgeschwindigkeit(d), Höchstgeschwindigkeit(e), Höchstgeschwindigkeit(f), Höchstgeschwindigkeit(g), 10])


def GeschwindigkeitsbegrenzungEinführen(a, Geschwindigkeitsbegrenzung):
    for i in range(len(a)):
        if i < len(a) / 7:
            a[i][2] = Geschwindigkeitsbegrenzung[0]
        elif i < 2*len(a) / 7:
            a[i][2] = Geschwindigkeitsbegrenzung[1]
        elif i < 3 * len(a) / 7:
            a[i][2] = Geschwindigkeitsbegrenzung[2]
        elif i < 4*len(a) / 7:
            a[i][2] = Geschwindigkeitsbegrenzung[3]
        elif i < 5*len(a) / 7:
            a[i][2] = Geschwindigkeitsbegrenzung[4]
        elif i < 6*len(a) / 7:
            a[i][2] = Geschwindigkeitsbegrenzung[5]
        elif i < len(a):
            a[i][2] = Geschwindigkeitsbegrenzung[6]
    return (a)


def Autobahn():
    Geschwindigkeitsbegrenzung = [10, 10, 10, 10, 10, 10, 10]
    # "Wie lange soll die Autobahn sein"
    a = 200  # 1/7 der Zellen
    # "Was ist die Höchstgeschwindigkeit der Fahrzeuge?"
    vmax = 7
    # "Was ist die Wahrscheinlichkeit, dass ein Auto trödelt?"
    p = [0.22, 0.2, 0.16, 0.13, 0.11, 0.08, 0.06, 0.05]
    Autobahn = neueSpur(a * 7, Geschwindigkeitsbegrenzung)
    #Anzahl der Fahrzeuge
    Autobahn = neueFahrzeuge(Autobahn, 200)

    window = Graphic(1400, 1000, a, a)
    window.showCars(Autobahn, Geschwindigkeitsbegrenzung)

    count = 0
    warten = 0
    while count < 1000:

        if warten == 1:
            if window._window.getKey() == "s":#s für starten
                warten = 0
        Geschwindigkeitsbegrenzung = neueGeschwindigkeitsbegrenzung(Autobahn)
        alteAutobahn = Fahrbahnkopieren(Autobahn)
        Autobahn = GeschwindigkeitsbegrenzungEinführen(Autobahn, Geschwindigkeitsbegrenzung)
        Autobahn = nächsteZeiteinheit(Autobahn, p, vmax, Geschwindigkeitsbegrenzung)
        window.setWhite(alteAutobahn, Autobahn)
        window.showCars(Autobahn, Geschwindigkeitsbegrenzung)
        if warten == 0:
            if window._window.checkKey() == "p":
                warten = 1
        time.sleep(0.1)
        count +=1

#Die Simulation pausiert duch Drücken von "p" und startet wieder durch Drücken von "s". Durch wiederholtes Drücken von "p" geht man nur einen Zeitschritt vorwärts
Autobahn()