class PriorityQueue:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def enqueue(self, valor : str, priorida: int) -> None:
            self.__data.append((valor, priorida))
            self.__data = self.order(self.__data)

    def dequeue(self):
        if not is_empty():
            return self.__data.pop(0)
        else:
            return None

    def order (self, cola):
        return sorted(cola, key=lambda v: v[1])

    def to_string(self):
        cl = ""
        for elem in self.__data:
            cl = cl + "| " + str(elem)
        cl = cl + "| "
        return cl
