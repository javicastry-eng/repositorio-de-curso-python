def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista


def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista


def mostrar_lista(lista):
    print("Lista actualizada:", lista)

def buscar_elemento(lista, elemento):
    if elemento in lista:
        print(f"{elemento} esta en la lista")
    else:
        print(f"{elemento} no esta en la lista")
