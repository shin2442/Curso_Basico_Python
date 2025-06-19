# Crear la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Definir el método para imprimir
    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

# Crear la clase Ciudadano que hereda de Persona
class Ciudadano(Persona):
    def __init__(self, nombre, edad, deposito):
        super().__init__(nombre, edad)
        self.deposito = deposito
    
    # Método para imprimir todos los datos
    def imprimir(self):
        super().imprimir()
        print("Depósito:", self.deposito)
    
    # Método para verificar si debe pagar impuestos
    def impuestos(self):
        if self.deposito > 4000:
            print(f"El ciudadano {self.nombre} **sí debe pagar impuestos**")
        else:
            print(f"El ciudadano {self.nombre} **no debe pagar impuestos**")

# Crear objetos con los datos dados
c1 = Ciudadano("Manuel Chima", 25, 6700)
c2 = Ciudadano("Fayle García", 56, 3500)
c3 = Ciudadano("Lesly Rodríguez", 34, 9000)
c4 = Ciudadano("Mario Herrera", 45, 2500)

# Llamar métodos para cada ciudadano
for ciudadano in [c1, c2, c3, c4]:
    ciudadano.imprimir()
    ciudadano.impuestos()
    print("-" * 40)

"""
Resultados de impuestos:

- Manuel Chima: sí debe pagar impuestos (depositó 6700)
- Fayle García: no debe pagar impuestos (depositó 3500)
- Lesly Rodríguez: sí debe pagar impuestos (depositó 9000)
- Mario Herrera: no debe pagar impuestos (depositó 2500)
"""
