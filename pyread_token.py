import dataclasses

# literal
@dataclasses.dataclass
class TKN_STRING:
    data: str

@dataclasses.dataclass
class TKN_INT:
    data: int

@dataclasses.dataclass
class TKN_FLOAT:
    data: float


@dataclasses.dataclass
class TKN_IDENTIFIER:
    data: str

@dataclasses.dataclass
class TKN_COMMENT:
    data: str

@dataclasses.dataclass
class TKN_UNKNOWN:
    data: str


# operation
@dataclasses.dataclass(frozen=True)
class TKN_PLUS:
    data = '+'

@dataclasses.dataclass(frozen=True)
class TKN_MINUS:
    data = '-'

@dataclasses.dataclass(frozen=True)
class TKN_PERCENT:
    data = '%'

@dataclasses.dataclass(frozen=True)
class TKN_SLASH:
    data = '/'

@dataclasses.dataclass(frozen=True)
class TKN_ASTERISK:
    data = '*'

@dataclasses.dataclass(frozen=True)
class TKN_AND_MARK:
    data = '&'

@dataclasses.dataclass(frozen=True)
class TKN_DOLLAR_MARK:
    data = '$'

@dataclasses.dataclass(frozen=True)
class TKN_EXCLAMATION_MARK:
	data = '!'

@dataclasses.dataclass(frozen=True)
class TKN_QUESTION_MARK:
	data = '?'

@dataclasses.dataclass(frozen=True)
class TKN_AT_MARK:
	data = '@'

@dataclasses.dataclass(frozen=True)
class TKN_EQUAL:
    data = '='

@dataclasses.dataclass(frozen=True)
class TKN_GREATER:
    data = '>'

@dataclasses.dataclass(frozen=True)
class TKN_EQUAL_TO_GREATER:
    data = '>='

@dataclasses.dataclass(frozen=True)
class TKN_LESSER:
    data = '<'

@dataclasses.dataclass(frozen=True)
class TKN_EQUAL_TO_LESSER:
    data = '<='

@dataclasses.dataclass(frozen=True)
class TKN_PARENTHESES_OPEN:
    data = '('

@dataclasses.dataclass(frozen=True)
class TKN_PARENTHESES_CLOSE:
    data = ')'

@dataclasses.dataclass(frozen=True)
class TKN_SQUARE_BRACKET_OPEN:
    data = '['

@dataclasses.dataclass(frozen=True)
class TKN_SQUARE_BRACKET_CLOSE:
    data = ']'

@dataclasses.dataclass(frozen=True)
class TKN_CURLY_BRACKET_OPEN:
    data = '{'

@dataclasses.dataclass(frozen=True)
class TKN_CURLY_BRACKET_CLOSE:
    data = '}'

@dataclasses.dataclass(frozen=True)
class TKN_COLON:
    data = ':'

@dataclasses.dataclass(frozen=True)
class TKN_SEMICOLON:
    data = ';'

@dataclasses.dataclass(frozen=True)
class TKN_COMMA:
    data = ','

@dataclasses.dataclass(frozen=True)
class TKN_PERIOD:
    data = '.'

# space
@dataclasses.dataclass(frozen=True)
class TKN_SPACE_WHITE:
    data = ' '

@dataclasses.dataclass(frozen=True)
class TKN_SPACE_TAB:
    data = '\t'

@dataclasses.dataclass(frozen=True)
class TKN_SPACE_NEWLINE:
    data = '\n'


# quotation
@dataclasses.dataclass(frozen=True)
class TKN_QUOTATION_SINGLE:
    data = "'"

@dataclasses.dataclass(frozen=True)
class TKN_QUOTATION_DOUBLE:
    data = '"'

# python予約語
@dataclasses.dataclass(frozen=True)
class PYK_FALSE:
	data = 'False'

@dataclasses.dataclass(frozen=True)
class PYK_NONE:
	data = 'None'

@dataclasses.dataclass(frozen=True)
class PYK_TRUE:
	data = 'True'

@dataclasses.dataclass(frozen=True)
class PYK_AND:
	data = 'and'

@dataclasses.dataclass(frozen=True)
class PYK_AS:
	data = 'as'

@dataclasses.dataclass(frozen=True)
class PYK_ASSERT:
	data = 'assert'

@dataclasses.dataclass(frozen=True)
class PYK_ASYNC:
	data = 'async'

@dataclasses.dataclass(frozen=True)
class PYK_AWAIT:
	data = 'await'

@dataclasses.dataclass(frozen=True)
class PYK_BREAK:
	data = 'break'

@dataclasses.dataclass(frozen=True)
class PYK_CLASS:
	data = 'class'

@dataclasses.dataclass(frozen=True)
class PYK_CONTINUE:
	data = 'continue'

@dataclasses.dataclass(frozen=True)
class PYK_DEF:
	data = 'def'

@dataclasses.dataclass(frozen=True)
class PYK_DEL:
	data = 'del'

@dataclasses.dataclass(frozen=True)
class PYK_ELIF:
	data = 'elif'

@dataclasses.dataclass(frozen=True)
class PYK_ELSE:
	data = 'else'

@dataclasses.dataclass(frozen=True)
class PYK_EXCEPT:
	data = 'except'

@dataclasses.dataclass(frozen=True)
class PYK_FINALLY:
	data = 'finally'

@dataclasses.dataclass(frozen=True)
class PYK_FOR:
	data = 'for'

@dataclasses.dataclass(frozen=True)
class PYK_FROM:
	data = 'from'

@dataclasses.dataclass(frozen=True)
class PYK_GLOBAL:
	data = 'global'

@dataclasses.dataclass(frozen=True)
class PYK_IF:
	data = 'if'

@dataclasses.dataclass(frozen=True)
class PYK_IMPORT:
	data = 'import'

@dataclasses.dataclass(frozen=True)
class PYK_IN:
	data = 'in'

@dataclasses.dataclass(frozen=True)
class PYK_IS:
	data = 'is'

@dataclasses.dataclass(frozen=True)
class PYK_LAMBDA:
	data = 'lambda'

@dataclasses.dataclass(frozen=True)
class PYK_NONLOCAL:
	data = 'nonlocal'

@dataclasses.dataclass(frozen=True)
class PYK_NOT:
	data = 'not'

@dataclasses.dataclass(frozen=True)
class PYK_OR:
	data = 'or'

@dataclasses.dataclass(frozen=True)
class PYK_PASS:
	data = 'pass'

@dataclasses.dataclass(frozen=True)
class PYK_RAISE:
	data = 'raise'

@dataclasses.dataclass(frozen=True)
class PYK_RETURN:
	data = 'return'

@dataclasses.dataclass(frozen=True)
class PYK_TRY:
	data = 'try'

@dataclasses.dataclass(frozen=True)
class PYK_WHILE:
	data = 'while'

@dataclasses.dataclass(frozen=True)
class PYK_WITH:
	data = 'with'

@dataclasses.dataclass(frozen=True)
class PYK_YIELD:
	data = 'yield'