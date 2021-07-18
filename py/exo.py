
def exo1():
    nbcube= 0

    for i in range(1,17):
        print(i)
        nbcube = nbcube + (i*i*i)
        i=i+2
    print(nbcube)
    
nbPlayer = int(input())
totaleq1 = 0
totaleq2 = 0

for i in range(nbPlayer * 2):
   eq1 = int(input())
   eq2 = int(input())
   totaleq1 = totaleq1 +eq1
   totaleq2 = totaleq2 +eq2

if totaleq1 >totaleq2:
   print("L'équipe 1 a un avantage")
   print("Poids total pour l'équipe 1 : ",totaleq1)
   print("Poids total pour l'équipe 2 : ",totaleq2)
else:
   print("L'équipe 2 a un avantage")
   print("Poids total pour l'équipe 1 : ",totaleq1)
   print("Poids total pour l'équipe 2 : ",totaleq2)
   