"""Compiler."""
from ast_formatter import format_ast
from compile_context import CompileContext
from object_constructor import ObjectConstructor
from wewparser import WewParser


def parse_with_semantics(text: str, semantics: object=None):
    """Parse a file with given semantics."""
    parser = WewParser(semantics=semantics())
    return parser.parse(text)


if __name__ == '__main__':
    import sys

    with open(sys.argv[1]) as f:
        text = f.read()
    ast = parse_with_semantics(text, ObjectConstructor)

    context = CompileContext()

    for i in ast:
        print(format_ast(str(i)))
        context.insert_function(i)
