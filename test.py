from lexer import Lexer

if __name__ == '__main__':
    lx = Lexer("name = 3")
    tks = lx.lex()
    for token in tks:
        print(token)