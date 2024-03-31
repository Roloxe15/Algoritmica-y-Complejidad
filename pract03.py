
import numpy as np
import time
import matplotlib.pyplot as plt



def Iter2(A,hueco, ficha, m):
    """

        Argumentos
            A   Array de tamaño 2n + 1 que contendra las fichas y lo huecos
            i   primer elemento del array
            j   ultimo elemento del array
            hueco   posicin donde no hay  una ficha en el array
            ficha   la pieza que se va a mover del array hacia el hueco
            m   El numero de moovimientos para finalazar la jugada

        Retorna (int) el numero de iteraciones y la funcion recursica en el caso que se cumpla

    """
    huecop = hueco
    fichap = ficha
    mp = m
    n = ((0 + len(A))// 2) - 1
    np = n

    stack = []
   
    while mp < 2*np - 1 :
       
        stack.append((huecop, fichap, mp))
        print(A)
        temp = A[huecop]
        A[huecop] = A[fichap]
        A[fichap] = temp
        if ficha == np + 1:
            mp += 1
        if np <= ficha and fichap <= np  + 2:
            mp += 1
        
        if huecop - 1 <= fichap and fichap <= huecop + 1:
            huecop = fichap
            fichap = huecop - A[huecop]
        elif A[huecop] == A[fichap + A[huecop]]:
            huecop = fichap
            fichap = huecop + A[huecop]
        else :
            huecop = fichap
            fichap = huecop + A[huecop] * 2

    y = 0

    if len(A) %2 == 0:
        stack.pop()
        y = y + 1
    
    while len(stack) > 0:
        c = stack.pop()
        huecop = len(A) - c[0] + 1
        fichap = len(A) - c[1] + 1
        Aux = A[fichap]
        A[fichap] = A[huecop]
        A[huecop] = Aux
        mp = c[2]
        y += 2
        Mostrar(A)

    return y
        

def Iter1(A, t = False):
    """

        Argumentos
            A   Array de tamaño 2n + 1 que contendra las fichas y lo huecos
            i   primer elemento del array
            j   ultimo elemento del array
            hueco   posicin donde no hay  una ficha en el array
            ficha   la pieza que se va a mover del array hacia el hueco
            m   El numero de moovimientos para finalazar la jugada

        Retorna (int) el numero de iteraciones y la funcion recursica en el caso que se cumpla

    """
    
    A2 = A
    
    m= 0
    
    hueco = len(A)//2
    ficha = hueco - 1

    n = hueco
    stack = []
   
    while m < len(A) - 2 :
       
        stack.append(A2)
        
        A2[hueco], A2[ficha] = A2[ficha], A2[hueco]

        ficha_aux  = ficha

        if ficha == n:
            m += 1
        if n - 1 <= ficha and ficha <= n  + 1:
            m += 1
        
        if hueco - 1 <= ficha and ficha <= hueco + 1:
            
            ficha = hueco - A[hueco]
        elif A[hueco] == A[ficha + A[hueco]]:
            ficha = ficha + A[hueco]
        else :
            
            ficha = ficha + A[hueco] * 2

        hueco = ficha_aux

    y = 0
    B = []
    while len(stack) > 0:
        B.append(stack.pop())
        
        y += 1

    return y


        
    


































# Implementación de los algoritmos
def Recursivo(A, hueco, ficha, m):
    if m >= len(A) - 2:
        Mostrar(A)
        return 0
    else:
        Mostrar(A)
        A[hueco], A[ficha] = A[ficha], A[hueco]
        n = len(A) // 2
        if ficha == n:
            m += 1
        if n - 1 <= ficha <= n + 1:
            m += 1
        if hueco - 1 <= ficha <= hueco + 1:
            return Recursivo(A, ficha, hueco - A[hueco], m) + 1
        elif A[hueco] == A[ficha + A[hueco]]:
            return Recursivo(A, ficha, ficha + A[hueco], m) + 1
        else:
            return Recursivo(A, ficha, ficha + A[hueco] * 2, m) + 1

def Mostrar(A):
    s = ''
    for i in range(len(A)):
        if A[i] == 1:
            s += '\33[42m  \33[0m  '
        elif A[i] == -1:
            s += '\33[43m  \33[0m  '
        else:
            s += '\33[47m  \33[0m  '
    print('\n' + s)



A=[[-1, 0, 1]]
ficha = 1
hueco = 0
m = 0


print(Iter2(A, ficha, hueco, m))
print(Recursivo(A, ficha, hueco, m))



B = [-1, -1, -1, -1, 1, 0, 1, -1, 1, 1, 1]
ficha2 = 6
hueco2 = 4
m2 = 4


print(Iter2(B, ficha2, hueco2, m2))
print(Recursivo(B, ficha2, hueco2, m2))
print(Iter1(B))



C= [-1, 1, -1, 0, 1]
ficha3 = 4
hueco3 = 5
m3 = 2
print(Iter2(C, ficha3, hueco3, m3))
print(Recursivo(C, ficha3, hueco3, m3))
print(Iter1(C))


D = [-1, -1, -1, 0, 1, 1, 1]
ficha4 = 4
hueco4 = 3
m4 = 0

print(Iter2(D, ficha4, hueco4, m4))
print(Recursivo((D, ficha4, hueco4, m4)))
print(Iter1(D))




