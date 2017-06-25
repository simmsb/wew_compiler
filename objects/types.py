class Int:
    size = 1

    def __str__(self):
        return "<INTEGER>"


class Float:
    size = 2

    def __str__(self):
        return "<FLOAT>"


class Pointer:
    def __init__(self, to):
        self.to = to

    def __str__(self):
        return f"<POINTER to {self.to}>"


def parse(typ):
    """Parse pointer types into POINTER TO <>"""
    match = {"int": Int,
             "float": Float}[typ.t]()
    for _ in typ.p:
        match = Pointer(match)
    return match
