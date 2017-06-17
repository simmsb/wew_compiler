class CompileContext:
    """Compile context is the context holding defined functions and labels so far."""

    def __init__(self):
        self.functions = {}
        self.current_scope = {}
        self.current_function = None

    def insert_function(self, function):
        if function.name in self.functions:
            raise Exception(f"Function {function.name} is declared twice.")
        self.functions[function.name] = function

    def init_compile(self):
        for i in self.functions:
            self.current_function = i
            i.compile()
