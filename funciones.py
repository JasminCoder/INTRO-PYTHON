#FUNCION: es un blloquede codigo q nombraos y podemos ejecutar las veces q queramos, siempre y cuando la mandemos llamar

#DEF para definir la funcion/es "funcion" en JS
def hola():
    print("Hola a todos!") #siempre identada 1 adentro, pq estan dentro de la funcion
    print("Como estan?")

hola() #llamamos a la funcion




#funcion q sume 2 numeros
def sumatoria(a,b):          #quiero recibir 2 valores (A y B).. a = 1;  b = 2
    suma = a+b
    print(suma) 

sumatoria(1, 2)              #como quiero recibir 2 valores, envio 2 valores al llamar la funcion




#funcion con valor de retorno, me regresa algo
def sumatoriaReturn(a, b):   #a = 3; b = 4
    suma = a+b  #suma = 3 + 4 = 7
    return suma #regresa 7

sum = sumatoriaReturn(3, 4) #enviamos a sumatoriaReturn 3 y 4 y el valor q recibimos, 
#lo guardamos en una nueva variable sum.. sum = 7
print("La sumatoria recibida fue:", sum)
sum -= 1  #podemos manipular lo q recibimos (7)
print("Restandole 1 es", sum)




#RETO 1 - Crear una función llamada sumatoriaArray(arreglo) y regrese la sumatoria de todos los elementos del arreglo
#arreglo = [2, 3, 4, 5]
#total = 0
#num = 2
#total = total + num = 0 + 2 = 2

#num = 3
#total = 2 + 3 = 5

#num = 4
#total = 5 + 4 = 9

#num = 5
#total = 9 + 5 = 14

#return 14

def sumatoriaArray(arreglo):  #arreglo = [2, 3, 4, 5]
    total = 0

    for num in arreglo:
        total += num          #se identa una hacia adentro para q se ejecute dentro de for

    return total
    
total_sumatoria = sumatoriaArray([2, 3, 4, 5]) #llamar a la funcion y guardar el total en total_sumatoria = 14
print(total_sumatoria)




#RETO 2: Crear una función que reciba un arreglo y que me regrese el promedio de los elementos del arreglo.
#arreglo = [1, 2, 3]
#suma = 0
#num = 1
#suma = 0 + 1 = 1

#num = 2
#sum = 1 + 2 = 3

#num = 3
#sum = 3 + 3 = 6

#cant_promedio = 6 / 3 = 2
def promedio(arreglo):      #arreglo = [1, 2, 3]
    suma = 0

    for num in arreglo:       #suma todos los numeros
        suma += num

    cant_promedio = suma / len(arreglo)  #la suma se divide entre el largo total del arreglo

    return cant_promedio

total_promedio = promedio([1, 2, 3]) #total_promedio = 2
print(total_promedio)




#RETO 3: Crear una función que reciba un arreglo y que sume todos los números SIEMPRE Y CUANDO sean positivos
def sumaPositivos(arreglo):
    sum = 0
    for num in arreglo:
        if num > 0:
            sum += num

    return sum

total_suma = sumaPositivos([1, 2, 3, -1]) #Solo va a sumar 1 + 2 + 3
print(total_suma)
