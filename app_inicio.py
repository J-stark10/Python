print("Hola mundo desde Python")

# Variables en Python
# Enteros
edad = 20
# Float
precio = 50.5
# Str
nombre = "Javier Jose"
# Bool
bandera = True

# Salida de datos
print("Nombre: ",nombre)
print("Edad: ",edad)
print("Precio: " + str(precio))

# Entrada de datos
nombre = input("Introduce tu nombre : ")
print("Hola " + nombre)

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
# Conversion de str a int, str a float, str a float
suma = num1 + num2

print("La suma es: ", suma)

curso = "python para iniciantes"

# Metodos
print(curso.upper())
print(curso)
print(curso.lower())
print(curso.capitalize())

# Busquedas
print(curso.find("o"))
print(curso.find("cia"))

# Reemplazos
print(curso.replace("para", "for"))
print(curso)

# Operador
print("para" in curso)

# Operadores matematicos
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
# División entera
print(10 // 5)
# Modulo - residuo
print(10 % 3)
# Exponente
print(2 ** 4)

x = 10 
x = x + 5
print(x)

y = 20 
y += 5 
print(y)

# Precedencia 
x = 10 + 3 * 2 
print(x)

# Expresiones Boolenas (True o False) 
# > , >= , <= , < , == , !=

x = 3 > 2
print(x)

x = 5 ==3
print(x)

x = 5 != 3
print(x)

# Operadores Lógicos
# and , or , not 
precio = 25
print(precio > 20 and precio < 30)

precio = 5
print(precio > 20 or precio < 30)
print( not precio > 10)

# Sentencias
temperatura = int(input("Indica la temperatura: "))

if temperatura > 28: 
    print("Esta haciendo calor")
else : 
    print("Esta haciendo frio")

if temperatura > 28:
    print("Esta haciendo calor")
elif temperatura > 20:
    print("Es un día agradable")
elif temperatura > 10 : 
    print("Hace un poco de frio")
else :
    print("Hace frio, brrr")

print("Proceso concluido")

# Bucles
contador = 12
while (contador <= 20):
    print(contador)
    contador += 1

i = 1 
while (i <= 10):
    print(i * "*")
    i +=1

# listas

frutas = ['Manzana','Fresa','Naranjas','Pera','Maracuya']
print(frutas)
print(frutas[0])
print(frutas[4])
print(frutas[-2])
print(frutas[1:3])

# Metodos de LIstas

numeros = [1,2,3,4,5]
#Adicionar elementos a una lista
numeros.append(6)
#Insertar elementos en un posición determinada
numeros.insert(0,"hola")
numeros.insert(1,0)

print(numeros)

#Elimina un elemento en su primera aparición
numeros.remove("hola")
print(numeros)

#Verificar si un elemento se encuentra en la lista
print("hola" in numeros)

#Tamaño de la lista
print(len(numeros))

#Elimina el contenido de la lista
numeros.clear()
print(numeros)

# Objeto range

numeros = range(5)
print(numeros)

for items in numeros:
    print(items)

for item in range(5,10):
    print(item)

for item in range(10,20,2):
    print(item)

# Tuplas (inmutables)

numeros = (1,2,3,5,4,5,6)
# Imprimiendo un elemento
print(numeros[3])
# Ocurrencia
print(numeros.count(5))

print(numeros.index(5))

# Diccionarios -> Almacenan a pares de clave-valor
mi_diccionario = {'nombre': 'Javier','edad': 20, 'ciudad':'La Paz'}
print(mi_diccionario)

# Acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['edad'])

# Agregar elementos 
mi_diccionario['profesion'] = 'Ingeniero'

print(mi_diccionario)

# Eliminar un elemento 
del mi_diccionario['edad']

print(mi_diccionario)

# Obtener claves del diccionario
print(mi_diccionario.keys())

# Obtener valores del diccionario
print(mi_diccionario.values())

# Verificar si una clave existe
if 'ciudad' in mi_diccionario:
    print('Clave encontrada')

# Recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("Clave : "+clave+ " Valor: "+valor)

# Funciones - Son bloques de codigo que realiza una tarea 
# especificas y que son reutilizables

# Funcion sin parámetros ni devolución de valor
def saludar ():
    print('Hola, bienvenidos al curso de Python')

saludar()

# Función con parámetros
def saludo (nombre):
    print('Hola ' + nombre+ ' bienvenido a clases')

saludo('Javier Jose')

# Función que devuelve valores
def suma(a,b):
    return a + b

resultado = suma(4,5)
print(f"La suma es : {resultado}")

# Establecer valores por defecto para los parámetros de una función
def bienvenida(nombre='Estudiante'):
    print(f"Bienvenido {nombre}")

bienvenida()
bienvenida("Javier")

# Función con argumentos variados
def sumador(*args):
    return sum(args)

print(sumador(1,2,3,4,5))
print(sumador(10,21))