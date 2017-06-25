import types

from .compiler_objects import Compilable, CompileException, LineReference


class Scoped(LineReference):
    def __init__(self, ast, scope: dict):
        super().__init__(ast)
        self.scope = scope

    def lookup_variable(self, ctx, variable):
        return self.scope.get(variable)

    def declare_variable(self, ctx, variable):
        """Add variable to scope."""
        if variable.name in self.scope:
            raise CompileException(variable.line, f"Variable <{variable}> is already declared in the scope: "
                                   + ctx.current_scope.name)
        self.scope[variable.name] = variable


class FunctionDecl(Scoped, Compilable):

    def __init__(self, ast):
        self.return_type = ast.type
        self.name = ast.name
        self.params = ast.params
        self.code = ast.stat  # this is a scope object now

        super().__init__(ast, {i.name: i for i in self.params})
        # scope holding variables, prefill with parameters

        # we might decide to build calling conventions

    def __str__(self):
        return "<FUNCTION: <return: {0.return_type}> <name: {0.name}> <params: {1}> <code: {2}>>".format(
            self, ", ".join(map(str, self.params)), self.code
        )

    def compile(self, ctx):
        yield from (i.compile(ctx) for i in self.code)


class Scope(Scoped, Compilable):

    def __init__(self, ast):
        super().__init__(ast, {})
        self.code = ast.code
        self.parent = None

    def compile(self, ctx):
        self.parent = ctx.current_function[-1]
        # save the parent scope
        yield from (i.compile(ctx) for i in self.code)

    @property
    def name(self):
        return f"{self.parent.name} -> scope:{self.line}"

    def __str__(self):
        return "<SCOPE: " + ", ".join(map(str, self.code)) + ">"


class Variable(LineReference):

    def __init__(self, ast):
        super().__init__(ast)
        self.type = ast.type
        self.name = ast.name


class TypedVariable(Variable):

    def __init__(self, ast):
        super().__init__(ast)

    def __str__(self):
        return f"<PARAM VARIABLE <NAME:{self.name}> <TYPE:{self.type}>>"


class DeclaredVariable(Variable, Compilable):

    def __init__(self, ast):
        super().__init__(ast)
        self.pt = ast.get("pt")
        self.ref = ast.get("ref")
        if self.ref == 'list':
            self.type = types.Pointer(self.type)
            # Wrap in a pointer for list declaration

    def __str__(self):
        return (f"<DECLVAR: <TYPE: {self.type}> <NAME: {self.name}> <pt: {self.pt}>>")

    def compile(self, ctx):
        ctx.current_scope.declare_variable(ctx, self)
