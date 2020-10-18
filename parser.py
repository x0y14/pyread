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
        parent = 0
        for ln in self.lined:
            for item in ln:
                if type(item) == TKN_WHITE_SPACE:
                    n += 1
                else:
                    if n == 0:
                        print(f'親({ln[0].position.ln}), 深さ = {n}')
                        parent = ln[0].position.ln
                    else:
                        # print(ln[0].position.ln, n)
                        print(f'|-- 子供({ln[0].position.ln}), 深さ = {n}')
                    n = 0
                    break