"""Object tree generation."""
import objects


class ObjectConstructor(object):

    def start(self, ast):  # noqa
        return ast

    def types(self, ast):  # noqa
        return ast

    def pointer(self, ast):  # noqa
        return ast

    def instance_types(self, ast):  # noqa
        return objects.parse_type(ast)

    def typed_variable(self, ast):  # noqa
        return objects.TypedVariable(ast)

    def declaration(self, ast):  # noqa
        return objects.DeclaredVariable(ast)

    def function_decl(self, ast):  # noqa
        return objects.FunctionDecl(ast)

    def scope(self, ast):  # noqa
        return objects.Scope(ast)

    def statement(self, ast):  # noqa
        return ast

    def expression_stmt(self, ast):  # noqa
        return objects.ExpressionStmt(ast)

    def return_stmt(self, ast):  # noqa
        return objects.ReturnStmt(ast)

    def if_statement(self, ast):  # noqa
        return objects.IfStmt(ast)

    def loop_statement(self, ast):  # noqa
        return objects.LoopStmt(ast)

    def expression(self, ast):  # noqa
        return ast

    def assign(self, ast):  # noqa
        return objects.AssignExpr(ast)

    def logical(self, ast):  # noqa
        return ast

    def bitwise(self, ast):  # noqa
        return objects.LogicalBitwise(ast)

    def boolean(self, ast):  # noqa
        return objects.LogicalBoolean(ast)

    def comparison(self, ast):  # noqa
        return ast

    def equality(self, ast):  # noqa
        return objects.EqExpr(ast)

    def relation(self, ast):  # noqa
        return objects.RelExpr(ast)

    def shift(self, ast):  # noqa
        return ast

    def bitshift(self, ast):  # noqa
        return objects.ShiftExpr(ast)

    def bin_expr(self, ast):  # noqa
        return ast

    def addition(self, ast):  # noqa
        return objects.AddExpr(ast)

    def subtraction(self, ast):  # noqa
        return objects.AddExpr(ast)

    def term(self, ast):  # noqa
        return ast

    def multiplication(self, ast):  # noqa
        return objects.MulExpr(ast)

    def division(self, ast):  # noqa
        return objects.MulExpr(ast)

    def unop(self, ast):  # noqa
        return objects.PreFixOp(ast)

    def postop(self, ast):  # noqa
        if ast.type == 'f':
            return objects.FuncCall(ast)
        return objects.PostFixOp(ast)

    def post_wrap(self, ast):  # noqa
        return ast

    def unary(self, ast):  # noqa
        return ast

    def factor(self, ast):  # noqa
        return ast

    def subexpression(self, ast):  # noqa
        return ast

    def literal(self, ast):  # noqa
        return objects.Literal(ast)

    def integer(self, ast):  # noqa
        return ast

    def string(self, ast):  # noqa
        return ast

    def char(self, ast):  # noqa
        return ast

    def identifier(self, ast):  # noqa
        return objects.Identifier(ast)
