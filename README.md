# Das Rate das Alter Spiel

## Das Spiel

Aus einer Gruppe von Menschen wird das Alter (T) von einer Person (durch Zufall) bestimmt, welches erraten werden soll.

Das Programm braucht als Informationen 

a) nur den Altersbereich (min / max) oder 
b) die genaue Verteilung des Alters der Gruppe 

und berechnet nun die Wahrscheinlichkeiten für das gesuchte Alter an Hand der Ergebnisse des 
folgenden Spiels:

Eine Person zieht aus einer Urne, in der alle Altersangaben sind, zufällig ein Alter. Dieses Alter x steht dann zu dem Alter T in einer der folgenden Beziehungen:

- x < T
- x = T
- x > T

Nur diese Information, also "<", "=" oder ">" wird gespeichert (und im Programm unter D abgelegt). 
Das Programm gibt nun, auf Grundlage der Bayes-Regel, an, wie warscheinlich das Alter X jeweils auf Grundlage der angegebenen Daten (D) ist.

Dazu wird auf Grundlage von p(T) (also der a-priori Verteilung des Alters), p( D | T = x) (also der bedingten Wahrscheinlichkeit, dass D auftritt, wenn T der Wert x ist) und P(D) (also der totalen Wahrscheinlichkeit von D) die Werte von p(T = x | D) mit Hilfe der Bayes-Regel berechnet.
Der maximale Wert von p(T=x | D) liefert den *maximale Likelihood* und somit den (aktuell) wahrscheinlichsten Wert von T gegeben das (aktuelle) D.

## Idee

Die Idee zu diesem Spiel habe ich gehabt, nach dem ich das Buch [Bernoulli's Fallacy: Statistical Illogic and the Crisis of Modern Science](https://amzn.to/3ZBc8uv) von Aubrey Clayton gelesen habe. Die Idee und die Grundlagen dazu beschreibt er im Kaptil 1 (What is probability?) im Abschnitt "The subjective Interpretation" ab Seite 35 bis Seite 45.
