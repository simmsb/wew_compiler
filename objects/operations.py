from .compiler_objects import Compilable, LineReference, CompileException
from .emitters import emit, Register

class ExpressionOp(LineReference, Compilable):

    is_lvalue = False

    def load_lvalue(self, register, ctx):
        yield NotImplemented

    def __init__(self, ast):
        super().__init__(ast)


class PostFixOp(ExpressionOp):


    def load_lvalue(self, register, ctx):
        if not self.expr.is_lvalue:
            raise CompileException(self.line, "Expression of list index is not a lvalue")
        if self.type == 'b':
            yield from self.expr.load_lvalue(Register.eee, ctx)  #load parent lvalue
            yield emit.psh(Register.eee)
            yield from self.op.compile(ctx)  # leaves in acumulator
            yield emit.pop(Register.eee)
            yield emit.sub(Register.eee, Register.acc)
            yield emit.mov(register, Register.acc)
        if self.type == 'a':
            yield from self.expr.load_lvalue(register, ctx) # if incrementing, our lvalue is the parent lvalue

    def __init__(self, ast):
        super().__init__(ast)
        self.expr = ast.left
        self.op = ast.op
        self.type = ast.type
        if self.type != 'f':
            self.is_lvalue = True

    def __str__(self):
        return f"<{self.__class__.__name__}: <OP: {self.op}> <EXPR: {self.expr}> <TYPE: {self.type}>>"

    def compile(self, ctx):
        if self.type == "f":
            # function call
            ...
            # TODO
        elif self.type == 'b':
            # array index
            yield from self.load_lvalue(Register.acc, ctx)  # loads our memory location into acc
            yield emit.mov(Register.acc, [Register.acc])  # dereference into accumulator
        elif self.type == 'a':
            # increment/ decrement
            yield from self.load_lvalue(Register.eee, ctx)  # load our memory location
            yield emit.mov(Register.acc, [Register.eee])  # store into eee
            if self.op == '++':
                yield emit.add(Register.acc, 1)  # increment value
            else:
                yield emit.sub(Register.acc, 1)
            yield emit.mov([Register.eee], Register.acc)  # return value to accumulator


class PreFixOp(ExpressionOp):

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
