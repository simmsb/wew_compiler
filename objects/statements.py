from .compiler_objects import Compilable

class ReturnStmt(Compilable):

    def __init__(self, ast):
        self.expr = ast.expr

    def __str__(self):
        return f"<RETURN: <EXPR: {self.expr}>>"


class IfStmt(Compilable):

    def __init__(self, ast):
        self.expr = ast.expr
        self.statements = ast.stat
        self.else_ = ast.get("else")

    def __str__(self):
        return "<IF STATEMENT: <EXPR {0.expr}> <STATEMENTS: {1}> <ELSE: {0.else_}>>".format(
            self, ", ".join(map(str, self.statements))
        )


class LoopStmt(Compilable):

    def __init__(self, ast):
        self.type = ast.type
        self.expr = ast.expr
        self.statements = ast.stat

    def __str__(self):
        return "<LOOP: <TYPE: {0.type}> <EXPR: {0.expr}> <STATEMENTS: {1}>>".format(
            self, ", ".join(map(str, self.statements))
        )


class ExpressionStmt(Compilable):

    def __init__(self, ast):
        self.expr = ast.expr

    def __str__(self):
        return f"<EXPRESSION STMT: {self.expr}>"
