from abc import ABCMeta, abstractmethod

class Compilable(metaclass=ABCMeta):

    @abstractmethod
    def compile(self, ctx):
        """Compile an object"""
        raise NotImplemented

class VariableReference:
    def __init__(self, name, type_, parent):
        self.name = name
        self.type = type_
        self.parent = parent
