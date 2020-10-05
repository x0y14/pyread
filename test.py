from lexer import Lexer
from pyread_token import *

if __name__ == '__main__':
    with open('./example.py') as f:
        lines = f.read()
    lx = Lexer(lines)
    tks = lx.lex()
    data = [
        PYK_DEF(),# def
        TKN_WHITE_SPACE(),# def 
        TKN_IDENTIFIER(data='main'),# def main
        TKN_PARENTHESES_OPEN(),# def main(
        TKN_PARENTHESES_CLOSE(),# def main()
        TKN_COLON(),# def main():
        TKN_NEWLINE(),

        TKN_WHITE_SPACE(),
        TKN_WHITE_SPACE(),
        TKN_WHITE_SPACE(),
        TKN_WHITE_SPACE(),
        TKN_IDENTIFIER(data='print'),#    print
        TKN_PARENTHESES_OPEN(),#    print(
        TKN_STRING(data='hello, python'),#    print('hello, python'
        TKN_PARENTHESES_CLOSE(),#    print('hello, python')
        TKN_NEWLINE(),

        TKN_WHITE_SPACE(),
        TKN_WHITE_SPACE(),
        TKN_WHITE_SPACE(),
        TKN_WHITE_SPACE(),
        TKN_IDENTIFIER(data='my_age'),#    my_age
        TKN_WHITE_SPACE(),
        TKN_EQUAL(),#    my_age =...10/6深夜
        


    ]