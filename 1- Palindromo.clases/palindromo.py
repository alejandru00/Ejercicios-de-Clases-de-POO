

#Ejercicio 1: crear una clase Palindromo que contenga un método de clase esPalindromo(), que devuelve un valor booleano que indica si una cadena de caracteres pasada como argumento es un palíndromo. Un palíndromo es una cadena que se puede leer de izquierda a derecha o de derecha a izquierda. Se tienen en cuenta los caracteres no alfanuméricos.

class Palindromo:
    @classmethod
    def esPalindromo(cls, cadena):
        cadena = ''.join(e for e in cadena if e.isalnum())
        return cadena.lower() == cadena[::-1].lower()
print(Palindromo.esPalindromo('radar'))    
print(Palindromo.esPalindromo('sonar'))   
print(Palindromo.esPalindromo('Arde ya la yedra'))   
print(Palindromo.esPalindromo('Ardeyalayedra'))   
print(Palindromo.esPalindromo('!@#$% %$#@!'))  
print(Palindromo.esPalindromo('L O L'))   
