class NodoDoble:
    def __init__(self, value, siguiente = None, anterior = None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble (None, None, None)
        self.__tail = NodoDoble (None, None, None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0
        #print(f"head :{self.__head}")
        #print(f"tail :{self.__tail}")

    def get_size(self):
        curr_node = self.__head
        while curr_node != None:
            curr_node = curr_node.prev
            self.__size = self.__size + 1
        print(f"Tiene elementos {self.__size}")

    def is_empty(self):
        return self.__head.data == None

    def append( self, value):
        nuevo = NodoDoble(value)
        if self.is_empty() == True:
           self.__head = nuevo
           self.__tail = nuevo
        else:
           nuevo.next = self.__tail
           self.__tail.prev = nuevo
           self.__tail = nuevo

    def transversal(self):
        nuevo = self.__head
        while nuevo != None:
            print(f"{nuevo.data} -> ", end="")
            nuevo = nuevo.prev
        print("")

    def reverse_transversal(self):
        nuevo = self.__tail
        while nuevo != None:
            print(f"{nuevo.data} -> ", end="")
            nuevo = nuevo.next
        print("")

    def find_from_tail(self, value):
        con = 0
        dato = None
        posicion = value
        if posicion == None:
            dato = print("No hay un valor")
        else:
            curr_node = self.__tail
            pre = None
            while curr_node.data != value and curr_node.next != None:
                pre = curr_node
                curr_node = curr_node.next
                con = con + 1
            if curr_node.data == posicion:
                dato = dato = print(f"El número de la posicion es: {con}")
            else:
                dato = print(f"El valor no existe")
                return dato

    def find_from_head(self, value):
        con = 0
        dato = None
        posicion = value
        if posicion == None:
            dato = print("No hay un valor")
        else:
            curr_node = self.__head
            pre = None
            while curr_node.data != value and curr_node.prev != None:
                pre = curr_node
                curr_node = curr_node.prev
                con = con + 1
            if curr_node.data == posicion:
                dato = dato = print(f"El número de la posicion es: {con}")
            else:
                dato = print(f"El valor no existe")
                return dato

    def remove_from_tail(self, value):
        curr_node = self.__tail
        if self.__tail.data == value:
            self.__tail = self.__tail.next
        else:
            pre = None
            while curr_node.data != value and curr_node.next != None:
                pre = curr_node
                curr_node = curr_node.next
                if curr_node.data == value:
                    pre.next = curr_node.next
                    self.remove_from_head(curr_node.data)

        if self.__head.data == value:
            self.__tail = self.tail()

    def remove_from_head(self, value):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.prev
        else:
            pre = None
            while curr_node.data != value and curr_node.prev != None:
                pre = curr_node
                curr_node = curr_node.prev
                if curr_node.data == value:
                    pre.prev = curr_node.prev
