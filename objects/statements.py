from .compiler_objects import Compilable, LineReference


class ReturnStmt(LineReference, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.expr = ast.expr

    def __str__(self):
        return f"<RETURN: <EXPR: {self.expr}>>"

    def compile(self, ctx):
        return NotImplemented


class IfStmt(LineReference, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.expr = ast.expr
        self.statements = ast.stat
        self.else_ = ast.get("else")

    def __str__(self):
        return "<IF STATEMENT: <EXPR {0.expr}> <STATEMENTS: {1}> <ELSE: {0.else_}>>".format(
            self, self.statements
        )

    def compile(self, ctx):
        return NotImplemented


class LoopStmt(LineReference, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.type = ast.type
        self.expr = ast.expr
        self.statements = ast.stat

    def __str__(self):
        return "<LOOP: <TYPE: {0.type}> <EXPR: {0.expr}> <STATEMENTS: {1}>>".format(
            self, self.statements
        )

    def compile(self, ctx):
        return NotImplemented


class ExpressionStmt(LineReference, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.expr = ast.expr

    def __str__(self):
        return f"<EXPRESSION STMT: {self.expr}>"

    def compile(self, ctx):
        return NotImplemented
