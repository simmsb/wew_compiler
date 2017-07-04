from .compiler_objects import LineReference, Compilable
from .emitters import emit, Register

class Literal(LineReference, Compilable):

    is_lvalue = False

    def __init__(self, ast):
        super().__init__(ast)
        self.value = ast.val
        self.type = ast.type

    def __str__(self):
        return f"<LITERAL: <VALUE: {self.value}> <TYPE: {self.type}>>"

    def compile(self, ctx):
        if self.type == "int":
            yield emit.mov(Register.acc, self.value)
        elif self.type == "str":
            yield emit.mov(Register.acc, ctx.string_len)
            ctx.strings.append(self.value)  # add string to context (to be included in the binary later)
            ctx.string_len += len(self.value)
        elif self.type == 'chr':
            yield emit.mov(Register.acc, ord(self.value))


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

    def compile(self, ctx):
        yield from self.load_lvalue(Register.acc, ctx)
        yield emit.mov(Register.acc, [Register.acc])
