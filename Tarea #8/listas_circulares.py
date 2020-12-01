class NodoSimple:
    def __init__( self , value , sig= None):
        self.data = value
        self.next = sig

class CircularLinkedList:
    def __init__( self ):
        self.__head = None
        self.__refe = None
        self.__size = 0

    def is_empty (self):
        return self.__size == 0

    def transversal (self):
        curr_node = self.__refe
        while curr_node.next != self.__refe :
            print(f"{ curr_node.next.data } --> " , end="")
            curr_node= curr_node.next
        print(self.__refe.data)

    def search (self, value ):
         new = NodoSimple(value)
         curr_node= self.__refe
         while new.data != curr_node.next.data and curr_node.next != self.__refe:
                curr_node = curr_node.next
         if new.data == curr_node.next.data :
             return True
         else:
             return False

    def insert (self, value ):
        if self.is_empty() :
            self.__head = self.__refe= NodoSimple(value)
            self.__refe.next= self.__head
            self.__size +=1
        elif self.search(value) == True :
              print("Este valor ya existe")
        elif value > self.__refe.data:
            new = self.__refe
            self.__refe = new.next= NodoSimple(value, self.__head)
            self.__size +=1
        elif value < self.__refe.data and value < self.__head.data:
             new =  NodoSimple(value)
             new.next = self.__head
             self.__head = new
             self.__refe.next = new
             self.__size +=1
        elif value < self.__refe.data and  value > self.__head.data:
            new = NodoSimple(value)
            curr_node= self.__head
            while new.data > curr_node.next.data:
                curr_node = curr_node.next
            new.next= curr_node.next
            curr_node.next= new
            self.__size +=1

    def remove( self , value ):
        new = NodoSimple(value)
        curr_node= self.__refe
        if self.search(value) == False :
              print("El valor no existe")
        else:
            while new.data != curr_node.next.data and curr_node.next != self.__refe:
                  curr_node = curr_node.next
            if curr_node.next.data == self.__refe.data:
                curr_node.next =  self.__refe.next
                self.__refe = curr_node
                self.__size -=1
            elif curr_node.next.data == self.__head.data:
                self.__head = self.__head.next
                self.__refe.next = self.__head
                self.__size -=1
            elif curr_node.next.data != self.__refe.data and curr_node.next.data != self.__head.data:
                pre = None
                while curr_node.data != value and curr_node.next != self.__refe:
                      pre = curr_node
                      curr_node= curr_node.next
                if curr_node.data == value:
                    pre.next= curr_node.next
                    self.__size -=1
