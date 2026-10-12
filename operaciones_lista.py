def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista


def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista


def mostrar_lista(lista):
    print("Lista actual:", lista)
