class FunctionDecl:

    def __init__(self, ast):
        self.return_type = ast["type"]
        self.name = ast["name"]
        self.params = ast["params"]
        self.code = ast["stat"]

    def __str__(self):
        return "<FUNCTION: <return: {0.return_type}> <name: {0.name}> <params: {1}> <code: {2}>>".format(
            self, list(map(str, self.params)), list(map(str, self.code))
        )


class TypedVariable:

    def __init__(self, ast):
        self.type = ast["type"]
        self.name = ast["name"]

    def __str__(self):
        return f"<VARIABLE <NAME:{self.name}> <TYPE:{self.type}>>"


class DeclaredVariable:

    def __init__(self, ast):
        self.type = ast["type"]
        self.pt = ast.get("pt")
        self.ref = ast.get("ref")

    def __str__(self):
        return (f"<DECLVAR: <TYPE: {self.type}> <pt: {self.pt}>"
                f"<REF: {self.ref}>>")
