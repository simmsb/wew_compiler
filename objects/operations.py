class FixOp:

    def __init__(self, ast):
        self.expr = ast["expr"]
        self.op = ast["op"]
        self.val = ast.get("val")

    def __str__(self):
        return f"<{self.__class__.__name__}: <OP: {self.op}> <EXPR: {self.expr}> <VAL: {self.val}>>"


class PostfixOp(FixOp):
    ...


class UnaryOp(FixOp):
    ...


class DuoOp:

    def __init__(self, ast):
        self.left = ast["left"]
        self.right = ast["right"]
        self.op = ast["op"]

    def __str__(self):
        return f"<{self.__class__.__name__}: <LEFT: {self.left}> <OP: {self.op}> <RIGHT: {self.right}>>"


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
    ...


class AndExpr(DuoOp):
    ...


class XorExpr(DuoOp):
    ...


class OrExpr(DuoOp):
    ...


class LAndExpr(DuoOp):
    ...


class LOrExpr(DuoOp):
    ...


class AssignExpr(DuoOp):
    ...


class FuncCall:

    def __init__(self, ast):
        self.name = ast["name"]
        self.vars = ast["vars"]

    def __str__(self):
        return "<FUNCTION_CALL: <NAME: {0.name}> <VARS: {1}>>".format(
            self, ", ".join(str(i) for i in self.vars)
        )
