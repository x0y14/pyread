from pyread_token import *

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
    
    def gen_nest_data(self):
        n = 0
        block_parent = 0
        size = 4

        # code_block_nest = 0
        parents = []
        nests = []

        for ln in self.lined:
            for item in ln:
                if type(item) == TKN_WHITE_SPACE:
                    n += 1
                else:
                    if nests != []:
                        if nests[-1][1] < n:
                            # print(nests[-1], n)
                            # print('a')
                            print(f'{ "  "*int((int(n) / int(size))) } ({nests[-1][0]}) <- {ln[0].position.ln}は{nests[-1][0]}の子供')
                    nests.append((ln[0].position.ln, n))
                    if n == 0:
                        print(f'({ln[0].position.ln}行目) 深さ = {n}')
                        block_parent = ln[0].position.ln
                        parents.append(ln[0].position.ln)
                    else:
                        print(f'{ "  "*int((int(n) / int(size))) }|-- ({ln[0].position.ln}行目) 深さ = {n} 親ブロック: {block_parent}')
                    n = 0
                    break