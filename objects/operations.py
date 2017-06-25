from .compiler_objects import Compilable, LineReference


class PostFixOp(LineReference, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.expr = ast.left
        self.op = ast.op
        self.type = ast.type

    def __str__(self):
        return f"<{self.__class__.__name__}: <OP: {self.op}> <EXPR: {self.expr}> <TYPE: {self.type}>>"

    def compile(self, ctx):
        return NotImplemented


class PreFixOp(LineReference, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.expr = ast.right
        self.op = ast.op

    def __str__(self):
        return f"<{self.__class__.__name__}: <OP: {self.op}> <EXPR: {self.expr}>>"

    def compile(self, ctx):
        return NotImplemented


class DuoOp(LineReference, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.left = ast.left
        self.right = ast.right
        self.op = ast.op

    def __str__(self):
        return f"<{self.__class__.__name__}: <LEFT: {self.left}> <OP: {self.op}> <RIGHT: {self.right}>>"

    def compile(self, ctx):
        return NotImplemented


class MulExpr(DuoOp):
    ...


class AddExpr(DuoOp):
    ...


class ShiftExpr(DuoOp):
    ...


class RelExpr(DuoOp):

    def __init__(self, ast):
        super().__init__(ast)
        self.op = {"<": "le",
                   ">": "me",
                   ">=": "meq",
                   "=<": "leq"}[self.op]


class EqExpr(DuoOp):

    def __init__(self, ast):
        super().__init__(ast)
        self.op = {"==": "eq",
                   "!=": "ne"}[self.op]


class LogicalBitwise(DuoOp):
    ...


class LogicalBoolean(DuoOp):
    ...


class AssignExpr(DuoOp):
    ...


class FuncCall(LineReference, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.name = ast.left
        self.vars = ast.op

    def __str__(self):
        return "<FUNCTION_CALL: <NAME: {0.name}> <VARS: {1}>>".format(
            self, ", ".join(str(i) for i in self.vars)
        )

    def compile(self, ctx):
        return NotImplemented
