import time

lista = []
nueva_lista = []
longitudes = []
lista_cuadrada = []

time.sleep(2)
print('\nPor favor introduce los numeros a sumar')
time.sleep(2)
print('\nCuando termines, escribe la letra "q" para empezar con la sumatoria.')

while True:
    time.sleep(1)
    print('\nIntroduzca un numero, o la letra "q"')
    entrada = input('>')
    if entrada != 'q':
        lista.append(entrada)
    else:
        break
    
def formato(lista, resultado_total):
    print('') 
    print(lista[0].rjust(10, ' '), ' +')
    for i in range(1, len(lista)):
        print(lista[i].rjust(10, ' '))
    print(10*'-')
    print(resultado_total.rjust(10, ' '))


def integer_to_string(lista):
    for item in lista:
        nueva_lista.append(str(item))

    return nueva_lista

def sumandos_a_matriz(lista):
    for item in lista:
        longitudes.append(len(list(item)))

    return longitudes

integer_to_string(lista)
sumandos_a_matriz(nueva_lista)
longitudes.sort()

def igualar_longitudes(lista):
    for item in lista:
        if len(item) < longitudes[-1]:
            item = '0'*(longitudes[-1]-len(item)) + item
            lista_cuadrada.append(item)
        else:
            lista_cuadrada.append(item)

    return lista_cuadrada

igualar_longitudes(nueva_lista)

def sumar_todo(lista):
    llevamos = 0
    resultado_parcial = 0
    resultado_total = ''

    for i in range(longitudes[-1]):
        texto = ''
        entero = 0

        time.sleep(2)
        formato(nueva_lista, resultado_total)

        for item in lista:
            texto = texto + ' + ' + item[-1-i]
            entero = entero + int(item[-1-i])
            
        resultado_parcial = entero + llevamos 
        time.sleep(2)
        print('\nCuanto es ', texto[3:], '?')
        respuesta = int(input())
        while respuesta != entero:
            time.sleep(2)
            print('\nNo es el numero que estamos buscando,,, por favor intenta nuevamente')
            respuesta = int(input())
        time.sleep(2)
        print(f'\nCorrecto, y {llevamos} que llevamos son {resultado_parcial}')

        if i < longitudes[-1] - 1:
            if resultado_parcial >= 10:
                llevamos = int((str(resultado_parcial))[0])
                ponemos = str(resultado_parcial)[-1]
            else:
                llevamos = 0
                ponemos = str(resultado_parcial)
    
            resultado_total = ponemos + resultado_total

            time.sleep(2)
            print(f'\nPonemos el {ponemos} y llevamos {llevamos}, presiona ENTER para continuar...')
            continuar = input()
        else:
            resultado_total = str(resultado_parcial) + resultado_total
            
            time.sleep(2)
            print(f'\nPonemos el {resultado_parcial} y terminamos la suma, este es el resultado:')
    
    time.sleep(2)        
    formato(nueva_lista, resultado_total)

sumar_todo(lista_cuadrada)


