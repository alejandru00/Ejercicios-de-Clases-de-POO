class Palíndromo:
    @staticmethod
    def esPalindromo(cadena):
        cadena = cadena.lower().replace(" ", "").replace(",", "").replace(".", "")
        return cadena == cadena[::-1]