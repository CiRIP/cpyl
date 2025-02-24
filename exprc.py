from dataclasses import dataclass
from abc import ABC


@dataclass(frozen=True)
class ExprC(ABC): pass


@dataclass(frozen=True)
class NumC(ExprC): n: int | float


@dataclass(frozen=True)
class TrueC(ExprC): pass


@dataclass(frozen=True)
class FalseC(ExprC): pass


@dataclass(frozen=True)
class NilC(ExprC): pass


@dataclass(frozen=True)
class UninitializedC(ExprC): pass


@dataclass(frozen=True)
class PlusC(ExprC): l: ExprC; r: ExprC


@dataclass(frozen=True)
class MultC(ExprC): l: ExprC; r: ExprC


@dataclass(frozen=True)
class EqNumC(ExprC): l: ExprC; r: ExprC


@dataclass(frozen=True)
class LtC(ExprC): l: ExprC; r: ExprC


@dataclass(frozen=True)
class IfC(ExprC): c: ExprC; t: ExprC; e: ExprC


@dataclass(frozen=True)
class ConsC(ExprC): l: ExprC; r: ExprC


@dataclass(frozen=True)
class IsNilC(ExprC): e: ExprC


@dataclass(frozen=True)
class IsListC(ExprC): e: ExprC


@dataclass(frozen=True)
class HeadC(ExprC): e: ExprC


@dataclass(frozen=True)
class TailC(ExprC): e: ExprC


@dataclass(frozen=True)
class UndefinedC(ExprC): pass


@dataclass(frozen=True)
class IdC(ExprC): id: str


@dataclass(frozen=True)
class SetC(ExprC): id: str; e: ExprC


@dataclass(frozen=True)
class SeqC(ExprC): e1: ExprC; e2: ExprC


@dataclass(frozen=True)
class FdC(ExprC): params: list[str]; body: ExprC


@dataclass(frozen=True)
class AppC(ExprC): f: ExprC; args: list[ExprC]
