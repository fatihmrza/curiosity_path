Pfadsuche auf Graphen (Greedy & Rekursiv) mit Laufzeitmessung
====================================================================

Überblick
---------
Es werden in diesem Programm zwei verschiedene Ansätze umgesetzt, um auf einem Graphen
einen möglichst guten Pfad vom Knoten „start“ zum Knoten „end“ zu finden:

- ein Greedy-Verfahren, das bei jeder Entscheidung den attraktivsten nächsten Schritt wählt,
- ein rekursiver Ansatz, der mehrere mögliche Wege betrachtet und diese anhand eines Verhältnisses
  aus Aufwand und Ablenkungswert bewertet.

Zusätzlich gibt es noch ein Modul zur Laufzeitmessung, das beide Verfahren
mithilfe von `time` und `timeit` miteinander vergleicht.

Projektstruktur
---------------

1) Hauptmodul (main)

   Dieses Modul dient als Einstiegspunkt für das Programm. Der Benutzer wählt, welcher Algorithmus ausgeführt werden
   soll.
   Dann werden der gefundene Pfad sowie die aufsummierten Kosten und Ablenkungswert ausgegeben.
   Modul-Docstring:
   "This module includes a main function to execute the algorithm"

2) apply_algorithm.py

   In dieser Datei befinden sich die eigentlichen Algorithmen zur Pfadberechnung.
   Sie greift auf die Graph-Struktur aus `Graph.py` und auf Bewertungsfunktionen
   aus `optimisation.py` zurück.

   Enthaltene Funktionen:
    - greedy_algo(graph, path1, path2):
      Vergleicht zwei mögliche Kanten anhand ihres prize-Wertes aus `graph.edges`
      und entscheidet sich für die günstigere Option.
    - greedy_progress(graph):
      Durchläuft den Graphen wiederholend von „start“ bis „end“ und trifft Entscheidungen
      mithilfe des Greedy-Prinzips. Daraus werden Pfad, Gesamtkosten und Gesamtablenkungswert zurückgegeben.
    - recursive_progress(graph, current_node, end_node, visited=None, cost=0, prize=0, paths=None):
      Baut Pfade nach dem rekursiven Ansatz auf, bis der Zielknoten erreicht ist. Hier wird zur Mehrzieloptimierung ratio_value() von
      optimisation.py implementiert.

3) Graph.py

   Dieses Modul stellt die Graph-Datenstruktur bereit.
   Modul-Docstring:
   "This module contains a class structure to define a graph"

   Zentrale Klasse:
    - Graph
        - nodes: enthält initial die Knoten ["start", "B", "C", "D", "E", "end"]
        - edges: Dictionary mit Kantendaten im Format ((node1, node2) → (cost, prize))
          Die Kanten sind doppelt gespeichert, da der Graph als ungerichtet modelliert ist.
          Methoden:
        - add_node(node): fügt einen neuen Knoten hinzu
        - add_edge(node1, node2, cost, prize): ergänzt eine Kante, sofern beide Knoten existieren

4) optimisation.py

   Dieses Modul macht den Vergleich und die Bewertung verschiedener Pfade.
   Modul-Docstring:
   "This module includes three algorithm functions for the optimise the specific structure"

   Enthaltene Funktionen:
    - ratio_value(r1, r2):
      Vergleicht zwei Pfade anhand des prize-/cost-Verhältnisses und berücksichtigt Sonderfälle
      wie `None` oder Division durch Null.
    - internal_comparison(p1, p2):
      Bevorzugt Pfade mit höherem prize, bei Gleichstand entscheidet die geringere cost.
    - score_cal(path, k1=0.35, k2=0.65):
      Berechnet einen gewichteten Score aus Aufwand und Ablenkungswert.

5) Laufzeitmessung (time / timeit)

   Dieses Modul vergleicht die Zeit der Algorithmen.
   Es werden `time` und `timeit` verwendet.
   P.s: Nach unserer eigenen Annahme haben wir Testdaten als die Angabe von sich ändernden Messungsdaten
   aufgefasst und deswegen in Kommentaren werden 3 Zeitmessungen von jeweiligen Algorithmen für 
   time und timeit Modul implementiert. Es wurde auch nochmal in Docstring erklärt.

   Enthaltene Funktionen:
    - time_measure(func, graph)
    - timeit_measure(func, graph)
    - algorithm_timing():
      Erstellt einen Graphen, misst die Laufzeiten von Greedy- und rekursivem Verfahren
      und gibt die Ergebnisse auf der Konsole aus.
      Hinweis:
      Doctests hier nur teilweise sinnvoll.

Doctests
--------
Mehrere Module enthalten Doctest-Abschnitte, die bei der Ausführung automatisch getestet werden. Bei der Laufzeitmessung
sind diese Tests teilweise
nur kommentiert vorhanden, weil die Ergebnisse unterschiedlich sind und dadurch zum Fail geführt wird. 
