#!/bin/python3
class Buffer:
    ls = []
    s = 0
    def __init__(self):
        # конструктор без аргументов
       self.ls = []
       self.s = 0
    def add(self, *a):
        # добавить следующую часть последовательности
        self.ls.extend (a)
        if len(self.ls) // 5 > 0:
            for i in range (0,5):
                self.s += self.ls.pop(0)
            print(self.s)
            self.s = 0
            self.add()
    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.ls

