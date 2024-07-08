import os

class InventarioFrutas:
    def __init__(self, max_cant=100, nombre_max=30, archivo="inventario.txt"):
        self.max_cant = max_cant
        self.nombre_max = nombre_max
        self.nombres = []
        self.cantidad = []
        self.precio = []
        self.archivo = archivo
        self.cargar_datos()

    def ingresar_fruta(self):
        if len(self.nombres) >= self.max_cant:
            print("INVENTARIO LLENO")
            return

        nombre = input("Ingrese el nombre de la fruta: ")

        while True:
            cantidad = int(input("Ingresar cantidad de la fruta: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
            else:
                break

        while True:
            precio = float(input("Ingresar precio de la fruta: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intente de nuevo.")
            else:
                break

        self.nombres.append(nombre)
        self.cantidad.append(cantidad)
        self.precio.append(precio)
        self.guardar_datos()
        print("FRUTA INGRESADA")

    def editar_fruta(self):
        nombre = input("Ingrese el nombre de la fruta que desea editar: ")
        index = self.buscar_fruta(nombre)
        if index == -1:
            print("FRUTA NO ENCONTRADA")
            return

        while True:
            cantidad = int(input("Ingresar la nueva cantidad de la fruta: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
            else:
                break

        while True:
            precio = float(input("Ingresar el nuevo precio de la fruta: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intente de nuevo.")
            else:
                break

        self.cantidad[index] = cantidad
        self.precio[index] = precio
        self.guardar_datos()
        print("FRUTA EDITADA")

    def eliminar_fruta(self):
        nombre = input("Ingresa el nombre de la fruta que deseas eliminar: ")
        index = self.buscar_fruta(nombre)
        if index == -1:
            print("Fruta no encontrada.")
            return

        del self.nombres[index]
        del self.cantidad[index]
        del self.precio[index]
        self.guardar_datos()
        print("FRUTA ELIMINADA")

    def listar_frutas(self):
        if not self.nombres:
            print("No hay frutas en el inventario.")
            return

        print("Lista de Frutas:")
        for nombre, cantidad, precio in zip(self.nombres, self.cantidad, self.precio):
            print(f"Nombre: {nombre}, Cantidad: {cantidad}, Precio: {precio:.2f}")

    def buscar_fruta(self, nombre):
        try:
            return self.nombres.index(nombre)
        except ValueError:
            return -1

    def guardar_datos(self):
        with open(self.archivo, 'w') as archivo:
            for nombre, cantidad, precio in zip(self.nombres, self.cantidad, self.precio):
                archivo.write(f"{nombre},{cantidad},{precio}\n")

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as archivo:
                for linea in archivo:
                    nombre, cantidad, precio = linea.strip().split(',')
                    self.nombres.append(nombre)
                    self.cantidad.append(int(cantidad))
                    self.precio.append(float(precio))

# Programa principal
def main():
    inventario = InventarioFrutas()
    opciones = {
        '1': inventario.ingresar_fruta,
        '2': inventario.editar_fruta,
        '3': inventario.eliminar_fruta,
        '4': inventario.listar_frutas,
        '5': exit
    }

    while True:
        print("\nINVENTARIO DE TIENDA DE FRUTAS\n")
        print("Seleccione la opción para configurar el inventario:")
        print("1. Ingresar fruta")
        print("2. Editar frutas")
        print("3. Eliminar frutas")
        print("4. Listar frutas")
        print("5. Salir")
        opcion = input("\tSeleccione una opción: ")

        if opcion in opciones:
            opciones[opcion]()
        else:
            print("La opción no es válida, vuelva a ingresar")

if __name__ == "__main__":
    main()
