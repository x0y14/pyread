from lexer import Lexer
# from parser import Parser
from parser_remake import Parser

from pprint import pprint



if __name__ == '__main__':
    # lxr = Lexer(file_path='./example.py')
    lxr = Lexer(file_path='/Users/x0y14/dev/python/pyread/parser_remake.py')
    tkn = lxr.lex()
    
    psr = Parser(tkn=tkn)
    lines = psr.gen_line()
    has_nest_data_lines = psr.add_nest_data(lines)
    has = psr.add_line_need_data(has_nest_data_lines)
    for l in has:
        print(l.ln_num, l.nest, f"only white : {l.only_space}")
    # psr.gen_nest_data(has)
