

#Ejercicio 3: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible.

class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z'))) 

"""
COMENTARIOS:

-> class A: la clase llamada A está compuesta por "z", que devuelve el mismo "self", y "y", que devuelve la longtud del parámetro "t".

-> a = A: se le asigma a la variable a la clase A.

-> y = a.z: se le asigna el metodo "z" de "a" (a la que se le ha asignado previamente la instancia de la clase "A") a la variable "y".  

-> print(y(a)): printea el resultado anterior: "<class '__main__.A'>"; ya que "a" es una instancia de "A".

-> aa = a(): se crea una instancia de la clase "A" dos veces "a".

-> print(aa is a()): printea "False", ya que "a" es una instancia de "A" y "aa" es otra instancia de "A" (son dos instancias diferentes).

-> z = aa.y: a la variable "z" se le asigna el método "y" de "aa".

-> print(z(())): se le llama a "z" con una tupla vacía por lo que devuelve "0".

-> print(a().y((a,))): esta tupla que contiene "a" devuelve "1" ya que su longitud es de 1.

-> print(A.y(aa, (a,z))): en este caso la dupla contiene "a" y "z" por lo que devuelve el número "2" (elementos de la dupla)

-> print(aa.y((z,1,'z'))): en este metodo "y", la dupla contiene los elementos "z", "1" y "'z '", la longitud de la cual es 3, por lo que printea un "3".

"""