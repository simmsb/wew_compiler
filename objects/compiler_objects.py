from abc import ABCMeta, abstractmethod


class Compilable(metaclass=ABCMeta):
    """Base class of compilable Objects."""

    @abstractmethod
    def compile(self, ctx):
        """Compile an object."""
        raise NotImplemented


class LineReference:
    """Grabs line reference from ast."""

    def __init__(self, ast):
        self.line = ast.parseinfo.line


class VariableReference:
    """A reference to a variable.

    contains info on scope for reslolving position at later stage
    """

    def __init__(self, var, name, type_, parent):
        self.var = var
        self.name = name
        self.type = type_
        self.parent = parent


class CompileException(Exception):
    def __init__(self, line, *args, **kwargs):
        self.line = line
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "Exception on line ({0.line}): {1}".format(
            self,
            super().__str__()
        )

    def __repr__(self):
        return "{0.__class__.__name__}({1})".format(
            self,
            self.__str__()
        )
