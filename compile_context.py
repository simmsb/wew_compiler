from objects.compiler_objects import CompileException, VariableReference


class CompileContext:
    """Compile context is the context holding defined functions and labels so far."""

    def __init__(self):
        self.functions = {}
        self.scope_chain = []

    def insert_function(self, function):
        if function.name in self.functions:
            raise Exception(f"Function {function.name} is declared twice.")
        self.functions[function.name] = function

    def init_compile(self):
        self.scope_chain = []
        for i in self.functions:
            self.scope_chain.append(i)
            i.compile()
            self.scope_chain.pop()

    @property
    def current_scope(self):
        return self.scope_chain[-1]

    def lookup_variable(self, variable, callee):
        """Lookup a variable in scope chain."""
        for i in reversed(self.scope_chain):
            var = i.lookup_variable(self, variable)
            if var is not None:
                return VariableReference(var.name, var.type, i)

        raise CompileException(callee.line,
                               f"Variable <{variable}> is not declared in the scope: "
                               + self.current_scope.name)
