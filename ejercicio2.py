
# Implementación de los algoritmos
"""
def potencia(b,n):
    

    pila = []
    while n > 0:
        if n % 2 == 0:
            pila.append(True)
            n /= 2
        else:
            pila.append(False)
            n = (n-1)/2

    pot = 1
    while pila:
        es_par = pila.pop()
        if es_par:
            pot = pot * pot
        else:
            pot = pot * pot * b

    return pot
"""
def CandidatoI(A, i, j):
    ip = i
    jp = j
    n = i + j
    stack = []
    while n >= 2 :
        
        stack.append((i, j))
        
        jp = k
    if n == 0:
        y = NULL   
    if n == 1:
        y = A[n]
    while len(stack) != 0:
        k = 0
        for s in range(ip, jp, 2):
            if A[s] == A[s + 1]:
                k += 1
                A[k] = A[s]
            
        y = 
    return y


def CandidatoR(A, i, j):
    if j == 1:
        if A[i] == A[j]:
            return A[i]
        else:
            return None
    elif j == 0:
        return A[i]
    elif len(A) == 0:
        return None
    else:
        D = []
        cont = 0
        if (j + 1 - i) % 2 != 0:
            cont += 1
            D.append(A[j])
        for k in range(i, j, 2):
            if A[k] == A[k+1]:
                D.append(A[k])
                cont += 1

        return CandidatoR(D, 0, cont - 1)
  
#P4 implementación de algoritmo de Comprobar
def Comprobar(A, i, j, m):
  """
  Esta función comprueba el numero que mas se repite en el array.

  Args:
      A(array de int): Lista que tiene una serie numeros.
      i (int): El número en el que inicia el array.
      j (int): El número en el que acaba el array.
      m (int): El numero que más veces se repite en el array.


  Returns:
      int: El numero que vas veces se repite en el array.

  La complejidad de la funcion es lineal O(n)
  O(n) = O(1) + (O(n) * (maxO(1) + O(1))) + max(O(1)) + O(1)
  """


  contador = 0 # O(1) iniciamos el contador
  for k in range (i, j+1):  #---O(n) recorre el subarray depende del tamaño
      if A[k] == m: #max(O(1)) si se ejecuta
          contador += 1
  num = (j - i + 1) // 2 #O(1) calcula os la  mitad del tamaño del array
  if contador > num: #max(O(1)) realizar la medicion es consante y reornar es constante
      return m
  return None #O(1) retornar none