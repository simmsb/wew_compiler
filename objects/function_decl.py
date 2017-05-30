class FunctionDecl:

    def __init__(self, args):
        self.return_type = args["typ"]
        self.name = args["name"]
        self.params = args["params"]
        self.code = args["exp"]

    def __str__(self):
        return "<FUNCTION D: <return: {0.return_type}> <name: {0.name}> <params: {0.params}> <code: {0.code}>>".format(self)
