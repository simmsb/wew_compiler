"""Compiler."""
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
    print(ast)
