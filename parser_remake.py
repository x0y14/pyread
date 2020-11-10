from pyread_token import *
from pyread_syntax import Syntax_Block, Syntax_Line


class Parser:
    def __init__(self, tkn):
        self.tkn = tkn
        super().__init__()
    

    def gen_line(self):
        lines = []
        ln = []
        n = 1
        for t in self.tkn:
            # print(t)
            ln.append(t)
            if type(t) == TKN_NEWLINE:
                lines.append(Syntax_Line(n, ln))
                n += 1
                ln = []
            elif type(t) == TKN_EOF:
                lines.append(Syntax_Line(n, ln))
                n += 1
                break
        return lines
    
    def add_nest_data(self, lines):
        continue_white_count = 0
        added_nest_data_lines = []

        for line in lines:
            for item in line.items:
                # print(item)
                if type(item) == TKN_WHITE_SPACE:
                    continue_white_count += 1
                else:
                    line.nest = continue_white_count
                    continue_white_count = 0
                    added_nest_data_lines.append(line)
                    break

        return added_nest_data_lines
    

    def add_line_need_data(self, lines):
        added_need_data_lines = []
        for line in lines:
            item_co = len(line.items)
            w = 0
            for it in line.items:
                if type(it) in [TKN_TAB, TKN_WHITE_SPACE, TKN_NEWLINE]:
                    w += 1
            if item_co == w:
                line.only_space = True
            added_need_data_lines.append(line)
        return added_need_data_lines
    
    # def gen_nest_data(self, lines):
    #     nest_data = {}
    #     for ln in lines:
    #         if nest_data.get(ln.nest) == None:
    #             nest_data[ln.nest] = {}
            