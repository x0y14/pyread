from modules.string_converter import StringConverter
import re
from pyread_token import *

class Lexer:
    def __init__(self, file_path):
        with open(file_path) as f:
            lines = f.read()
        self.file_path = file_path
        self.input = lines
        self.pos = 0
        self.in_string = False
        self.first_char_of_line = True

        self.ln = 1
        self.col = 1
        super().__init__()
    

    def is_eof(self) -> bool:
        # self.pos+1なのは数えるのが0,1,2,3,...だからです(多分あってる)
        # len()だとそのままの文字数を返してくるので、1ずれてしまうので。
        # print(f'[is_eof] MAX: {len(self.input)}, NOW: {self.pos+1}')
        q = self.pos >= len(self.input)
        # if q:
            # print(f'= End Of File =')
        #     pass

        return q
    

    def can_move_next(self) -> bool:
        # 次の文字あるんですか？
        if self.is_eof():
            return False
        try:
            _ = self.input[self.pos+1]
            # print(_)
            return True
        except:
            return False
    

    def is_not_over_eof(self):
        if (self.is_eof() == False) and (self.can_move_next() == True):
            return True
        else:
            return False
    

    def get_char(self) -> str:
        # 動かないでその場の文字を返します。
        return self.input[self.pos]
    
    def get_position(self) -> int:
        return self.pos
    

    def get_next_char(self) -> str:
        if self.can_move_next():
            return self.input[self.pos+1]
        else:
            raise IndexError(f'文字列を超過しました。文字数: {len(self.input)}, 現在の位置: {self.pos}, 要求した位置: {self.pos+1}')
        
    
    def is_next_char(self, target='') -> bool:
        return self.get_next_char() == target
    

    def consume_char(self) -> str:
        # その場の文字を返し、次へ移動します。
        c = self.input[self.pos]
        # print(f'[consume_char] pos: {self.pos}, c: {c}')
        self.pos += 1
        self.add_col_number()
        return c
    

    def consume_while(self, target='') -> str:
        p_s = self.get_position()
        col_s = self.get_col_number()

        # 次の文字が与えられたものと一致している間、consume_char()をし続けます。
        result = ''
        if target == '':
            p_e = self.get_position()
            col_e = self.get_col_number()

            return (result, POSITION_DATA(self.file_path, p_s, p_e))
        while self.is_eof() is False:
            if self.get_char() == target:
                result += self.consume_char()
                if self.is_next_char(target) == False:
                    break
        p_e = self.get_position()
        col_e = self.get_col_number()

        return (result, POSITION_DATA(self.file_path, p=(p_s, p_e), ln=self.get_ln_number(), col=(col_s, col_e)))
    

    def consume_while_variable_func_name(self):
        col_s = self.get_col_number()
        p_s = self.get_position()
        # 関数名や変数などに。
        result = ''
        while self.is_eof() == False:
            c = self.get_char()
            if re.match(r'[a-zA-Z0-9_]', c):
                result += self.consume_char()
            else:
                break
        p_e = self.get_position()
        col_e = self.get_col_number()
        return (result, POSITION_DATA(self.file_path, p=(p_s, p_e), ln=self.get_ln_number(), col=(col_s, col_e)))
    

    def consume_number(self):
        # 数字
        p_s = self.get_position()
        col_s = self.get_col_number()

        result = ''
        while self.is_eof() == False:
            c = self.get_char()
            if re.match(r'[0-9.]', c):
                result += self.consume_char()
            else:
                break
        p_e = self.get_position()
        col_e = self.get_col_number()

        return (result, POSITION_DATA(self.file_path, p=(p_s, p_e), ln=self.get_ln_number(), col=(col_s, col_e)))
    

    def consume_text(self):
        p_s = self.get_position()
        col_s = self.get_col_number()

        is_single_q = False
        text = ''
        assert (self.get_char() in ["'", '"'])
        quotation = self.consume_char()
        if quotation == "'":
            is_single_q = True

        while self.is_eof() == False:
            c = self.consume_char()
            if c == "'":
                if is_single_q:
                    p_e = self.get_position()
                    col_e = self.get_col_number()

                    break# ' ' end
                else:
                    text += c# ' " ' continue
            elif c == '"':
                if is_single_q:
                    text += c# " ' " continue
                else:
                    p_e = self.get_position()
                    col_e = self.get_col_number()

                    break# "" end
            else:
                text += c
            
        # print(f'text: {text}')
        return (text, POSITION_DATA(self.file_path, p=(p_s, p_e), ln=self.get_ln_number(), col=(col_s, col_e)))
    

    def consume_comment(self):
        p_s = self.get_position()
        col_s = self.get_col_number()

        # 全部こんだけ綺麗にかけたらすごいシンプルになるのに。
        # 後で書き直そうかな。
        comment = ''
        assert (self.get_char() == '#')
        self.consume_char()

        # この場合、
        # TKN_COMMENT(data=' this is comment\n')
        # TKN_SPACE_NEWLINE()
        # こうなる
        # \nを別にした方がいいのか悪いのか。
        # while self.is_eof() == False:
        #     c_here = self.consume_char()
        #     comment += c_here
        #     if c_here == '\n':
        #         return comment

        # 一方こっちは
        # TKN_COMMENT(data=' this is comment')
        # TKN_SPACE_NEWLINE()
        # TKN_SPACE_NEWLINE()
        # こっちにする。
        while self.is_eof() == False:
            if self.get_char() == '\n':
                p_e = self.get_position()
                col_e = self.get_col_number()

                return (comment, POSITION_DATA(self.file_path, p=(p_s, p_e), ln=self.get_ln_number(), col=(col_s, col_e)))
            else:
                comment += self.consume_char()
        
    def is_here_and_next_and_next_quotation(self):
        # for """ str """
        return (self.input[self.pos] == self.input[self.pos+1] == self.input[self.pos+2])
    

    def consume_triple_quotation_text(self):
        p_s = self.get_position()
        col_s = self.get_col_number()

        is_single_q = False
        text = ''
        assert (self.input[self.pos] == self.input[self.pos+1] == self.input[self.pos+2])
        if self.input[self.pos] == "'":
            is_single_q = True

        # triple_q
        self.consume_char()
        self.consume_char()
        self.consume_char()# triple_q

        while self.is_eof() == False:
            c = self.consume_char()
            if c == "'":
                if is_single_q:
                    self.consume_char()
                    self.consume_char()
                    p_e = self.get_position()
                    col_e = self.get_col_number()

                    break# ' ' end
                else:
                    text += c# ' " ' continue
            elif c == '"':
                if is_single_q:
                    text += c# " ' " continue
                else:
                    self.consume_char()
                    self.consume_char()
                    p_e = self.get_position()
                    col_e = self.get_col_number()

                    break# "" end
            else:
                text += c
        return (text, POSITION_DATA(self.file_path, p=(p_s, p_e), ln=self.get_ln_number(), col=(col_s, col_e)))
        


    def add_ln_number(self):
        self.ln += 1
    
    def get_ln_number(self):
        return self.ln
    
    def add_col_number(self):
        self.col += 1
    
    def reset_col_number(self):
        self.col = 1
    
    def get_col_number(self):
        return self.col


    def lex(self):
        tokens = []

        while self.is_eof() == False:
            c_here = self.get_char()
            _pos = self.get_position()
            col_s = self.get_col_number()
            _pos = POSITION_DATA(file_name=self.file_path, p=(_pos, _pos), ln=self.get_ln_number(), col=(col_s, col_s))
            # print(c_here)
            
            if re.match(r'[a-zA-Z_]', c_here):
                block, p = self.consume_while_variable_func_name()
                if block == "False":
                    tokens.append(PYK_FALSE(position=p))
                elif block == "None":
                    tokens.append(PYK_NONE(position=p))
                elif block == "True":
                    tokens.append(PYK_TRUE(position=p))
                elif block == "and":
                    tokens.append(PYK_AND(position=p))
                elif block == "as":
                    tokens.append(PYK_AS(position=p))
                elif block == "assert":
                    tokens.append(PYK_ASSERT(position=p))
                elif block == "async":
                    tokens.append(PYK_ASYNC(position=p))
                elif block == "await":
                    tokens.append(PYK_AWAIT(position=p))
                elif block == "break":
                    tokens.append(PYK_BREAK(position=p))
                elif block == "class":
                    tokens.append(PYK_CLASS(position=p))
                elif block == "continue":
                    tokens.append(PYK_CONTINUE(position=p))
                elif block == "def":
                    tokens.append(PYK_DEF(position=p))
                elif block == "del":
                    tokens.append(PYK_DEL(position=p))
                elif block == "elif":
                    tokens.append(PYK_ELIF(position=p))
                elif block == "else":
                    tokens.append(PYK_ELSE(position=p))
                elif block == "except":
                    tokens.append(PYK_EXCEPT(position=p))
                elif block == "finally":
                    tokens.append(PYK_FINALLY(position=p))
                elif block == "for":
                    tokens.append(PYK_FOR(position=p))
                elif block == "from":
                    tokens.append(PYK_FROM(position=p))
                elif block == "global":
                    tokens.append(PYK_GLOBAL(position=p))
                elif block == "if":
                    tokens.append(PYK_IF(position=p))
                elif block == "import":
                    tokens.append(PYK_IMPORT(position=p))
                elif block == "in":
                    tokens.append(PYK_IN(position=p))
                elif block == "is":
                    tokens.append(PYK_IS(position=p))
                elif block == "lambda":
                    tokens.append(PYK_LAMBDA(position=p))
                elif block == "nonlocal":
                    tokens.append(PYK_NONLOCAL(position=p))
                elif block == "not":
                    tokens.append(PYK_NOT(position=p))
                elif block == "or":
                    tokens.append(PYK_OR(position=p))
                elif block == "pass":
                    tokens.append(PYK_PASS(position=p))
                elif block == "raise":
                    tokens.append(PYK_RAISE(position=p))
                elif block == "return":
                    tokens.append(PYK_RETURN(position=p))
                elif block == "try":
                    tokens.append(PYK_TRY(position=p))
                elif block == "while":
                    tokens.append(PYK_WHILE(position=p))
                elif block == "with":
                    tokens.append(PYK_WITH(position=p))
                elif block == "yield":
                    tokens.append(PYK_YIELD(position=p))
                else:
                    tokens.append(TKN_IDENTIFIER(data=block, position=p))# token
            
            elif re.match(r'[0-9]', c_here):
                block, p = self.consume_number()
                # print(self.get_ln_number())
                data, is_float = StringConverter(block).convert()
                # print( (f'{in_func_param_tag}number', n) )
                if is_float:
                    tokens.append(TKN_FLOAT(data=data, position=p))
                else:
                    tokens.append(TKN_INT(data=data, position=p))

            # quotation
            elif c_here in ['"', "'"]:
                # get text
                if self.is_here_and_next_and_next_quotation():
                    # print('[ !! found triple quotation !! ]')# コメントなのかテキストなのかの判断をどうするか。まぁパーサーに任せよう。
                    text, p = self.consume_triple_quotation_text()
                    tokens.append(TKN_TRIPLE_QUOTATION_TEXT(data=text, position=p))
                else:
                    text, p = self.consume_text()
                    tokens.append(TKN_STRING(data=text, position=p))

            # op
            elif c_here in '+-=%/*&$!?@><()[]{}:;,.':
                if c_here == '+':
                    tokens.append(TKN_PLUS(position=_pos,))
                elif c_here == '-':
                    tokens.append(TKN_MINUS(position=_pos))
                elif c_here == '%':
                    tokens.append(TKN_PERCENT(position=_pos))
                elif c_here == '/':
                    tokens.append(TKN_SLASH(position=_pos))
                elif c_here == '*':
                    tokens.append(TKN_ASTERISK(position=_pos))
                elif c_here == '$':
                    tokens.append(TKN_DOLLAR_MARK(position=_pos))
                elif c_here == '!':
                    tokens.append(TKN_EXCLAMATION_MARK(position=_pos))
                elif c_here == '?':
                    tokens.append(TKN_QUESTION_MARK(position=_pos))
                elif c_here == '@':
                    tokens.append(TKN_AT_MARK(position=_pos))
                elif c_here == '=':
                    tokens.append(TKN_EQUAL(position=_pos))
                elif c_here == '>':
                    tokens.append(TKN_GREATER(position=_pos))
                elif c_here == '<':
                    tokens.append(TKN_LESSER(position=_pos))
                elif c_here == '(':
                    tokens.append(TKN_PARENTHESES_OPEN(position=_pos))
                elif c_here == ')':
                    tokens.append(TKN_PARENTHESES_CLOSE(position=_pos))
                elif c_here == '[':
                    tokens.append(TKN_SQUARE_BRACKET_OPEN(position=_pos))
                elif c_here == ']':
                    tokens.append(TKN_SQUARE_BRACKET_CLOSE(position=_pos))
                elif c_here == '{':
                    tokens.append(TKN_CURLY_BRACKET_OPEN(position=_pos))
                elif c_here == '}':
                    tokens.append(TKN_CURLY_BRACKET_CLOSE(position=_pos))
                elif c_here == ':':
                    tokens.append(TKN_COLON(position=_pos))
                elif c_here == ';':
                    tokens.append(TKN_SEMICOLON(position=_pos))
                elif c_here == ',':
                    tokens.append(TKN_COMMA(position=_pos))
                elif c_here == '.':
                    tokens.append(TKN_DOT(position=_pos))
                elif c_here == '&':
                    tokens.append(TKN_AND_MARK(position=_pos))
                
                else:
                    tokens.append(TKN_UNKNOWN(data=c_here, position=_pos))
            
                self.consume_char()

            # space
            elif re.match(r'\s', c_here):
                if c_here == '\n':
                    # print( ('new_line', '\n') )
                    self.add_ln_number()
                    self.reset_col_number()
                    # _pos = POSITION_DATA(file_name=self.file_path, s=_pos, e=_pos, ln=self.get_ln_number(), col=(col_s, col_e))
                    tokens.append(TKN_NEWLINE(position=_pos))
                elif c_here == ' ':
                    # print( ('white_space', ' ') )
                    tokens.append(TKN_WHITE_SPACE(position=_pos))
                elif c_here == '\t':
                    tokens.append(TKN_TAB(position=_pos))

                else:
                    print( ('[space]', c_here) )
                
                self.consume_char()
            
            elif c_here == '#':
                comment, p = self.consume_comment()
                tokens.append(TKN_COMMENT(data=comment, position=p))

            else:
                # print( ('[unknown]', c_here) )
                tokens.append(TKN_UNKNOWN(data=c_here))
                if self.can_move_next():
                    self.consume_char()
        

        eof_p = POSITION_DATA(file_name=self.file_path, p=(self.get_position(), self.get_position()), ln=self.get_ln_number(), col=(self.get_col_number(), self.get_col_number()))
        tokens.append(TKN_EOF(position=eof_p))
        return tokens