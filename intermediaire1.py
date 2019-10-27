import math
# exercice 1 : Le nombre le plus grand
print ("excercice 1")

a = -7
b = 2
c = 34
d = 56

if a>b and a>c and a>d:
    print (a)
elif b>a and b>c and b>d:
    print (b)
elif c>a and c>b and c>d:
    print (c)
else:
    print (d)        

# ecercice 2 : Condition d'Age
print ("exercice 2")

age = int(input("Veuillez indiquer votre age "))
if age <=0:
    print ("Entrer un age réel")
if age >=21:
    print ("Accès autorisé")
if age%2 ==0:
    print ("Votre age est pair")
if math.sqrt(age).is_integer():
    print ("Votre age est carré")
else :
    print ("Veuiller entrer un nombre" )

# exercice 3 : Le nombre caché
print ("exercice 3")

number = 88
user = int(input("Insert number "))

while number != user:
    if number >  user:
        print ("Le nombre est petit")
    user = int(input("recommence"))    
    if number < user:
        print ("Le nombre est grand")
    user = int(input("recommence"))
if number == user:
    print ("Vous avez gagner")



# exercice 4 : Des nombres en boucles
print ("exercice 4 ")

for i in range(1, 101): #pour i allant de 1 a 100
    print (i)


# exercice 5 : Des nombres en boucle bis
print ("exercice 5")

for i in range(1, 101, 2): #pour i allant de 1 a 100 avec chiffre pair
    print (i)


# exercice 6 : Remplir la piscine 
print (" exercice 6")
def piscine (longueur, largeur, profondeur, debit):
    calcul1 = longueur*largeur*profondeur
    calcul2 = calcul1 / debit
    print ("le temps de remplissage est de {} min".format(calcul2))

piscine(100, 50, 3, 2)


#exercice 7 : Calcul de cercle
print ("exercice 7")
from math import pi
r = float(input("Taper le rayon du cercle : "))
perimetre = round(2*pi*r)
surface = round(pi*r**2)
print ("Le périmètre du cercle de rayon : ",r," est : {}".format(perimetre))
print ("La surface du cercle de rayon : ",r," est : {}".format(surface))

#exercice 8 : Une pyramide
print ("exercice 8")
pyramide = ["*","**","***","****","*****"]
for i in (pyramide):
    print(i)

#exercice 9 : Fizz buzz
print ("exercice 9")
for i in range (1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)





