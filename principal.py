from operaciones_lista import agregar_elemento, eliminar_elemento, mostrar_lista


def main():
    lista = []
    while True:
        print("\n1. Agregar\n2. Eliminar\n3. Mostrar lista\n4. Salir")
        opcion = input("Ingrese valor: ")

        if opcion == "1":
            elemento = input("Elemento a agregar: ")
            agregar_elemento(lista, elemento)
        elif opcion == "2":
            elemento = input("Elemento a eliminar: ")
            eliminar_elemento(lista, elemento)
        elif opcion == "3":
            mostrar_lista(lista)
        elif opcion == "4":
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()
