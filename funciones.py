"""
def multipliacion():
    print(f'la multiplicación de 7x7 es igual a {7*7}')
"""
#metodo para multiplicar dos parametros
def multipliacion(a,b):
    #multiplicación
    print(f'la multiplicación de {a}X{b} es igual a {a*b}')
    #comprobación de par
    print(f'Y este resultado es par: {par(a*b)}')
#evalua si un numero es par o impar
def par(a):
    if (a % 2) == 0:
        return 'par'
    else:
        return 'impar'
print('inicia el software')
#llamado de la función
multipliacion(3,4)
print('siguiente')
multipliacion(5,5)