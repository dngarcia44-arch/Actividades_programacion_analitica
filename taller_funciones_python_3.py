# Ejercicios de práctica Fundamentos Python (3)
# Edna Rocio Garcia Hende

# %% EJERCICIO 1 - Definir una función

def saludar():
    print("Hola")

saludar()

# %% EJERCICIO 2 - Llamar a la función

def bienvenida():
    print("Bienvenido al curso")

bienvenida()

# %% EJERCICIO 3 - Predecir el orden de ejecución

def uno():
    print("A")

print("B")
uno()
print("C")
# Respuesta:
# B
# A
# C

# Ejercicios 4 al 8 — Definir y llamar funciones
# %% EJERCICIO 4 - Corregir el orden

def saludar(nombre):
    print("Hola,", nombre)

saludar("Ana")

# %% EJERCICIO 5 - Función con un parámetro

def saludar(nombre):
    print("Hola,", nombre)

saludar("Ana")

# %% EJERCICIO 6 - Función con dos parámetros

def area(base, altura):
    return base * altura

print(area(3, 4))

# %% EJERCICIO 7 - Completar la llamada

def area(base, altura):
    return base * altura

print(area(5.0, 5))

# %% EJERCICIO 8 - Reutilizar la misma función

def con_iva(precio):
    return precio * 1.19

print(con_iva(1000))
print(con_iva(2000))
print(con_iva(3000))

# Ejercicios 9 al 15 — Parámetros y argumentos

# %% EJERCICIO 9 - Parámetro o argumento

def doble(n):
    return n * 2

resultado = doble(5)
# n es el parámetro.
# 5 es el argumento.

print(resultado)

# %% EJERCICIO 10 - Argumentos por posición

def perfil(nombre, edad, ciudad):
    print(nombre, edad, ciudad)

perfil("Ana", 20, "Bogota")

# %% EJERCICIO 11 - Argumentos por nombre

def perfil(nombre, edad, ciudad):
    print(nombre, edad, ciudad)

perfil(edad=20, nombre="Ana", ciudad="Bogota")

# %% EJERCICIO 12 - Valor por defecto

def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar("Ana")

# %% EJERCICIO 13 - Reemplazar el valor por defecto

def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar("Luis", "Buen dia")

# %% EJERCICIO 14 - Orden de los parametros

def registrar(producto, cantidad=1):
    print(producto, cantidad)

# %% EJERCICIO 15 - Una lista como argumento

def total(precios):
    suma = 0
    for p in precios:
        suma = suma + p
    return suma

print(total([1200, 950, 3400]))

# %% EJERCICIO 16 - Devolver un valor

def doble(n):
    return n * 2

print(doble(5))

# %% EJERCICIO 17 - Usar el valor devuelto

def doble(n):
    return n * 2

resultado = doble(6)

print(resultado + 1)

# %% EJERCICIO 18 - Funcion sin return

def saludo(nombre):
    print("Hola,", nombre)

x = saludo("Ana")
print(x)
# Aparece None porque la funcion imprime el saludo,
# pero no devuelve ningun valor con return.

# %% EJERCICIO 19 - print o return

def doble(n):
    return n * 2

total = doble(5) + 3

print(total)

# %% EJERCICIO 20 - return dentro de una condicion

def signo(n):
    if n < 0:
        return "negativo"
    return "positivo"

print(signo(-4))
print(signo(7))

# %% EJERCICIO 21 - return termina la funcion

def prueba(n):
    if n > 0:
        return "positivo"
    print("linea intermedia")
    return "otro"

print(prueba(5))

# Respuesta:
# Solo se imprime "positivo".
# La linea intermedia no aparece porque return termina
# la ejecucion de la funcion.

# %% EJERCICIO 22 - Devolver dos valores

def resumen(valores):
    return min(valores), max(valores)

menor, mayor = resumen([8, 3, 10, 5])

print(menor, mayor)

# %% EJERCICIO 23 - Encadenar funciones

def con_iva(p):
    return p * 1.19

def redondear(valor):
    return round(valor, 2)

print(redondear(con_iva(1200)))

# Ejercicios 24 al 29 — Ámbito y colecciones
# %% EJERCICIO 24 - Variable local y global

mensaje = "global"

def prueba():
    mensaje = "local"
    print(mensaje)

prueba()
print(mensaje)

# Respuesta:
# local
# global

# %% EJERCICIO 25 - Evitar variables globales

def con_iva(precio, iva):
    return precio * (1 + iva)

print(con_iva(1000, 0.19))

# %% EJERCICIO 26 - No modificar el original

def agregar(lista):
    nueva = lista + [3]
    return nueva

datos = [1, 2]

print(agregar(datos))
print(datos)

# %% EJERCICIO 27 - Funcion que recibe una lista

def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)

print(promedio([3.5, 4.2, 2.8]))

# %% EJERCICIO 28 - Funcion que recibe un diccionario

def describir(alumno):
    print(alumno["nombre"], alumno["nota"])

describir({"nombre": "Laura", "nota": 4.6})

# %% EJERCICIO 29 - Funcion que devuelve una lista

def aprobados(estudiantes):
    resultado = []
    for e in estudiantes:
        if e["nota"] >= 3.0:
            resultado.append(e["nombre"])
    return resultado

datos = [
    {"nombre": "Ana", "nota": 4.2},
    {"nombre": "Luis", "nota": 2.8}]
print(aprobados(datos))

# %% EJERCICIO 30 - Reporte de notas con funciones

def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)
def aprueba(prom, minimo=3.0):
    return prom >= minimo
def reporte(nombre, notas):
    prom = promedio(notas)
    print(nombre, round(prom, 2))
    if aprueba(prom):
        print("Aprobado")
    else:
        print("No aprobado")
reporte("Laura", [3.5, 4.2, 2.8])


# Respuesta:
# promedio recibe una lista de notas y devuelve el promedio.
# aprueba recibe el promedio y la nota minima, y devuelve
# True si aprueba o False si no aprueba.
# reporte recibe el nombre y las notas del estudiante,
# y muestra el nombre, el promedio y si aprobo.

# %%
