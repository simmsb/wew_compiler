def format_ast(string, indent=2):
    """Format a ast with specified indentation per block."""
    blocks = ""
    brackets = -1

    while string:
        char, string = string[0], string[1:]
        if char == "<":
            brackets += 1
            blocks += "\n" + " " * indent * brackets + "<"
        elif char == ">":
            while char == ">" and string:
                char, string = string[0], string[1:]
                brackets -= 1
                blocks += ">"
        else:
            blocks += char
    return blocks
