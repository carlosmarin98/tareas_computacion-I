#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Se crea la clase naturales. Como los numeros naturales son una estructura sencilla, la clase tiene unicamente un atributo,
# y es el numero en sí mismo.

class naturales:
    def __init__(self,numero):
        self.num=numero
        
    
#aqui se usa el primer constructor, es unicamente para poder mostrar el objeto
    
    def mostrar(self):
     print(self.num)
    
#el segundo constructor es parecido al anterior, sirve para convertir a cadena el objeto y poder mostrarlo    
    
    def __str__(self):
        return str(self.num)
    

#el primer metodo en sí. Es la suma, nos permitira realizar la suma habitual que conocemos, entre dos instancias u objetos de
#nuestra clase
    
    def __add__(self,otronum):

        nuevoNum = self.num+otronum.num
        return naturales(nuevoNum)

#De manera similar, esta operacion nos permitira multiplicar dos objetos, el resultado es otro entero    
    
    def __mul__(self,nuevomult):
        nuevomult=self.num*nuevomult.num
        return naturales(nuevomult)
    
    
 # esta es una operacion logica, nos permite comparar si dos de nuestro objetos son iguales.Retorna True sí es el caso.

    def __eq__(self,Acomparar):
        return self.num == Acomparar.num 
    
    
    

    
#Decidimos realizar las operaciones de manera secuencial, en el orden en que aparecen en la clase. Se muestra un ejemplo para
#los objetos (instancias de clase) a y b.
    
a=naturales(4)
b=naturales(6)



print(a+b)
print(a*b)
print(a == b)





        


# In[ ]:




