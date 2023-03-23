#lista que se puede modicar 
lista = ["rodrigo", "xdd",True,1.74]

#tupla es datos que no se pueden modicar 
#tupla = ["rodrigo", "xdd",True,1.74]

#esto es valido
lista[3]= "maquinola"

#esto no 
#tupla[3]= "maquinola"



print(lista[3])

#acordarse que empieza del 0 al 3 en la lista se cuenta el 0 como en js 


#creando un conjuntos (set)
#la lista de conjunto no tiene duplicados osea agrego rodrigo de vuelta y lo anota una sola vez 

conjunto = {"rodrigo", "maquinaaxd",True, 1.75,"rodrigo"}

print(conjunto)


#creando un diccionario (dict)

diccionario = {
    "nombre" : "rodrigo",
    "apellido" : "martinez",
    "esta emocionado": True,
    "altura" : 1.74,
    "dato duplicado" : "rodrigo"
    
}


print(diccionario["apellido"])


