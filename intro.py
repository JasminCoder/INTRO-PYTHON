#para ejecutar terminal:
#mac: python3 + nombre archivo.py
#windows: python + nombre archivo.py o py + nombre archivo.py


#BOOLEANS
boolean = True #True o False "T" o "F" en mayusculas

#NUMERALES
num = 10
fl = 10.34 #float
#parseint() en JS el texto lo convertia en entero.   .round redondeaba
nuevo_float = float(num) #10.0
nuevo_entero = int(fl) #10

print(nuevo_float)
print(nuevo_entero)
print(round(fl)) #round(numero) redondeamos

import random #importamos una libreria llamada random
num_aleatorio = random.randint(2,5) #numero aleatorio entre 2 y 5
print(num_aleatorio)



#CADENAS O TEXTOS STRING
string = "ABCDEFG"
print("Este es el alfabeto", string) #la coma en automatico agrega un espacio
#imprime: Este es el alfabeto ABCDEFG

print("Este es el alfabeto"+string) #el + concatena las cadenas tal cual
#imprime: Este es el alfabetoABCDEFG

print("Este es el alfabeto", 10) #print("Este es un numero "+10)... + cree q quieres sumar
#imprime: Este es el alfabeto 10

print("Este es el alfabeto"+str(10)) #str(10) ->"10"... el 10 se pone como string para q los concatene y no intente sumar
#imprime: Estees el alfabeto10

print(f"este es el alfabeto {string}") #en vez de poner una coma o un + se puede usar llaves para concatenar
#imprime: Este es el alfabeto ABCDEFG...... "f" seria función

#print("Les presento a", nombre, ", le pueden llamar '", apodo, "'")
#print(f"Les presento a '{nombre}', le pueden llamar '{apodo}'") 
#lo mismo en ambos, para no confundirse al usar tantas comillas, se usan {}



#METODOS Q NOS PUEDEN SERVIR
string2 = "hola mundo! soy Elena de Troya y hoy es 5 de septiembre"
print(string2.title()) #Primera letra de cada palabra será mayúscula
print(string2.upper()) #Todas en mayúsculas
print(string2.lower()) #todas en minúsculas
print(string2.count('oy')) #regresa cuántos 'oy' hay en la cadena

string3 = "Elena!Juana!Pablo!Pedro"
print(string3.split('!')) #Enlistas y dividir mi cadena por cada '!' que haya
print(string2.find('Elena')) #Devuelve dónde comienza 'Elena'. Si ponemos "Elena" en mayusculas, regresa 16
#si ponemos "elena" con minuscula, Regresa -1 porque NO LO ENCONTRÓ. No lo encuentra pq es Case-sensitive
#Case-sensitive = reconoce mayusculas y minusculas



#TUPLA 
#Muy parecida a una lista con la diferencia q una vez q se le asigna un valor, este ya no se puede cambiar. Pueden tener
#mas de un tipo de dato
tupla = ("ABC", 10, 10.3, False)
#print(tupla[13])
#tupla[1] = 11


#LISTAS / ARRAY / ARREGLO
lista_vacia = []
lista_llena = ["Hugo", "Paco", "Luis"] #pocisiones: 0-> Hugo; 1 -> Paco; 2-> Luis
print(lista_llena[2]) #imprime luis
lista_llena[2] = "Donald"
print(lista_llena)
lista_llena.pop() #elimina el ultimo dato de la lista
print(lista_llena)
lista_llena.pop(0) #elimina el dato de la posicion indicada (cero)
print(lista_llena)
lista_llena.append("Mickey") #agrega un dato al final de la lista
print(lista_llena)

lista_mix = ["Texto1", "Texto2", 1, False, ["lista1", "Lista2"]] #se puede guardar diferentes tipos de valores
lista_nombres = ["Elena", "Juana", "Pedro"]
nuevo_lista = lista_llena + lista_nombres #sumar 2 listas
print(nuevo_lista)




#DICCIONARIOS -> OBJETOS EN JAVASCRIPT
diccionario_vacio = {}
diccionario = {"nombre": "Elena", "edad":30, "soltera": False, "hobbies": ["leer", "comer", "ver tv"]} 
#hobbies es una lista
diccionario['estatura'] = 1.67 #para agregar un dato
print(diccionario)
diccionario.pop('estatura') #Eliminamos por completo la propiedad
print(diccionario)
edad = diccionario.pop('edad') #Eliminamos de diccionario esa propiedad Y el valor lo asignamos a la variable
print(diccionario)
print(edad)




#para eliminar un dato especifico de una lista
lista_alumnas = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]



#¿Cómo eliminamos de la lista de cursos de Pedro MERN?
lista_alumnas[2]["cursos"].pop(2)
from pprint import pprint #Mas bonitas nuestras impresiones / imprime de una forma mas entendible
print(lista_alumnas)

