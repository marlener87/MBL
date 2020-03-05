a = 42
def affichage():
    print(a)

affichage() # Affiche 42

def modifier(nombre):
    a = nombre
    print(a)
    
modifier(10)
print(a)




a = int(input("a:"))
b = int(input("b:"))
while b != 0:
    a, b = b, a%b
print(a)




i = 0
while i < 10:
    i += 1 # Pour ne pas avoir une boucle infinie
    if i%2 == 0: # Si i est pair
        continue
    print(i)




def affiche_menu():
    print("Menu :")
    print("* Action 1")
    print("* Action 2")
affiche_menu()




def dire(texte):
    print('# ' + texte)
dire('Bonjour') # Affiche `# Bonjour`
dire('Au revoir') # Affiche `# Au revoir`




def addition(a, b):
    return a + b
somme=addition(10, 5) 
# addition(10)
print(somme) # Renvoie 15




def saluer(nom):
    print('Bonjour ' + nom)

def saluerbis(nom = 'Visiteur'):
    print('Bonjour ' + nom)
saluerbis('Clem') # Affiche `Bonjour Clem`
saluerbis() # Affiche `Bonjour Visiteur`




# def saluer(nom):
#    print('Bonjour ' + nom)

def saluer(nom = 'Visiteur'):
    print('Bonjour ' + nom)

#saluer('Clem')
saluer('Clem') # Affiche `Bonjour Clem`
saluer() # Affiche `Bonjour Visiteur`




a = 42
def affichage():
    print(a)
affichage() # Affiche 42




a = 42
def change(valeur):
    global a   # variable globale
    a = valeur

print(a) # Affiche `42`
change(10)
print(a) # Affiche ... `10`




# fonction anonyme (lambda)
fonction = lambda a, b: a**b
print(fonction(2,3)) # Affiche 8




def test(f, a, b=None):
    if b != None:
        r = f(a, b)
    else:
        r = f(a)
    if r:
        print("Test passé avec succès :)")
    else:
        print("Echec du test :(")

pair = lambda a: a % 2 == 0
divise = lambda a, b: a % b == 0

test(pair, 6)
test(divise, 6, 3)




# commun.py
# N'oubliez pas l'encodage
def xor(a, b):
    return (a and not(b)) or (b and not(a))













