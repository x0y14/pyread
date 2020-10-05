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
        if q:
            # print(f'= End Of File =')
            pass

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
    

    def consume_while_number(self):
        # 数字
        result = ''
        while self.is_eof() == False:
            c = self.get_char()
            if re.match(r'[0-9.]', c):
                result += self.consume_char()
            else:
                return result
        return result
    

    def consume_while_text(self):
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

    
    def lex(self):
        in_text = False
        # in_func_param = False
        # in_func_param_tag = ''
        tokens = []

        # variable_func_identfy = True

        while self.is_eof() == False:
            c_here = self.get_char()
            # print(c_here)

            if re.match(r'[a-zA-Z_]', c_here):
                if not in_text:
                    block = self.consume_while_variable_func_name()
                    # print( (f'{in_func_param_tag}symble', block) )
                    tokens.append(TKN_IDENTIFIER(data=block))# token
                    # if self.can_move_next():
                        # self.consume_char()

                else:
                    raise SyntaxError('?')
                    # print('= TEXT =')# ?
                    # if self.can_move_next():
                    #     self.consume_char()
            
            elif re.match(r'[0-9.]', c_here):
                block = self.consume_while_number()
                data, is_float = StringConverter(block).convert()
                # print( (f'{in_func_param_tag}number', n) )
                if is_float:
                    tokens.append(TKN_FLOAT(data=data))
                else:
                    tokens.append(TKN_INT(data=data))

                # if self.can_move_next():
                #     self.consume_char()

            elif c_here in ['"', "'"]:
                # get text
                text = self.consume_while_text()
                # print( ( 'data', text ) )
                tokens.append(TKN_STRING(data=text))

            elif c_here in '(){},:;+-=[]':
                # print( (f'operations', c_here) )
                if c_here == '(':
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
                    tokens.append(TKN_CURLY_BRACKET_OPEN())      

                elif c_here == '=':
                    tokens.append(TKN_EQUAL())
                
                elif c_here == ',':
                    tokens.append(TKN_COMMA())
                
                elif c_here == ':':
                    tokens.append(TKN_COLON())

                elif c_here == ';':
                    tokens.append(TKN_SEMICOLON())
                
                else:
                    print( (f'[op]', c_here) )
            
                self.consume_char()

            elif re.match(r'\s', c_here):
                if c_here == '\n':
                    # print( ('new_line', '\n') )
                    tokens.append(TKN_SPACE_NEWLINE())
                elif c_here == ' ':
                    # print( ('white_space', ' ') )
                    tokens.append(TKN_SPACE_WHITE())
                elif c_here == '\t':
                    tokens.append(TKN_SPACE_TAB())

                else:
                    print( ('[space]', c_here) )
                
                self.consume_char()

            else:
                print( ('[unknown]', c_here) )
                if self.can_move_next():
                    self.consume_char()
        
        return tokens