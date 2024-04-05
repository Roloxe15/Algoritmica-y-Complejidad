

 
# Función para encontrar la suma máxima de la sublista usando divide y vencerás
def suma_max_subarrays(A, i, j):
 

    # Caso BaseSi la lista contiene 0 o 1 elemento
    if i == j:
        return A[i], i, j
    else: # casos
        # Encuentra el elemento del medio en la lista
        k = (i + j) // 2
    
        # Encuentra la suma máxima de la sublista para la sublista izquierda,
        # incluido el elemento central
        mayor1 = -900000
        tot = 0
        for s in range(k, i - 1, -1):
            tot += A[s]
            #Comparamos el valor del  total y mayor en el caso que tot no sea mayor maypr es tot
            if tot > mayor1:
                mayor1 = tot
    
        # Encuentra la suma máxima de la sublista para la sublista derecha,
        # excluyendo el elemento central
        mayor2 = -900000
        tot = 0        # restablecemos la suma a 0
    
        for s in range(k + 1, j + 1):
            tot += A[s]
            if tot > mayor2:
                mayor2 = tot
    
        # Encuentre recursivamentemente la suma máxima de la sublista para la izquierda
        # y sublista derecha, y toma el máximo

        sum1, i1, j1 =  suma_max_subarrays(A, i, k)
        sum2, i2, j2 =  suma_max_subarrays(A, k + 1, j)

        aux = 0
        ia = 0
        ja = 0
        if  sum1 >= sum2 :
            aux = sum1
            ia = i1
            ja = j1
        else: 
            aux = sum2
            ia = i2
            ja = j2
        # devuelve el máximo de los tres
        if aux >= (mayor1 + mayor2):
            return aux, ia, ja
        else:
            return (mayor1 + mayor2), ia, ja
        
 
 

 
A = [2, -4, 1, 9, -6, 7, -3]
print('La maxima suma de un subarray de la lista es', suma_max_subarrays(A, 0, len(A) - 1))

B = [10, -19, 18, 3, -20, 22]
print('La maxima suma de un subarray de la lista es', suma_max_subarrays(B, 0, len(B) - 1))