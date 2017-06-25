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
<<<<<<< HEAD
    """Parse pointer types into POINTER TO <>."""
=======
    """Parse pointer types into POINTER TO <>"""
>>>>>>> d83d4a16a290ffed8364345cdb9c75f0be2d33e5
    match = {"int": Int,
             "float": Float}[typ.t]()
    for _ in typ.p:
        match = Pointer(match)
    return match
