class Stack:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def pop(self):
        if self.is_empty():
            print("Pila vacia")
        else:
            return self.__data.pop()

    def push(self, value):
        self.__data.append(value)

    def peek(self):
        return self.__data[len(self.__data)-1]

    def to_string(self):
        for item in self.__data[::-1]:
            print(f"{item}")
            print("-----")

def recurcion(pila, n, m):
    if (pila.is_empty() or m == n):
        return
    newp = pila.peek()
    pila.pop()
    recurcion(pila, n, m+1)
    mt = (n/2)
    if mt == int(mt):
      if (m != mt and m != (mt-1)):
        pila.push(newp)
    else:
        if (m != int(n/2)):
          pila.push(newp)

def main():
  pila_2 = Stack()
  pila_2.push(1)
  pila_2.push(2)
  pila_2.push(3)
  pila_2.push(4)
  pila_2.push(5)
  pila_2.to_string()
  print("***************************************")
  recurcion(pila_2, pila_2.length(), 0)
  pila_2.to_string()

main()
