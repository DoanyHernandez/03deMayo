print("Bienvenido al programa\n")

class casa_principal: 
    def _init_(self, ventanas, puertas, techo, color):
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.color = color

    def mostrar_info(self):
        print(f"Ventanas: {self.ventanas}")
        print(f"Puertas: {self.puertas}")
        print(f"Techo: {self.techo}")
        print(f"Color: {self.color}")


class casa_colonial(casa_principal):
    def _init_(self, ventanas, puertas, techo, color, num_habitaciones, cortinas):
        super()._init_(ventanas, puertas, techo, color)
        self.num_habitaciones = num_habitaciones
        self.cortinas = cortinas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habitaciones: {self.num_habitaciones}")
        print(f"Cortinas: {self.cortinas}")


class casa_familiar(casa_principal):
    def _init_(self, ventanas, puertas, techo, color, patio_juegos, piscina):
        super()._init_(ventanas, puertas, techo, color)
        self.patio_juegos = patio_juegos
        self.piscina = piscina

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Patio de juegos: {self.patio_juegos}")
        print(f"Piscina: {self.piscina}")

class casa_campo(casa_principal):
    def _init_(self, ventanas, puertas, techo, color, balcon):
        super()._init_(ventanas, puertas, techo, color)
        self.balcon = balcon

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Balcón: {self.balcon}")

while True:
    print("\nSeleccione el tipo de casa que desea crear:")
    print("1. Casa Colonial")
    print("2. Casa Familiar")
    print("3. Casa de Campo")

    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        casa = casa_colonial(6, 2, "a dos aguas", "blanco", 4, "cortinas elegantes")
        break
    elif opcion == "2":
        casa = casa_familiar(8, 3, "moderno", "gris", "sí", "sí")
        break
    elif opcion == "3":
        casa = casa_campo(5, 2, "de tejas", "verde", "amplio")
        break
    else:
        print("\nOpción no válida. Por favor, intente de nuevo.")
        
print("\nInformación de la casa creada:")
casa.mostrar_info()