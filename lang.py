import pyparsing as pp
from pyparsing import pyparsing_common as pp_c


def choice_list(*items):
    """Construct a MatchFirst group of a list of keywords"""
    return pp.MatchFirst(map(pp.Keyword, items))


def pwrapped(expr):
    """Return expression wrapped in parentheses."""
    return lparen + expr + rparen


number = pp_c.hex_integer | pp_c.integer

semicol = pp.Literal(";").suppress()
equals = pp.Literal(":=").suppress()

opening_curly_bracket = pp.Literal("{").suppress()
closing_curly_bracket = pp.Literal("}").suppress()

lparen = pp.Literal("(").suppress()
rparen = pp.Literal(")").suppress()
lsqrbrk = pp.Literal("[").suppress()
rsqrbrk = pp.Literal("]").suppress()

comparison = pp.oneOf("== != > < >= <=")
addsub = pp.oneOf("+ -")
muldiv = pp.oneOf("* /")

oplist = [(muldiv, 2, pp.opAssoc.LEFT),
          (addsub, 2, pp.opAssoc.LEFT)]

types = choice_list("int",)

pointer = types + pp.OneOrMore("*")
list_type = types + lsqrbrk + number + rsqrbrk


declare_types = types | pointer | list_type
return_types = types | pointer

var_type = return_types + pp_c.identifier

declaration = declare_types + pp_c.identifier + semicol

scope = pp.Forward()
statement = pp.Forward()
expression = pp.Forward()

scope <<= opening_curly_bracket + pp.OneOrMore(scope ^ statement) + closing_curly_bracket

function_decl = var_type + pwrapped(pp.delimitedList(var_type)) + scope


# statements
if_stmt = pp.Keyword("if") + pwrapped(expression) + scope
elif_stmt = if_stmt + pp.Keyword("elif") + pwrapped(expression) + scope
else_stmt = (elif_stmt ^ if_stmt) + pp.Keyword("else") + expression + scope

while_stmt = pp.Keyword("while") + pwrapped(expression) + scope

assignment_stmt = pp_c.identifier + equals + expression + semicol

function_call_stmt = pp_c.identifier + pwrapped(pp.delimitedList(expression))


# TODO: build math, combine expressions (function call, math, variable, literals)
