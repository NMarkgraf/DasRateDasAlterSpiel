"""
Spiel. Errate das Alter!

    (C)opyright in 2023 by N. Markgraf (nmarkgraf@hotmail.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

a) Jeder im Raum schreibt sein Alter auf einen Zettel und wirft ihn in eine Urne.
b) Jemand zieht einen Zettel. Das Alter x auf diesem Zettel soll erraten werden.
c) Nun wird n(=20 ?) mal aus der Urne (mit zurücklegen) gezogen und der neue Wert y
   mit dem Wert x verglichen. Es können drei mögliche Ergebnisse auftreten.
   y < x, y = x oder y > x.
   Die Ergebnisse dieses Vergleichs ("<", "=" und ">") werden notiert. (Und hier unter D eingetragen!)
d) Dieses Programm wird auf Grundlage von T, Tn und D die Wahrscheinlichkeiten
   auf Grundlage der Regel von Bayes bestimmen.

"""
from fractions import Fraction
import matplotlib.pyplot as plt
""" 
    T gibt den Wertebereich an
"""
T =  (22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42)

"""
    Tn gibt an, wie oft der jeweilige Wert von T vorkommt
"""
# Keine a priori Annahme:
Tn = ( 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1)

# relative Häufigkeiten als a priori Annahme:
Tn = ( 2,  1,  1,  3,  0,  1,  2,  0,  1,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2)

"""
    N liefert die tatsächliche Anzahl an Werten
"""
N = sum(Tn)

"""
Beispiel für einen Würfel (W6) zum Testen:
"""
"""
T  = (1, 2, 3, 4, 5, 6)
Tn = (1, 1, 1, 1, 1, 1)
N = sum(Tn)
"""

"""
    In D speichern wir die Anfolge an "<", ">" und "=" aus den Vergleichen.
"""
D = ("<", ">", ">", ">", "=", "=", "<", ">", ">", "<",
     "=", ">", ">", "<", ">", ">", ">", "=", "=", "<",
     ">", "=", ">", ">", "=", "=", ">", "=", ">", "<")

def berechne_p_von_T(T, Tn):
    """
    Berechnet p(T) auf Grundlage des Alters T und das Anzahl Tn.
    p(T) ist hier die Wahrscheinlichkeit auf Grundlage der relativen
    Häufigkeit.

    :param T:
    :param Tn:
    :return: p(T), also die relative Häufigkeit von T=t auf Grundlage der relativen Häufigkeiten.
    """
    if len(T) != len(Tn):
        raise ValueError("!!!")
    return tuple(Fraction(x, N) for x in Tn)


def berechne_p_von_D_gegeben_T(D, T, Tn):
    """
    Berechne P(D | T = i) für alle i aus T und jedes d aus D

    :param D:
    :param T:
    :return: P(D | T = i) für alle i aus T
    """
    ret = []
    #for i in range(0, len(T)):
    for i, _ in enumerate(T):
        p = Fraction(1, 1)
        for d in D:
            # Für T = i bestimme p(d | T = i) und multipliziere die W'keiten in p
            if d == "<":
                p *= Fraction(sum(Tn[:i]), N)
            if d == ">":
                p *= Fraction(sum(Tn[i+1:]), N)
            if d == "=":
                p *= Fraction(Tn[i], N)
        # Erbebnis anhängen und nächstes T wählen
        ret += [p]
    return ret


def berechne_p_von_D(pT, pDT):
    """
    Berechne p(D), also die totale Wahrscheinlichkeit von D

    p(D) = p(T=1) * p(D | T=1) + p(T=1) * p(D | T=2) * ... * p(T=N) * p(D | T=N)

    :return: p(D)
    """
    ret = Fraction(0, 1)
    for pt, pdt in zip(pT, pDT):
        ret += pt * pdt
    return ret


def berechne_p_von_T_gegeben_D(pT, pDT, pD):
    """
    Nutze die Bayes-Regel um p(T | D) aus p(T), P(D) und P(D | T)zu berechnen:

    p(T | D) = p(T) * p(D | T)  / p(D)

    :param pT: p(T)
    :param pDT: p(D | T)
    :param pD: p(D)
    :return: p(T | D)
    """
    ret = []
    for pt, pdt in zip(pT, pDT):
        ret += [pt * pdt / pD]
    return ret


def show_p_von_T(pT):
    """
    Zeige p(T) als Säulendiagramm an

    :param pT: p(T)
    """
    ax = plt.subplot()
    ax.bar(T, pT)
    ax.set_ylabel('P(T)')
    ax.set_title('A priorie Wahrscheinlichkeiten von T')
    plt.show()

def show_p_von_D_von_T(pDT):
    """
    Zeige p(D | T) als Säulendiagramm an

    :param pT: p(T)
    """
    ax = plt.subplot()
    ax.bar(T, pDT)
    ax.set_ylabel('P(D | T)')
    ax.set_title('Wahrscheinlichkeiten von D gegeben T')
    plt.show()

def show_p_von_T_von_D(pTD, n=0):
    """
    Zeige p(T | D) als Säulendiagramm an

    :param pT: p(T)
    """
    ax = plt.subplot()
    ax.bar(T, pTD)
    ax.set_ylabel('P(T | D)')
    #ax.set_title('Wahrscheinlichkeiten von T gegeben D')
    if n > 0:
        ax.set_title(f'Wahrscheinlichkeiten von T gegeben D[0:{n}] auf Grundlage der Bayes-Regel')
    else:
        ax.set_title(f'Wahrscheinlichkeiten von T gegeben D auf Grundlage der Bayes-Regel')

    plt.show()


def main():
    """
        Hauptroutine
    """
    p_T = berechne_p_von_T(T, Tn)
    print("p(T) =", p_T)
    show_p_von_T(p_T)

    for i, _  in enumerate(D,1):
        d = D[:i]

        p_D_T = berechne_p_von_D_gegeben_T(d, T, Tn)
        print("p(D | T=i) =", p_D_T)
        #show_p_von_D_von_T(p_D_T)

        p_D = berechne_p_von_D(p_T, p_D_T)
        print("p(D) =", p_D)

        p_T_D = berechne_p_von_T_gegeben_D(p_T, p_D_T, p_D)
        print("p(T | D) =", p_T_D)

        p = [float(x) for x in p_T_D]
        print("p(T | D) =", p)

        show_p_von_T_von_D(p_T_D, i)

"""
    p_D_T = berechne_p_von_D_gegeben_T(D, T, Tn)
    print("p(D | T=i) =", p_D_T)
    show_p_von_D_von_T(p_D_T)

    p_D = berechne_p_von_D(p_T, p_D_T)
    print("p(D) =", p_D)
    

    p_T_D = berechne_p_von_T_gegeben_D(p_T, p_D_T, p_D)
    print("p(T | D) =", p_T_D)

    p = [float(x) for x in p_T_D]
    print("p(T | D) =", p)

    ax = plt.subplot()
    ax.bar(T, p_T_D)
    ax.set_ylabel('P(T = x | D)')
    ax.set_title('Wahrscheinlichkeiten mit Bayes auf Grundlage von D')
    plt.show()
"""

if __name__ == "__main__":
    main()
