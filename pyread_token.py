import dataclasses

# literal

@dataclasses.dataclass
class POSITION_DATA:
    s: int
    e: int

@dataclasses.dataclass
class TKN_STRING:
    data: str
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_INT:
    data: int
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_FLOAT:
    data: float
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_IDENTIFIER:
    data: str
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_COMMENT:
    data: str
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_UNKNOWN:
    data: str
    position: POSITION_DATA


# operation
@dataclasses.dataclass
class TKN_PLUS:
    data = '+'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_MINUS:
    data = '-'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_PERCENT:
    data = '%'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_SLASH:
    data = '/'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_ASTERISK:
    data = '*'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_AND_MARK:
    data = '&'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_DOLLAR_MARK:
    data = '$'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_EXCLAMATION_MARK:
    data = '!'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_QUESTION_MARK:
    data = '?'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_AT_MARK:
    data = '@'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_EQUAL:
    data = '='
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_GREATER:
    data = '>'
    position: POSITION_DATA

# @dataclasses.dataclass
# class TKN_EQUAL_TO_GREATER:
#     data = '>='

@dataclasses.dataclass
class TKN_LESSER:
    data = '<'
    position: POSITION_DATA

# @dataclasses.dataclass
# class TKN_EQUAL_TO_LESSER:
#     data = '<='

@dataclasses.dataclass
class TKN_PARENTHESES_OPEN:
    data = '('
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_PARENTHESES_CLOSE:
    data = ')'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_SQUARE_BRACKET_OPEN:
    data = '['
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_SQUARE_BRACKET_CLOSE:
    data = ']'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_CURLY_BRACKET_OPEN:
    data = '{'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_CURLY_BRACKET_CLOSE:
    data = '}'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_COLON:
    data = ':'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_SEMICOLON:
    data = ';'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_COMMA:
    data = ','
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_PERIOD:
    data = '.'
    position: POSITION_DATA

# space
@dataclasses.dataclass
class TKN_WHITE_SPACE:
    data = ' '
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_TAB:
    data = '\t'
    position: POSITION_DATA

@dataclasses.dataclass
class TKN_NEWLINE:
    data = '\n'
    position: POSITION_DATA


@dataclasses.dataclass
class TKN_TRIPLE_QUOTATION_TEXT:
    data: str
    position: POSITION_DATA

# quotation
# @dataclasses.dataclass
# class TKN_QUOTATION_SINGLE:
#     data = "'"

# @dataclasses.dataclass
# class TKN_QUOTATION_DOUBLE:
#     data = '"'

# python予約語
@dataclasses.dataclass
class PYK_FALSE:
    data = 'False'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_NONE:
    data = 'None'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_TRUE:
    data = 'True'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_AND:
    data = 'and'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_AS:
    data = 'as'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_ASSERT:
    data = 'assert'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_ASYNC:
    data = 'async'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_AWAIT:
    data = 'await'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_BREAK:
    data = 'break'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_CLASS:
    data = 'class'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_CONTINUE:
    data = 'continue'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_DEF:
    data = 'def'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_DEL:
    data = 'del'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_ELIF:
    data = 'elif'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_ELSE:
    data = 'else'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_EXCEPT:
    data = 'except'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_FINALLY:
    data = 'finally'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_FOR:
    data = 'for'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_FROM:
    data = 'from'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_GLOBAL:
    data = 'global'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_IF:
    data = 'if'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_IMPORT:
    data = 'import'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_IN:
    data = 'in'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_IS:
    data = 'is'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_LAMBDA:
    data = 'lambda'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_NONLOCAL:
    data = 'nonlocal'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_NOT:
    data = 'not'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_OR:
    data = 'or'
    position: POSITION_DATA
    
@dataclasses.dataclass
class PYK_PASS:
    data = 'pass'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_RAISE:
    data = 'raise'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_RETURN:
    data = 'return'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_TRY:
    data = 'try'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_WHILE:
    data = 'while'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_WITH:
    data = 'with'
    position: POSITION_DATA

@dataclasses.dataclass
class PYK_YIELD:
    data = 'yield'
    position: POSITION_DATA