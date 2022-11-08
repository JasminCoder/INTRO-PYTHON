#CONDICIONALES
#la identacion es muy importante.. Todo lo q quiero q se ejecute al cumplirse la condicion, debe estar 4 puntos mas adentro

x = 20
if x > 10:                 #primera condicional
    print("Mayor a 10")    #imprimir
    #x +=20                #i
else:
    print("Menor a 10")


if x < 10:                 #primera condicional
    print("Menor a 10")
elif x > 25:               #segunda condicional, si no se cumplió con la 1° ver si se cumple la 2°
    print("Mayor a 25")
else:
    print("Numero entre 10 y 25")



y = 2
if (y < 5 and x > 10):                    # 'and': ambas consicionales se deben cumplir.. and = a && en js
    print("Y menor a 5, X mayor a 10")
else:
    print("Alguna de las condicionales no se cumplió")
if(y < 5 or x > 10):                        # 'or' : una u otra de las condiciones se debe cumplir
    print("Alguna de las 2 SI se cumplió")
else:
    print("Ninguna de las condicionales se cumplió")


if x < 5:
    print("Menor a 5")


i = 10
if (i > 5 and i % 2 == 0 and i % 5 == 0):
    print("Se cumple con 3")              #se cumplen las 3 condiciones





    #BUCLES o CICLOS
for i in range(5): #del 0 al 4. Ya no entra en el 5,, pq lo toma como menor a 5,, no igual menor o igual a 5
    print(i)

print('----------') #linea divisora


for j in range(1, 5): #Rango del 1 al 4. Ya no entra en el 5, porq lo toma como menor a 5, no igual a 5
    print(j)

print('----------') #linea divisora


for k in range(0, 10, 2): #Comienzo, Parada, Cantidad a avanzar: Del 0 al 10 avanzar de 2 en 2. 
    print(k)              #El 10 lo toma como menor a 10, no igual, por eso no lo imprime


#Podemos recorrer textos
string = "Buenos días"
for letra in string:
    print(letra)          #imprime todas las letras del buenos dias


array = ['A', 'B', 'C', 'D']
#for(var i=0; i<array.length; i++){....... en JS seria asi
#   console.log(array[i])
#}
for elemento in array:
    print(elemento)




gastos = [10, 20, 30, 10]
total = 0
#total = 0
#gasto = 10
#total = 0 + 10 = 10

#gasto = 20
#total = 10 + 20 = 30

#gasto = 30
#total = 30 + 30 = 60

#gasto = 10
#total = 60 + 10 = 70
for gasto in gastos:
    total += gasto # total = total + gasto
print(total)




array = ['A', 'B', 'C', 'D']
for i in range(0, len(array)): #si quisieramos saber el indice o posicion de mi arreglo
    print(i, array[i])



#recorrer un diccionario
diccionario = {"nombre": "Elena", "apellido": "De Troya", "edad": 31}
for llave in diccionario:
    print(llave, diccionario[llave]) #imprime: nombre Elena, apellido De Troya....





y = 0
while y < 3:
    print(y)
    y += 1
else:
    print("Sentencia else final")



num = 1
while num < 15:
    print(num)
    num += 2
#else:
    #print("Ya no entra al ciclo porque el numero es", num) 
    #la primera vez q ya no se cumpla la condicion, imprimira esto
    #este else es opcional, solo si se quiere hacer algo luego q deja de cumplirse el if




#BREAK: es una interrupcion completa del bucle, es decir cuando nos encontramos con un break, el bucle deja de 
#ejecutarse x completo... Aplica para for y while

#CONTINUE: es una interrupcion de esa ronda del bucle. Cuando nos encontramos con un continue, el bucle ignora esa 
#ronda y continua la siguiente... Aplica para for y while


#RETO 1
#Dado un for y recorriendo del 1 al 15, imprime todos los número EXCEPTO aquellos múltiples de 5 - Break o Continue?
#for i in range(1, 15):
    #if(i % 5 == 0):
    #print(i)

for i in range(1, 16): #hasta el 16 pq no entra en el ultimo numero, ya q lo toma como menor a 15,, no igual
    if i % 5 == 0:
        continue       #para q continue despues de cumplirse la condicion
        print(i)




#RETO 2
#Dada una cadena, imprime cada uno de los caracteres y DETENTE cuando encuentres un . (punto)
#cadena1 = "Había una vez una niña. Esa niña quería aprender Python"

cadena1 = "Había una vez una niña. Esa niña quería aprender Python"
#for letra in cadena1:
    #if (cadena == .)
    #break
    #print(letra)
    
for letra in cadena1:
    if letra == ".":
        break
    print(letra)





#rango entre 1-100: cuando sea divisible entre 3 imprima pizza
#divisible entre 7 imprimir sandwich
#x = 1
#PRINT 1
#x = 2
#PRINT 2
#x = 3
#PRINT pizza
#x = 4
#PRINT 4
#x = 5
#PRINT 5
#x = 6
#PRINT pizza
#x = 7
#PRINT sandwich
#.......
for x in range(1, 101):                   #var x=1; x < 101; x++ ... asi lo veriamos en JS
    if x % 3 == 0:                        #primera condicion
        print("pizza")                        
    elif x % 7 == 0:                      #segunda condicion
        print("sandwich")
    else:
        print(x)


