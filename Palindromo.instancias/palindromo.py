class Palindromo:
    def __init__(self,cadena):
        self.cadena = cadena
    @classmethod
    def esPalindromo(cls,cadena):
        cadena = ''.join(e for e in cadena if e.isalnum()) 
        return cadena.lower() == cadena[::-1].lower()  
    def test(self):
        return self.esPalindromo(self.cadena)
    def __del__(self):
        print(self.cadena.upper())
p = Palindromo ("radar")
print(p.test())