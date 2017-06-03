class TypedVariable:

    def __init__(self, ast):
        self.type = ast["type"]
        self.name = ast["name"]

    def __str__(self):
        return f"<VARIABLE <NAME:{self.name}> <TYPE:{self.type_}>>"
