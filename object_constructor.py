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
        return ast

    def typed_variable(self, ast):  # noqa
        return objects.TypedVariable(ast)

    def declaration(self, ast):  # noqa
        return objects.DeclaredVariable(ast)

    def function_decl(self, ast):  # noqa
        return objects.FunctionDecl(ast)

    def multi_statements(self, ast):  # noqa
        return ast

    def statement(self, ast):  # noqa
        return ast

    def expression_stmt(self, ast):  # noqa
        return ast

    def return_stmt(self, ast):  # noqa
        return objects.ReturnStmt(ast)

    def if_statement(self, ast):  # noqa
        return objects.IfStmt(ast)

    def loop_statement(self, ast):  # noqa
        return objects.LoopStmt(ast)

    def primary_expression(self, ast):  # noqa
        return ast

    def function_call(self, ast):  # noqa
        return objects.FuncCall(ast)

    def postfix_expression(self, ast):  # noqa
        return objects.PostfixOp(ast)

    def unary_expression(self, ast):  # noqa
        return objects.UnaryOp(ast)

    def un_op(self, ast):  # noqa
        return ast

    def mult_expression(self, ast):  # noqa
        return objects.MulExpr(ast)

    def add_expression(self, ast):  # noqa
        return objects.AddExpr(ast)

    def shift_expression(self, ast):  # noqa
        return objects.ShiftExpr(ast)

    def relative_expression(self, ast):  # noqa
        return objects.RelExpr(ast)

    def equality_expression(self, ast):  # noqa
        return objects.EqExpr(ast)

    def and_expression(self, ast):  # noqa
        return objects.AndExpr(ast)

    def xor_expression(self, ast):  # noqa
        return objects.XorExpr(ast)

    def or_expression(self, ast):  # noqa
        return objects.OrExpr(ast)

    def land_expression(self, ast):  # noqa
        return objects.LAndExpr(ast)

    def lor_expression(self, ast):  # noqa
        return objects.LOrExpr(ast)

    def assign_expression(self, ast):  # noqa
        return objects.AssignExpr(ast)

    def expression(self, ast):  # noqa
        return ast

    def integer(self, ast):  # noqa
        return ast

    def string(self, ast):  # noqa
        return ast

    def char(self, ast):  # noqa
        return ast

    def literal(self, ast):  # noqa
        return objects.Literal(ast)

    def identifier(self, ast):  # noqa
        return objects.Identifier(ast)
