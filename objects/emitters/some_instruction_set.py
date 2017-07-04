from .instructions import ops0, ops1, ops2, Instruction, pack_address, Register

from ..compiler_objects import VariableReference

class Instruction:
    def __init__(self, instr, *args):
        self.instr = instr
        self.args = args


class Emitter:
    def __getattr__(self, name):
        if hasattr(ops0, name):
            return instruction_helper(ops0(name), 0)
        if hasattr(ops1, name):
            return instruction_helper(ops1(name), 1)
        if hasattr(ops2, name):
            return instruction_helper(ops2(name), 2)
        if hasattr(self, name):
            return getattr(self, name)
        raise Exception(f"Instruction {name} is not a valid instruction "
                            f"in the set {__file__}.")



def instruction_helper(instr, n_args):
    def receiver(*args):
        if len(args) != n_args:
            raise Exception(f"Instruction {instr} expects {n_args} but "
                            f"{len(args)} were given.")
        return AbstractInstruction(instr, args)

#
#  if int, dereference
#  if register, dereference
#  if variableref, resolve location into ggg, then dereference that
#


class AbstractInstruction:
    def __init__(self, instr, args):
        self.instr = instr
        self.args = args
        self.pre_instructions = []
        self.to_use = [Register.ggg, Register.fff]

    def resolve_arg(self, arg):
        if isinstance(i, int):
            return i
        if isinstance(i, VariableReference):
            reg_used = self.to_use.pop()
            pre = [
                Instruction(ops2.sub, Register.epb, i.var.size),
                Instruction(ops2.mov, reg_used, Register.acc)
            ]

            self.pre_instructions += pre
            return pack_address(reg_used, is_deref=True, is_reg=True)

        if isinstance(i, list):  # dereference, child will
            pre, _ = self.resolve_arg(i[0])
            return pack_address(pre, is_deref=True)

        if isinstance(i, Register):
            return pack_address(i, is_reg=True)


    def emit(self):
        args = [self.resolve_arg(i) for i in self.args]
        yield from self.pre_instructions
        yield Instruction(self.instr, *args)

 
emit = Emitter()
