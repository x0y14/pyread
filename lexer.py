from modules.string_converter import StringConverter
import re
from pyread_token import *

class Lexer:
    def __init__(self, inp):
        self.input = inp
        self.pos = 0
        self.in_string = False
        self.first_char_of_line = True
        super().__init__()
    

    def is_eof(self) -> bool:
        # ぴったりですか?
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
        return c
    

    def consume_while(self, target='') -> str:
        # 次の文字が与えられたものと一致している間、consume_char()をし続けます。
        result = ''
        if target == '':
            return ''
        while self.is_eof() is False:
            if self.get_char() == target:
                result += self.consume_char()
                if self.is_next_char(target) == False:
                    return result
    

    def consume_while_variable_func_name(self):
        # 関数名や変数などに。
        result = ''
        while self.is_eof() == False:
            c = self.get_char()
            if re.match(r'[a-zA-Z0-9_]', c):
                result += self.consume_char()
            else:
                return result
        return result
    

    def consume_number(self):
        # 数字
        result = ''
        while self.is_eof() == False:
            c = self.get_char()
            if re.match(r'[0-9.]', c):
                result += self.consume_char()
            else:
                return result
        return result
    

    def consume_text(self):
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
                    break# ' ' end
                else:
                    text += c# ' " ' continue
            elif c == '"':
                if is_single_q:
                    text += c# " ' " continue
                else:
                    break# "" end
            else:
                text += c
            
        # print(f'text: {text}')
        return text
    

    def consume_comment(self):
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
                return comment
            else:
                comment += self.consume_char()



    def lex(self):
        tokens = []

        while self.is_eof() == False:
            c_here = self.get_char()
            # print(c_here)
            
            if re.match(r'[a-zA-Z_]', c_here):
                block = self.consume_while_variable_func_name()
                if block == "False":
                    tokens.append(PYK_FALSE())
                elif block == "None":
                    tokens.append(PYK_NONE())
                elif block == "True":
                    tokens.append(PYK_TRUE())
                elif block == "and":
                    tokens.append(PYK_AND())
                elif block == "as":
                    tokens.append(PYK_AS())
                elif block == "assert":
                    tokens.append(PYK_ASSERT())
                elif block == "async":
                    tokens.append(PYK_ASYNC())
                elif block == "await":
                    tokens.append(PYK_AWAIT())
                elif block == "break":
                    tokens.append(PYK_BREAK())
                elif block == "class":
                    tokens.append(PYK_CLASS())
                elif block == "continue":
                    tokens.append(PYK_CONTINUE())
                elif block == "def":
                    tokens.append(PYK_DEF())
                elif block == "del":
                    tokens.append(PYK_DEL())
                elif block == "elif":
                    tokens.append(PYK_ELIF())
                elif block == "else":
                    tokens.append(PYK_ELSE())
                elif block == "except":
                    tokens.append(PYK_EXCEPT())
                elif block == "finally":
                    tokens.append(PYK_FINALLY())
                elif block == "for":
                    tokens.append(PYK_FOR())
                elif block == "from":
                    tokens.append(PYK_FROM())
                elif block == "global":
                    tokens.append(PYK_GLOBAL())
                elif block == "if":
                    tokens.append(PYK_IF())
                elif block == "import":
                    tokens.append(PYK_IMPORT())
                elif block == "in":
                    tokens.append(PYK_IN())
                elif block == "is":
                    tokens.append(PYK_IS())
                elif block == "lambda":
                    tokens.append(PYK_LAMBDA())
                elif block == "nonlocal":
                    tokens.append(PYK_NONLOCAL())
                elif block == "not":
                    tokens.append(PYK_NOT())
                elif block == "or":
                    tokens.append(PYK_OR())
                elif block == "pass":
                    tokens.append(PYK_PASS())
                elif block == "raise":
                    tokens.append(PYK_RAISE())
                elif block == "return":
                    tokens.append(PYK_RETURN())
                elif block == "try":
                    tokens.append(PYK_TRY())
                elif block == "while":
                    tokens.append(PYK_WHILE())
                elif block == "with":
                    tokens.append(PYK_WITH())
                elif block == "yield":
                    tokens.append(PYK_YIELD())
                else:
                    tokens.append(TKN_IDENTIFIER(data=block))# token
            
            elif re.match(r'[0-9.]', c_here):
                block = self.consume_number()
                data, is_float = StringConverter(block).convert()
                # print( (f'{in_func_param_tag}number', n) )
                if is_float:
                    tokens.append(TKN_FLOAT(data=data))
                else:
                    tokens.append(TKN_INT(data=data))

            # quotation
            elif c_here in ['"', "'"]:
                # get text
                text = self.consume_text()
                tokens.append(TKN_STRING(data=text))

            # op
            elif c_here in '+-=%/*&$!?@><()[]{}:;,.':
                if c_here == '+':
                    tokens.append(TKN_PLUS())
                elif c_here == '-':
                    tokens.append(TKN_MINUS())
                elif c_here == '%':
                    tokens.append(TKN_PERCENT())
                elif c_here == '/':
                    tokens.append(TKN_SLASH())
                elif c_here == '*':
                    tokens.append(TKN_ASTERISK())
                elif c_here == '$':
                    tokens.append(TKN_DOLLAR_MARK())
                elif c_here == '!':
                    tokens.append(TKN_EXCLAMATION_MARK())
                elif c_here == '?':
                    tokens.append(TKN_QUESTION_MARK())
                elif c_here == '@':
                    tokens.append(TKN_AT_MARK())
                elif c_here == '=':
                    tokens.append(TKN_EQUAL())
                elif c_here == '>':
                    tokens.append(TKN_GREATER())
                elif c_here == '<':
                    tokens.append(TKN_LESSER())
                elif c_here == '(':
                    tokens.append(TKN_PARENTHESES_OPEN())
                elif c_here == ')':
                    tokens.append(TKN_PARENTHESES_CLOSE())
                elif c_here == '[':
                    tokens.append(TKN_SQUARE_BRACKET_OPEN())
                elif c_here == ']':
                    tokens.append(TKN_SQUARE_BRACKET_CLOSE())
                elif c_here == '{':
                    tokens.append(TKN_CURLY_BRACKET_OPEN())
                elif c_here == '}':
                    tokens.append(TKN_CURLY_BRACKET_CLOSE())
                elif c_here == ':':
                    tokens.append(TKN_COLON())
                elif c_here == ';':
                    tokens.append(TKN_SEMICOLON())
                elif c_here == ',':
                    tokens.append(TKN_COMMA())
                elif c_here == '.':
                    tokens.append(TKN_PERIOD())
                elif c_here == '&':
                    tokens.append(TKN_AND_MARK())
                
                else:
                    tokens.append(TKN_UNKNOWN(data=c_here))
            
                self.consume_char()

            # space
            elif re.match(r'\s', c_here):
                if c_here == '\n':
                    # print( ('new_line', '\n') )
                    tokens.append(TKN_NEWLINE())
                elif c_here == ' ':
                    # print( ('white_space', ' ') )
                    tokens.append(TKN_WHITE_SPACE())
                elif c_here == '\t':
                    tokens.append(TKN_TAB())

                else:
                    print( ('[space]', c_here) )
                
                self.consume_char()
            
            elif c_here == '#':
                comment = self.consume_comment()
                tokens.append(TKN_COMMENT(data=comment))

            else:
                # print( ('[unknown]', c_here) )
                tokens.append(TKN_UNKNOWN(data=c_here))
                if self.can_move_next():
                    self.consume_char()
        
        return tokens