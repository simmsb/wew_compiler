import types


class FunctionDecl:

    def __init__(self, ast):
        self.return_type = ast.type
        self.name = ast.name
        self.params = ast.params
        self.code = ast.stat
        self.compiled = None

        self.scope = {}  # scope holding variables

    def __str__(self):
        return "<FUNCTION: <return: {0.return_type}> <name: {0.name}> <params: {1}> <code: {2}>>".format(
            self, ", ".join(map(str, self.params)), ", ".join(map(str, self.code))
        )

    def compile(self, ctx):
        self.complied = [i.compile() for i in self.code]


class TypedVariable:

    def __init__(self, ast):
        self.type = ast.type
        self.name = ast.name

    def __str__(self):
        return f"<VARIABLE <NAME:{self.name}> <TYPE:{self.type}>>"


class DeclaredVariable:

    def __init__(self, ast):
        self.type = ast.type
        self.pt = ast.get("pt")
        self.ref = ast.get("ref")
        if self.ref == 'list':
            self.type = types.Pointer(self.type)
            # Wrap in a pointer for list declaration

    def __str__(self):
        return (f"<DECLVAR: <TYPE: {self.type}> <pt: {self.pt}>"
                f"<REF: {self.ref}>>")
