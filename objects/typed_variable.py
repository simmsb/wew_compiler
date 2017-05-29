class TypedVariable:

    def __init__(self, type_, name):
        self.type = type_
        self.name = name

    def __str__(self):
        return f"<VARIABLE name:{self.name} type:{self.type_}"
