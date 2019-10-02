"""
1. Coder une fonction récursive pour tester si un élément x existe dans une liste L (a_liste)
    1.a Utiliser la fonction debug de PyCharm (step through) pour visualiser la quantité d'appels récursifs
    1.b Quelle est la complexité en temps dans le pire de cas ?


2. Coder une fonction récursive pour tester si un élément x existe dans une matrice A (a_matrice)
    2.a Utiliser la fonction debug de PyCharm (step through) pour visualiser la quantité d'appels récursifs
    2.b Quelle est la complexité en temps dans le pire de cas ?
"""


def recherche_rec(a_liste: list, x: int):
    """
    Fonction récursive pour vérifier si un élément existe dans une liste
    :param a_liste: liste avec des éléments (entiers)
    :param x: une clef de recherche
    :return: True si trouvé False sinon
    """

    if len(a_liste) == 0:
        print("False")
        return False
    elif a_liste[0] == x:
        print("True")
        return True
    else:
        return recherche_rec(a_liste[1:], x)










def recherche_mat_rec(a_matrice: list, x: int):
    """
    Fonction récursive pour vérifier si un élément existe dans une matrice
    :param a_matrice: matrice avec des éléments (entiers)
    :param x: une clef de recherche
    :return: True si trouvé False sinon
    """










if __name__ == "__main__":
    assert not recherche_rec([], 3)
    assert not recherche_rec([1], 3)
    assert recherche_rec([3, 1], 3)
    assert recherche_rec([1, 2, 3, 1], 3)
    assert not recherche_rec([1, 2, 1, 2], 3)

    # assert not recherche_mat_rec([], 3)
    # assert not recherche_mat_rec([[]], 3)
    # assert not recherche_mat_rec([[1]], 3)
    # assert recherche_mat_rec([[3], [1]], 3)
    # assert recherche_mat_rec([[1, 2], [3, 1]], 3)
    # assert not recherche_mat_rec([[1, 2], [1, 2]], 3)
