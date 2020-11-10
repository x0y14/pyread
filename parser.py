from pyread_token import *
from pyread_syntax import Syntax_Block

class Parser:
    def __init__(self, tkn):
        self.tkn = tkn
        self.lined = []
        super().__init__()
    

    def gen_line(self):
        lines = []
        ln = []
        for t in self.tkn:
            # print(t)
            ln.append(t)
            if type(t) == TKN_NEWLINE:
                lines.append(ln)
                ln = []
            elif type(t) == TKN_EOF:
                lines.append(ln)
                break
        self.lined = lines
        return lines
    

    def is_space_only(self, line):
        item_c = len(line)
        i = 0
        for it in line:
            if type(it) in [TKN_WHITE_SPACE, TKN_NEWLINE, TKN_TAB]:
                i += 1
        if item_c == i:
            return True
        else:
            return False


    
    def gen_nest_data(self):
        n = 0
        block_parent = 0
        size = 4

        parents = []
        nests = []

        syntax_dict = {}

        for ln in self.lined:
            this_line = ln[0].position.ln
            syntax_dict[this_line] = {'parent': 0, 'sub_parent': []}

            if (len(ln) == 1) and (type(ln[0]) == TKN_NEWLINE):
                print(f'{ln[0].position.ln} empty line')
                continue

            elif self.is_space_only(ln) == True:
                print(f'{ln[0].position.ln} empty line')
                continue

            for item in ln:
                if type(item) == TKN_WHITE_SPACE:
                    n += 1
                else:
                    if nests != []:
                        if nests[-1][1] < n:
                            # print(nests[-1], n)
                            # print('a')
                            print(f'{ "  "*int((int(n) / int(size))) } {ln[0].position.ln}は{nests[-1][0]}の子供')
                            syntax_dict[this_line]['sub_parent'].append(nests[-1][0])
                            # print('[nia parent]')
                        # else:
                        #     # print(';')

                    nests.append((ln[0].position.ln, n))
                    if n == 0:
                        print(f'({ln[0].position.ln}行目) 深さ = {n}')
                        block_parent = ln[0].position.ln
                        parents.append(ln[0].position.ln)
                        # print('[parent]')
                    else:
                        print(f'{ "  "*int((int(n) / int(size))) }|-- ({ln[0].position.ln}行目) 深さ = {n} 親ブロック: {block_parent}')
                        syntax_dict[this_line]['parent'] = block_parent
                    n = 0
                    break
        print(parents)
        return syntax_dict