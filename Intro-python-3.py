print ("Manejo de Funciones en Python")
print ()


def saludar():
    print("Bienvenido, ")

def sumar(a,b):
    r=a+b 
    return r

def multiplicar(a,b):
    r=a*b 
    return r

def imprimir(alumno,edad):
    print("Alumno:", alumno)
    print("Edad:", edad)
    return;


alumno='Rafael'
saludar()
print(alumno)

a=10
b=3
resultado = sumar(a,b)
print(resultado)
resultado = multiplicar(a,b)
print(resultado)

print()
alumno = "Catalina"
edad = 20 
imprimir(alumno,edad)
