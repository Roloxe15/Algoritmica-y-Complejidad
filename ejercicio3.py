
def stoogesort(A, i, n): 
  
     
    # En el caso en el que el primer elemento es mayor que el ultimo cambialo
    if A[i]>A[n]: 
        temp = A[i] 
        A[i] = A[n] 
        A[n] = temp 
   
    # If there are more than 2 elements in 
    # the Aay 
    if n-i + 1 > 2: 
        #truncamos para obtener el auxilar por abajo
        m = (int)((n-i + 1)/3) 
   
        # Recursivamente vamos divienod el algoritmo en  2/3 del inicio el segundo tercio
        stoogesort(A, i, (n-m)) 
   
        # Lo mismo pero en vez del primer elemento con los dos ultimos tercios
        stoogesort(A, i + m, (n)) 
   
        # Hacemos otravez el inicio para reordenarlo
        stoogesort(A, i, (n-m)) 
   
  
#Ejemplo
A = [2, 4, 5, 3, 1] 
n = len(A) 
  
stoogesort(A, 0, n-1) 
   

print(A) 
  