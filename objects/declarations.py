import types

from .compiler_objects import Compilable, VariableReference

class FunctionDecl(Compilable):

    def __init__(self, ast):
        self.return_type = ast.type
        self.name = ast.name
        self.params = ast.params
        self.code = ast.stat
        self.compiled = None

        self.scope = {i.name: i for i in self.params}
        # scope holding variables, prefill with parameters

        # we might decide to build calling conventions

    def __str__(self):
        return "<FUNCTION: <return: {0.return_type}> <name: {0.name}> <params: {1}> <code: {2}>>".format(
            self, ", ".join(map(str, self.params)), ", ".join(map(str, self.code))
        )

    def declare_variable(self, var):
        self.scope[var.name] = var

    def compile(self, ctx):
        self.complied = [i.compile(ctx) for i in self.code]

    def lookup_variable(self, variable):
        """Return a VariableReference object containing a variables parameters."""
        var = self.scope.get(variable)
        if var is None:
            raise Exception(f"Variable <{variable}> is not declared")
        return VariableReference(var.name, var.type, self)

class Variable:
    def __init__(self, type_, name):
        self.type = type_
        self.name = name

class TypedVariable(Variable):

    def __init__(self, ast):
        super().__init__(ast.type,
                         ast.name)

    def __str__(self):
        return f"<PARAM VARIABLE <NAME:{self.name}> <TYPE:{self.type}>>"


class DeclaredVariable(Variable, Compilable):

    def __init__(self, ast):
        super().__init__(ast.type,
                         ast.name)
        self.pt = ast.get("pt")
        self.ref = ast.get("ref")
        if self.ref == 'list':
            self.type = types.Pointer(self.type)
            # Wrap in a pointer for list declaration

    def __str__(self):
        return (f"<DECLVAR: <TYPE: {self.type}> <NAME: {self.name}> <pt: {self.pt}>>")

    def compile(self, ctx):
        ctx.current_function.declare_variable(self)
