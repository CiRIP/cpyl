from dataclasses import dataclass
from abc import ABC


@dataclass(frozen=True)
class SExpr(ABC): pass


@dataclass(frozen=True)
class SNum(SExpr): n: int | float


@dataclass(frozen=True)
class SSym(SExpr): s: str


@dataclass(frozen=True)
class SList(SExpr): l: list[SExpr]
