from lexer import Lexer

if __name__ == '__main__':
    with open('./example.py') as f:
        lines = f.read()
    # for i in lines:
    lx = Lexer(lines)
    tks = lx.lex()
    for token in tks:
        print(token)