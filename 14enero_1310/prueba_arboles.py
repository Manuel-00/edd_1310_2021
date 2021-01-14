class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

arbol = NodoArbol("R",NodoArbol("C", None, None),NodoArbol("H", None, None)) #el None es opcional

print(arbol.left.data)
print(arbol.right.data)
print(arbol.data)

arbol2 = NodoArbol(4, NodoArbol(3, NodoArbol(2, NodoArbol(2),None)), NodoArbol(5))
print(arbol2.data)
print(arbol2.left.data)
print(arbol2.left.left.data)
print(arbol2.left.left.left.data)
print(arbol2.right.data)
