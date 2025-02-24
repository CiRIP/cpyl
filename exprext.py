from dataclasses import dataclass
from abc import ABC


@dataclass(frozen=True)
class ExprExt(ABC): pass


@dataclass(frozen=True)
class NumExt(ExprExt): n: int


@dataclass(frozen=True)
class TrueExt(ExprExt): pass


@dataclass(frozen=True)
class FalseExt(ExprExt): pass


@dataclass(frozen=True)
class NilExt(ExprExt): pass


@dataclass(frozen=True)
class IdExt(ExprExt): id: str


@dataclass(frozen=True)
class UnOpExt(ExprExt): op: str; e: ExprExt


@dataclass(frozen=True)
class BinOpExt(ExprExt): op: str; l: ExprExt; r: ExprExt


@dataclass(frozen=True)
class IfExt(ExprExt): c: ExprExt; t: ExprExt; e: ExprExt


@dataclass(frozen=True)
class CondExt(ExprExt): cs: list[ExprExt]


@dataclass(frozen=True)
class CondEExt(ExprExt): cs: list[ExprExt]; e: ExprExt


@dataclass(frozen=True)
class ListExt(ExprExt): l: list[ExprExt]


@dataclass(frozen=True)
class FdExt(ExprExt): params: list[str]; body: ExprExt


@dataclass(frozen=True)
class AppExt(ExprExt): f: ExprExt; args: list[ExprExt]


@dataclass(frozen=True)
class LetExt(ExprExt): binds: list[(str, ExprExt)]; body: ExprExt


@dataclass(frozen=True)
class SetExt(ExprExt): id: str; e: ExprExt
