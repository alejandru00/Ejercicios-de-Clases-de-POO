class Palindromo:
    def __init__(self,cadena):
        self.cadena = cadena
    def test(self):
        cadena = ''.join(filter(str.isalum,self.cadena)).lower()
        if cadena == cadena[::-1]:
            return True
        else:
            print(self.cadena.upper())
            return False
    def __del__(self):
        print(self.cadena.upper())