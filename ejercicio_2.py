#con este algoritmo obtenemos la maxima suma de una secuencia sumando la maxima subsecuencia

def suma1(A):
    sumamax=0
    for i in range(len(A)):
        for j in range(i,len(A)):
            actual=0
            for k in range(i,j):
                actual=actual+A[k]
            if actual > sumamax:
                sumamax=actual
    print(sumamax)         
                


def suma2(A):
    sumamaxd=0
    for i in range(len(A)):
        sumamaxd=sumamaxd+A[i]
    print(sumamaxd)    
        

        
A=[7,11,12,15,3]        
suma1(A)  

suma2(A)
    