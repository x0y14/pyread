from lexer import Lexer
from parser import Parser
from pprint import pprint



if __name__ == '__main__':
    lxr = Lexer(file_path='./example.py')
    tkn = lxr.lex()
    
    psr = Parser(tkn=tkn)
    r = psr.gen_line()
    # pprint(r)
    psr.gen_nest_data()# AST用に関数の深さみたいなのを表示できるように