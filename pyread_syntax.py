import dataclasses
from typing import Tuple
from typing import List


@dataclasses.dataclass
class Syntax_Block:
    def __init__(self, ln):
        self.child = []
        self.ln = ln
        self.child_ln = []
    
    def set_child(self, token):
        self.child.append(token)
    
    def set_child_ln(self, ln):
        self.child_ln.append(ln)

class Syntax_Line:
    def __init__(self, ln_n, items):
        self.ln_num = ln_n
        self.items = items
        self.nest = 0
        self.only_space = False