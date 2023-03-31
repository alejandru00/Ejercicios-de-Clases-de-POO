

#Clase logger
class logger:
    def __init__(self, nombre):         #Constructor
        self.nombre = nombre
        self.contador = 0
        with open(self.nombre, "w") as f:
            f.write("--Log start--: \n")

    def log(self, mensaje):             #Escribir en el log
        self.contador += 1
        with open(self.nombre, "a") as f:
            f.write(f"{self.contador}: {mensaje}")
    
    def __del__(self):                  #Destructor
        with open(self.nombre, "a") as f:
            f.write("--Log end--: \n")

#Testear
class test:
    def __init__(self):
        self.logger = logger("log.txt")
    
    def llamar(self, mensaje):
        self.logger.log(mensaje)

test = test()
i = 1
while True:
    mensaje = "Llamada numero {i}"
    test.llamar(mensaje)
    i += 1


    
