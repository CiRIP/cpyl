from typing import cast

from sexpr import *
from exprext import *


KEYWORDS = {"lambda", "nil", "cons", "head", "tail"}


def parse(s: SExpr) -> ExprExt:
    match s:
        case SNum(n): return NumExt(n)

        case SSym("true"):  return TrueExt()
        case SSym("false"): return FalseExt()
        case SSym("nil"):   return NilExt()

        case SSym(id) if id not in KEYWORDS: return IdExt(id)

        case SList([SSym("if"), c, t, e]): return IfExt(parse(c), parse(t), parse(e))
        case SList([SSym("cond"), *cs]):   return CondExt([parse(c) for c in cs])
        # case SList([SSym("cond-e")])
        case SList([SSym("list"), *es]):   return ListExt([parse(e) for e in es])

        case SList([SSym("lambda"), SList(ps), b]):
            ps = [parse(p) for p in ps]

            if not all(isinstance(p, IdExt) for p in ps):
                raise SyntaxError("Lambda does not have valid arguments")

            return FdExt([p.id for p in ps], parse(b))

        case SList([SSym(op), e]):    return UnOpExt(op, parse(e))
        case SList([SSym(op), l, r]): return BinOpExt(op, parse(l), parse(r))

        case SList([f, SList(args)]): return AppExt(parse(f), [parse(a) for a in args])

    raise SyntaxError(f"Unknown syntax {s}")
