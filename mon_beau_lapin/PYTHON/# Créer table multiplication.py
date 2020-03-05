# Toutes les table de multiplication comprises entre 1 et 10
for i in range (1,11):
    for j in range (1,11):
        print (i * j)




# Demander à l'utilisateur quelle table il veut:
i=1
a=input("Saisissez la table que vous souhaitez voir: ")
while i<11:
    a=int(a)
    resultat=i*a
    print(str(a)+"x"+str(i)+"="+str(resultat))
    i+=1




# Demander à l'utilisateur quelle table il veut
num = int (input("Entrez un nombre: "))

print("Mutiplication de la table :", num)

for i in range(1,11):
    print(num, "X", i, "=", num * i)