from .compiler_objects import LineReference


class Literal(LineReference):

    def __init__(self, ast):
        super().__init__(ast)
        self.value = ast.val
        self.type = ast.type

    def __str__(self):
        return f"<LITERAL: <VALUE: {self.value}> <TYPE: {self.type}>>"


class Identifier(LineReference):

    def __init__(self, ast):
        super().__init__(ast)
        self.name = ast.name

    def __str__(self):
        return f"<IDENTIFIER: <NAME: {self.name}>>"
