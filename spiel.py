"""
Spiel. Errate das Alter

a) Jeder im Raum schreibt sein Alter auf einen Zettel und wirft ihn in die Urne.
b) Jemand zieht einen Zettel. Das Alter x, welches gezogen wird soll erraten werden.
c) Nun wird n=20 mal aus der Urne (mit zurücklegen) gezogen und der neue Wert y
   mit dem Wert x verglichen. Es können drei mögliche Ergebnisse auftreten.
   x < y, x = y oder x > y.
   Die Ergebnisse "<", "=" und ">" werden notiert. (Und D eingetragen)
d) Dieses Programm wird auf Grundlage von T, Tn und D die Wahrscheinlichkeiten
   auf Grundlage der Regel von Bayes bestimmen.

"""
from fractions import Fraction
import matplotlib.pyplot as plt

T =  [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
Tn = [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1]
Tn = [ 2,  1,  1,  3,  0,  1,  2,  0,  1,  0,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2]
N = sum(Tn)

"""
T  = [1, 2, 3, 4, 5, 6]
Tn = [1, 1, 1, 1, 1, 1]
N = sum(Tn)
"""

D = ("<", ">", ">", ">") #, "=", "=", "<", ">", ">", "<",
#     "=", ">", ">", "<", ">", ">", ">", "=", "=", "<",
#     ">", "=", ">", ">", "=", "=", ">", "=", ">", "<")

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
    return [Fraction(x, N) for x in Tn]


def berechne_p_von_D_gegeben_T(D, T, Tn):
    """
    Berechne P(D | T = i) für alle i aus T und jedes d aus D

    :param D:
    :param T:
    :return: P(D | T = i) für alle i aus T
    """
    ret = []
    for i in range(0, len(T)):
        p = Fraction(1, 1)
        for d in D:
            # Für T = i bestimme p(d | T = i)
            g = sum(Tn[i+1:])
            l = sum(Tn[:i])
            e = Tn[i]
            if d == "<":
                p *= Fraction(l, N)
            if d == ">":
                p *= Fraction(g, N)
            if d == "=":
                p *= Fraction(e, N)
        ret += [p]
    return ret


def berechne_p_von_D(pT, pDT):
    """
    Berechne p(D), also die totale Wahrscheinlichkeit

    :return:
    """
    ret = Fraction(0, 1)
    for pt, pdt in zip(pT, pDT):
        ret += pt * pdt
    return ret


def berechne_p_von_T_gegeben_D(pT, pDT, pD):
    """
    Nutze die Bayes Formel um p(T | D) zu berechnen

    :param pT:
    :param pDT:
    :param pD:
    :return:
    """
    ret = []
    for pt, pdt in zip(pT, pDT):
        ret += [pt * pdt / pD]
    return ret


def main():
    """
    Hauptroutine
    """
    p_T = berechne_p_von_T(T, Tn)
    print("p(T) =", p_T)

    p_D_T = berechne_p_von_D_gegeben_T(D, T, Tn)
    print("p(D|T=i) =", p_D_T)

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


if __name__ == "__main__":
    main()
