import array 

print ("Manejo de datos dentro de Python")
print ("Variables, Arreglos, cadenas de texto y tuplas")
print ()
print ("Variables ---")
variable=2022 

print(variable)

lenguaje='Python' 
# Recuerda que lenguaje='Python'  es diferente a Lenguaje='Python' , la L lo hace diferente
print(lenguaje)

universidad, year = 'Laboratorio financieo EAN', 2022
print(universidad, year)

texto1=texto2='Sarta de texto'
print(texto1,texto2) 

print ()
print ("******************")
print ("Arreglos ---")
arreglo=(10,20,30,40,50)    # Las posiciones siempre inician en 0
print(arreglo[0])
print(arreglo[1])
print ()
for p in range (0, 5):      #recorre el array posicion por posicion iniciando la 0
    print(arreglo[p])
print ()

print ("******************")
print ("Cadena de texto ---")
texto='Introduccion a Python' 
print(texto)
print (texto[0])    #imprime primer caracter de la cadena de texto
print (texto[-1])   #imprime ultimo caracter de la cadena de texto
print (texto[13:14])   #imprime ultimo caracter 13 de la cadena de texto
print ()


print ("******************")
print ("Tuplas ---")
# Simple coleccion de datos que no se pueden cambiar, luego de ser creados

personas  = ('rafael','john')    # Las posiciones siempre inician en 0
segmentos = (10,20,30,40,50)    # Las posiciones siempre inician en 0
vocales   = "a","e","i","o","u";
print(personas[0])  #primera persona
print(personas[1])  #segunda persona
print(len(personas))#numero de personas en la tupla

print ()
print ("Concatenando Tuplas")
print (personas+segmentos)
print ()
print(personas[1:])
print(segmentos[::-1])
print(vocales[1:3])



