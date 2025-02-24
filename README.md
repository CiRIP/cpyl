# CPyL

A Python implementation of a Paret-like interpreter (from Programming Languages: Application and Interpretation), using Python 3.10+ `match` pattern matching syntax.

Implements functions/closures and function application. Mutable state and mutable boxes are not yet implemented.

## Architecture

* **Lexer** - transforms a string into S-Expressions (e.g. `"(+ 3 x)"` -> `SList([SSym("+"), SNum(3), SSym("x")])`).
* **Parser** - transforms an S-Expression into an extended-language expression.
* **Desugarer** - transforms extended-language sugar (such as `let` clauses) into concrete expressions (such as function definitions and applications).
* **Interpreter** - evaluates a concrete expression to a value type.
