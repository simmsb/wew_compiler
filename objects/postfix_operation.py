class PostfixOp:
    def __init__(self, ast):
        self.expr = ast["expr"]
        self.optype = ast["op"]
