from sexpr import *
from exprext import *
from exprc import *
from lex import lex
from parse import parse
from desugar import desugar
from interp import interp


if __name__ == '__main__':
    # e = LetExt([("a", NumExt(10)), ("b", NumExt(20))], BinOpExt("+", IdExt("a"), IdExt("b")))
    # print(desugar(e))
    # print(interp(desugar(e)))

    s = lex("((lambda (x) (* x 2)) (8))")
    # s = lex("(+ 1 2)")
    print(s)
    print(parse(s))
    print(interp(desugar(parse(s))))