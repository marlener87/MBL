print(5+3)

a = 5
print(a)

b = 8.2
print(a + b)

a = 10
print(a)

a = b + 1
print(a)

c = 1
# c = c + 3
c += 3
print(c)

a, d = 2, 3 
print(a + d)

a = 5
b = 10
c = a
a = b
b = c
print(a)
print(b)
print(a, b)

print (type(1))

a = 1
print(type(a))

b = 1.0
print(type(b))

chaine = 'Nous l\'avons'
print(chaine)
print(type(chaine))

age = 10
print(type(age))
print(age)
age = str(age)
print(type(age))
print(age)
age = float(age)
print(type(age))
print(age)

age = input("Age : ")
print(type(age))
print(age)
age = str(age)
print(type(age))
print(age)
age = float(age)
print(type(age))
print(age)

age = int(input("Quel est votre âge ? "))
if age > 16:
    print("Vous avez plus de 16 ans :)")

age = int(input("Quel est votre âge ? "))
condition = age > 16
if condition:
    print(type(condition))

age = int(input("Quel est votre âge ? "))
condition = age > 16
print(type(condition))
if condition:
    print("Vous avez plus de 16 ans :)")
    
age = int(input("Quel est votre âge ? "))
condition = age > 16
print(type(condition))
if condition:
    print("Vous avez plus de 16 ans :)")
print(condition)

age = int(input("Quel est votre âge ? "))
condition = age > 16
print(type(condition))
if condition:
    print("Vous avez plus de 16 ans :)")
elif age < 0:
    print("Tu te moquerais pas de moi ?")
else:
    print("Tu es encore un peu jeune")
print("Au revoir")
print(condition)













