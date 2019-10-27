# Exercice 1 : Un échiquier
print("Exercice 1")
for x in range(8):
    for y in range(16):
        if (x + y) % 2:
           print('#', end='')
        else:
           print('', end=' ')
    print()


# Exercice 2 : Matrix dans le terminal
print ("Exercice 2")
for i in range (0, 4):
    for j in range (0, 4):
        if i == j:
            print(1)
        else:
            print (0)
    print("------")


# Exercice 3 : Nombre paire
print ("Exercice 3")
n = float(input("entrer un motant "))
def paire (n):
    if not isinstance (n, int) :
        n = round(n)
    if n%2==0 : 
        return True
    else :
        return False

resultat = paire (n)
if resultat:
    print("paire")
else :
    print("impaire") 


# Exercice 4 : Vous avez dit factorielle
print("Exercice 4")
facto = 1 #initial value
n = int(input("Taper une valeur : "))
for i in range (1, n+1):
    facto = facto * i
print("Le factorielle de", n,  "est de", facto)

# Exercice 5 : Les tirets ca compte
print("Exercice 5")
txt = "La facture est de 15 euro --------."
x = txt.replace("-", "\_")
print(x)

# Exercice 6 : Entraînez-vous avec les tableaux
print("Exercice 6")
liste_de_courses =["eau", "lait", "pepito", "banane", "madelaine"]
print(liste_de_courses[0], liste_de_courses[-1], liste_de_courses[1])

# Exercice 7 : Le tableau d'un homme
print("Exercice 7")
user = [["mahyadine", "yassi", "34", "1984"], ["farid", "dz", "30", "2005"]]
def tableau(user):
    for i in range (len(user)):
        for j in range (len(user[i])):
            print (user[i][j])

tableau(user)

# Exercice 8 : Le max d'un tableau
print("Exercice 8")
liste = str([1, 5, 0, 15, 45, 99, "fariddz"])
print ("Le nombre le plus grand est ", max(liste))

# Exercice 9 : Une to do list
print("Exercice 9")
user = ""
liste = []
while user != "fin":
    liste.append(user)
    user = input("Ajouter une tache: " )
liste.pop(0)
print(liste)

