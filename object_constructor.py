"""Object tree generation."""
import objects
from wewparser import WewSemantics


class ObjectConstructor(WewSemantics):
    """Class used to generate program objects from ast, as a means of preprocessing."""

    def _default(self, ast):
        print(f"DEFAULT: {ast}")
        return ast

    def start(self, ast):  # noqa
        return ast

    def types(self, ast):  # noqa
        print(f"TYPE: {ast}")
        return ast

    def pointer(self, ast):  # noqa
        print(f"POINTER: {ast}")
        return ast

    def declare_types(self, ast):  # noqa
        print(f"Decl type: {ast}")
        return ast

    def instance_types(self, ast):  # noqa
        print(f"Inst type: {ast}")
        return ast

    def typed_variable(self, ast):  # noqa
        return objects.TypedVariable(ast[0], ast[1])

    def declaration(self, ast):  # noqa
        print("Declaration: {ast}")
        return ast

    def function_decl(self, ast):  # noqa
        return objects.FunctionDecl(ast)

    def statement(self, ast):  # noqa
        print(f"Statement: {ast}")
        return ast

    def return_stmt(self, ast):  # noqa
        print(f"Ret: {ast}")
        return ast

    def if_statement(self, ast):  # noqa
        print(f"IF: {ast}")
        return ast

    def loop_statement(self, ast):  # noqa
        print(f"LOOP: {ast}")
        return ast

    def scope(self, ast):  # noqa
        print(f"SCOPE: {ast}")
        return ast

    def assignment(self, ast):  # noqa
        print(f"ASSIGN: {ast}")
        return ast

    def function_call(self, ast):  # noqa
        print(f"FunCall: {ast}")
        return ast

    def function_call_stmt(self, ast):  # noqa
        print(f"FunCallStmt: {ast}")
        return ast

    def expression(self, ast):  # noqa
        print(f"EXPR: {ast}")
        return ast

    def comparisons(self, ast):  # noqa
        return ast

    def comparison_stmt(self, ast):  # noqa
        print(f"Comp stmt: {ast}")
        return ast

    def prefix_expression(self, ast):  # noqa
        print(f"Prefix expr: {ast}")
        return ast

    def postfix_expression(self, ast):  # noqa:
        print(f"Postfix expr: {ast}")
        return ast

    def integer(self, ast):  # noqa
        print(f"Iteger Literal: {ast}")
        return ast

    def string(self, ast):  # noqa
        print("String Literal: {ast}")
        return ast

    def literal(self, ast):  # noqa
        print("Literal: {ast}")
        return ast

    def var_name(self, ast):  # noqa
        print("Var Name: {ast}")
        return ast

    def infix_expression(self, ast):  # noqa
        print("Infix Expr: {ast}")
        return ast

    def mul_expr(self, ast):  # noqa
        return ast

