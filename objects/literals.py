class Literal:

    def __init__(self, ast):
        print(ast)
        self.value = ast["val"]
        self.type = ast["type"]

    def __str__(self):
        return f"<LITERAL: <VALUE: {self.value}> <TYPE: {self.type}>>"


class Identifier:

    def __init__(self, ast):
        self.name = ast

    def __str__(self):
        return f"<IDENTIFIER: <NAME: {self.name}>>"
