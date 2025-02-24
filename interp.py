from exprc import *
from exprv import *


def interp(e: ExprC, nv: dict[str, ExprV] = None) -> ExprV:
    if nv is None:
        nv = dict()

    match e:
        case NumC(n):  return NumV(n)
        case TrueC():  return BoolV(True)
        case FalseC(): return BoolV(False)
        case NilC():   return NilV()
        case UninitializedC(): return UninitializedV()

        case PlusC(l, r):
            match interp(l, nv), interp(r, nv):
                case NumV(l), NumV(r): return NumV(l + r)
                case l, r: raise TypeError(f"Invalid operands {l} and {r} for operator +")

        case MultC(l, r):
            match interp(l, nv), interp(r, nv):
                case NumV(l), NumV(r): return NumV(l * r)
                case _: raise TypeError(f"Invalid operands {l} and {r} for operator *")

        case EqNumC(l, r):
            match interp(l, nv), interp(r, nv):
                case NumV(l), NumV(r): return BoolV(l == r)
                case _: raise TypeError(f"Invalid operands {l} and {r} for operator num=")

        case LtC(l, r):
            match interp(l, nv), interp(r, nv):
                case NumV(l), NumV(r): return BoolV(l < r)
                case _: raise TypeError(f"Invalid operands {l} and {r} for operator num<")

        case IfC(c, t, e):
            match interp(c, nv):
                case BoolV(True):  return interp(t, nv)
                case BoolV(False): return interp(e, nv)
                case c:            raise TypeError(f"Invalid condition {c}")

        case ConsC(l, r): return ConsV(interp(l, nv), interp(r, nv))

        case IsNilC(e):
            match interp(e, nv):
                case NilV():      return BoolV(True)
                case ConsV(_, _): return BoolV(False)
                case e:           raise TypeError(f"{e} is not a list type")

        case IsListC(e):
            match interp(e, nv):
                case NilV():      return BoolV(True)
                case ConsV(_, _): return BoolV(True)
                case _:           return BoolV(False)

        case HeadC(e):
            match interp(e, nv):
                case ConsV(h, _): return h
                case e: raise TypeError(f"{e} is not a list type")

        case TailC(e):
            match interp(e, nv):
                case ConsV(_, t): return t
                case e: raise TypeError(f"{e} is not a list type")

        case UndefinedC(): raise ValueError("Multi-armed conditional did not match any conditions")

        case IdC(id): return nv[id]

        # case SeqC(e1, e2): return interp(e2)

        case FdC(_, _): return PointerClosV(e, nv)

        case AppC(f, args):
            match interp(f, nv):
                case PointerClosV(f, nv_) if len(f.params) == len(args):
                    return interp(f.body, {**nv_, **dict(zip(f.params, [interp(a, nv) for a in args]))})
                case PointerClosV(f, _): raise TypeError(f"Invalid arguments {args} for function {f}")
                case _: raise TypeError(f"{f} is not a closure")

    raise ValueError(f"Unable to interpret {e}")
