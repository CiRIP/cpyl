from functools import reduce

from exprext import *
from exprc import *

def desugar(e: ExprExt) -> ExprC:
    match e:
        case TrueExt():  return TrueC()
        case FalseExt(): return FalseC()
        case NumExt(n):  return NumC(n)
        case NilExt():   return NilC()
        case IdExt(id):  return IdC(id)

        case UnOpExt("-", e):        return MultC(NumC(-1), desugar(e))
        case BinOpExt("+", l, r):    return PlusC(desugar(l), desugar(r))
        case BinOpExt("*", l, r):    return MultC(desugar(l), desugar(r))
        case BinOpExt("-", l, r):    return PlusC(desugar(l), MultC(NumC(-1), desugar(r)))
        case BinOpExt("num<", l, r): return LtC(desugar(l), desugar(r))
        case BinOpExt("num>", l, r): return LtC(MultC(NumC(-1), desugar(l)), MultC(NumC(-1), desugar(r)))
        case BinOpExt("num=", l, r): return EqNumC(desugar(l), desugar(r))

        case IfExt(c, t, e): return IfC(desugar(c), desugar(t), desugar(e))

        case UnOpExt("not", e):     return IfC(desugar(e), FalseC(), TrueC())
        case BinOpExt("and", l, r): return IfC(desugar(l), desugar(r), FalseC())
        case BinOpExt("or", l, r):  return IfC(desugar(l), TrueC(), desugar(r))

        case UnOpExt("head", e):     return HeadC(desugar(e))
        case UnOpExt("tail", e):     return TailC(desugar(e))
        case UnOpExt("is-nil", e):   return IsNilC(desugar(e))
        case UnOpExt("is-list", e):  return IsListC(desugar(e))
        case BinOpExt("cons", l, r): return ConsC(desugar(l), desugar(r))

        # case CondExt
        # case CondEExt

        case ListExt(l): acc = NilC(); [acc := ConsC(desugar(e), acc) for e in l]; return acc

        case FdExt(params, body): return FdC(params, desugar(body))
        case AppExt(f, args):     return AppC(desugar(f), [desugar(a) for a in args])
        case LetExt(binds, body): return AppC(FdC([n for n, v in binds], desugar(body)), [desugar(v) for n, v in binds])

        case BinOpExt("seq", l, r): return SeqC(desugar(l), desugar(r))

        case SetExt(id, e): return SetC(id, desugar(e))
