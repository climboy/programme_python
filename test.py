annee = input("Saisissez une année: ")

annee = int(annee)

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 !=0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")

a = 5
if a >= 2:
    if a <= 8:
        print("a est dans l'intervalle.")
    else:
        print("a n'est pas dans l'intervalle.")

a = 0
a == 5

a > -8

a != 33.19

age = 21
majeur = False
if age >= 18:
    majeur = True
