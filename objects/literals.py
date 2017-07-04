from .compiler_objects import LineReference
from .emitters import emit

class Literal(LineReference):

    is_lvalue = False

    def __init__(self, ast):
        super().__init__(ast)
        self.value = ast.val
        self.type = ast.type

    def __str__(self):
        return f"<LITERAL: <VALUE: {self.value}> <TYPE: {self.type}>>"


class Identifier(LineReference):

    is_lvalue = True

    def load_lvalue(self, register, ctx):
        var = ctx.lookup_variable(self.name, self)
        yield from var.load_lvalue()
        # ezpz

    def __init__(self, ast):
        super().__init__(ast)
        self.name = ast.name

    def __str__(self):
        return f"<IDENTIFIER: <NAME: {self.name}>>"
