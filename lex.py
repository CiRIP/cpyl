import re

from sexpr import *


def is_int(s: str) -> bool:
    try: int(s); return True
    except ValueError: return False


def is_float(s: str) -> bool:
    try: float(s); return True
    except ValueError: return False


def lex(s: str) -> SExpr:
    tokens = re.findall(r'\(|\)|[+-]?\d+|[a-zA-Z_][a-zA-Z0-9_]*|\S+', s)

    def _lex(tokens: list[str]) -> SExpr:
        if not tokens:
            raise SyntaxError("Unexpected end of input")

        match tokens.pop(0):
            case "(":
                l = []
                while tokens[0] != ")":
                    l.append(_lex(tokens))
                    if not tokens:
                        raise SyntaxError("Expected )")
                tokens.pop(0)
                return SList(l)

            case ")":
                raise SyntaxError("Unexpected )")

            case n if is_int(n):   return SNum(int(n))
            case x if is_float(x): return SNum(float(x))

            case s: return SSym(s)

    return _lex(tokens)
