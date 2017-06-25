"""Module holding all object types together."""
from .declarations import FunctionDecl, TypedVariable, Scope
from .literals import Identifier, Literal
from .operations import *
from .statements import ExpressionStmt, IfStmt, LoopStmt, ReturnStmt
from .types import parse as parse_type
from .types import Float, Int, Pointer
