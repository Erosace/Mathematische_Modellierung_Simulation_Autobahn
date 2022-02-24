# Mathematische_Modellierung_Simulation_Autobahn
Für das Ausführen der Simulation wird die Grafikbibliothek graphics.py benötigt.

Der erste Teil der Simulation besteht aus der geschlossenen Fahrbahn:

  - Um die Simulation zu starten werden beide Dateien im Ordner benötigt.
  - Die Simulation startet mit dem Ausführen der Datei "einspurigeAutobahn_SiebenSpuren.py"
  - Möchte man die Größe des Fensters ändern, so kann man dies in der Methode "Autobahn()" tun:
    - Ändere die ersten zwei Werte der Variablen "window", bsp. Graphic(1200,1000,a,a) oder Graphic(1000,1400,a,a). Sie entsprechen dabei der Anzahl der Pixel (Breite, Höhe)
  - Die Simulation pausiert duch Drücken von "p" und startet wieder durch Drücken von "s"
  - Durch wiederholtes Drücken von "p" geht man nur einen Zeitschritt vorwärt

Der zweite Teil der Simulation funktioniert mit einer offenen Fahrbahn. Dabei hat sie die selben Eigenschaften, wie die Simulation zuvor.
ACHTUNG: Hier auch die neue Graphikdatei verwenden.
