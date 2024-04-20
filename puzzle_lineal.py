from bfs import Nodo
def buscar_scc_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    
    while(not solucionado)and len(nodos_frontera)!=0:
        nodo = nodos_frontera.pop(0)
        
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            # Operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izq = Nodo(hijo)
            if not hijo_izq.en_lista(nodos_visitados) and not hijo_izq.en_lista(nodos_frontera):
                nodo.set_hijos([hijo_izq])
                nodos_frontera.append(hijo_izq)

            # Operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_cent = Nodo(hijo)
            if not hijo_cent.en_lista(nodos_visitados) and not hijo_cent.en_lista(nodos_frontera):
                nodo.set_hijos([hijo_cent])
                nodos_frontera.append(hijo_cent)

            # Operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_der = Nodo(hijo)
            if not hijo_der.en_lista(nodos_visitados) and not hijo_der.en_lista(nodos_frontera):
                nodo.set_hijos([hijo_der])
                nodos_frontera.append(hijo_der)

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_scc_BFS(estado_inicial, solucion)

    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)