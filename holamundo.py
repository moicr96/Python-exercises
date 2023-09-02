print("hola mundo")

# en el directorio del proyecto correr el cmd y escribir> python holamundo.py

"""
con triple comilla se hace un comentario multilinea
"""
'''
dobles o simples
'''

#variables 
texto= "blablabla"
numero= 2023

#para concatenar
print(f"{texto} - {numero}") #es un estilo de impresion en la consola

#si el valor numero causa algun problema se puede cambiar su tipo de la siguiente forma:
print(f"{texto} - {str(numero)}")

#es lo mismo que:
print(texto + " - " + str(numero))

'''
#entrada de datos del usuario
nombre = input("dime tu nombre")
print("ya veo, tu nombre es: "+nombre)
'''

'''
#condiciones 
altura=int(input("dime tu altura"))  #lo que recoge el input por efecto es un string, entonces hay que convertirlo
if altura >= 180:
    print("eres una persona alta")
elif altura==0:
    print("WTF BRO")
else:
    print("eres una persona baja")

color='amarillo'
match color:
    case 'verde':
        print('adelante')
    case 'amarillo':
        print('cuidado')
    case 'rojo':
        print('pare')
    case _:  #guion bajo es para capturar casos adicionales
        print('error')
'''







'''
#listas 
personas=["jose","juan","carlos"]
print(personas[0])

for persona in personas:
    print("->"+persona)

#mapas
jugadores= {
    10: "MESSI",
    7: "CRISTIANO"
}
print(jugadores[7])

#diccionario texto a texto
paises= {
    "mx": "mexico",
    "ar": "argentina"
}
print(paises["mx"])
'''


'''
#funciones
var_altura=int(input("dime tu altura"))  #lo que recoge el input por efecto es un string, entonces hay que convertirlo
def mostrarAltura(altura):
    resultado=""
    if altura >= 180:
        resultado="eres una persona alta"
    else:
        resultado="eres una persona baja"
    
    return resultado

print(mostrarAltura(var_altura))



def quicksort(lista):
    if len(lista) <=1:
        return lista
    pivote = lista[0]
    izquierda = []
    derecha = []
    for i in range (1, len(lista)):
        izquierda.append(lista[i]) if lista[i]<pivote else derecha.append(lista[i])
    return quicksort(izquierda) + [pivote] + quicksort(derecha)
numeros = [23,45,16,37,3,99,22]
listaOrdenada=quicksort(numeros)
print(listaOrdenada)
'''

'''
#bucles
animales = ['perro', 'gato', 'tigre']
for animal in animales:
    print(animal)


def multiplicar(primero,segundo):
    print(primero*segundo)
numeros = [23,45,16,37,3,99,22]

for numero in numeros:
    multiplicar(numero,2)


entero=100
emergencia=911
while entero<emergencia:
    print(entero)
    entero+=1

'''

#POO
class lenguaje:
    def __init__(self, nombre, año):
        self.nombre=nombre
        self.año=año
    def descripcion(self):
        print('%s fue creado en %s' % (self.nombre, self.año))
javascript=lenguaje('javascript',1995)
javascript.descripcion() 

css=lenguaje('css',1996) #lo genial es que se puede reutilizar 
css.descripcion() 

#modulos
import moduloholamundo
moduloholamundo.restar(10,2)

