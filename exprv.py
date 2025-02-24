from dataclasses import dataclass
from abc import ABC

from exprc import FdC


@dataclass(frozen=True)
class ExprV(ABC): pass


@dataclass(frozen=True)
class NumV(ExprV): n: int | float


@dataclass(frozen=True)
class BoolV(ExprV): b: bool


@dataclass(frozen=True)
class NilV(ExprV): pass


@dataclass(frozen=True)
class UninitializedV(ExprV): pass


@dataclass(frozen=True)
class ConsV(ExprV): l: ExprV; r: ExprV


@dataclass(frozen=True)
class PointerClosV(ExprV): f: FdC; nv: dict[str, ExprV]
