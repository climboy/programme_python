"""module multipli contenant ma fonction table"""

def table(nb, max=10):
    """Foncion affichant ma table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
