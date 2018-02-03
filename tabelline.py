from random import choice

print("tabelline 2,3,4,5,6,7,8,9,10")

incoraggiamenti=["esatto","bravo","favoloso","eccezionale"]

def traguardo(giustedifila):        
        if giustedifila==100:
            return("leggendario!!! (100)")
           
        elif giustedifila==75:
            return("epico (75)")

        elif giustedifila==50:
            return("mitico (50)")

        elif giustedifila==25:
            return("fantastico (25)")
        
        elif (giustedifila%5)==0:
            return("continua così"+" ("+str(giustedifila)+")")
            
        else:
            return(choice(incoraggiamenti))



lista=[]

for i in range(2,11):
    for a in range(2,11):
         domanda=str(i)+" x "+str(a)+" = "
         risultato=i*a
         nuovo_elemento = {"d" : domanda ,"r":risultato,"s":0}
         lista.append(nuovo_elemento)


        
giustedifila=0
while len(lista)>0 and giustedifila<100:
    k=choice(lista)
    risposta=input(k["d"])
    if int(risposta)==k["r"]:
        k["s"]=k["s"]+1
        if k["s"]==5:
            lista.remove(k)
        giustedifila=giustedifila+1
        print(traguardo(giustedifila))
        
    else:
        print("no la risposta giusta è",k["r"])
        k["s"]=0
        giustedifila=0
