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
