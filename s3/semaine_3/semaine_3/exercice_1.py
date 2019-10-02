import time
"""
1. Coder une fonction pour calculer la somme des n premiers entiers
    1.a utiliser une fonction récursive
    1.b utiliser une fonction iterative (en utilisant une boucle)

2. Mésurer le temps d'éxécution pour les fonctions
    2.1 quel est la plus rapide pour n = 10, 100, 500, 990 ?
    2.2 essayez avec n = 1000
"""


def somme_n_rec(n: int):
    """
    Calcule la somme des n premiers entiers de façon récursif
    :param n: int
    :return: int
    """

    if n <= 1:
        return 1
    else:
        return n + somme_n_rec(n-1)






def somme_n_iter(n: int):
    """
    Calcule la somme des n premiers entiers de façon iteratif
    :param n: int
    :return: int
    """
    somme: int = 0
    for c in range(n+1):
        somme += c
    return somme








if __name__ == "__main__":
    for n in [10, 100, 500, 990,1000]:

        start = time.time()
        res_rec = somme_n_rec(n)
        end = time.time()
        print(start - end)

        start = time.time()
        res_iter = somme_n_iter(n)
        end = time.time()
        print(start - end)

        print("rec : %d -> %d" % (n, res_rec))
        print("iter : %d -> %d" % (n, res_iter))

        assert res_rec == res_iter

        print()
