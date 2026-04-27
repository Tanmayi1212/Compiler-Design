# 🛠️ Mini Compiler in Python

A modular **mini-compiler pipeline** implemented in Python that simulates the core phases of a compiler:

- Lexical Analysis
- Syntax Analysis
- Semantic Analysis
- Intermediate Code Generation (ICG)
- Code Optimization
- Target Code Generation

---

## 🚀 Features

- 🔍 Tokenization of source code
- 🌳 Abstract Syntax Tree (AST) generation
- 📘 Symbol Table construction
- ⚙️ Three Address Code (TAC) generation
- 🚀 Code optimization techniques:
  - Constant Folding
  - Constant Propagation
  - Common Subexpression Elimination
  - Dead Code Elimination
- 🧠 Target code generation (assembly-like output)
- ❌ Strong error handling at every phase
- 📂 Command-line execution support

---

## 📁 Project Structure

- `main.py` - Orchestrates the full compilation pipeline and writes to `output.txt`.
- `lexical.py` - Tokenizer for the mini language.
- `syntax.py` - Parser that builds a small AST.
- `semantic.py` - Symbol table checks (e.g., use before definition).
- `icg.py` - Intermediate code (three-address style) generation.
- `code_optimisation.py` - Simple optimization pass (constant folding).
- `target_code_generation.py` - Assembly-like target code emission.
- `input.txt` - Sample program input for manual testing/reference.
- `output.txt` - Sample compilation output produced by `main.py`.

---

## 🧩 Mini Language Overview

This compiler understands a tiny expression language with two statement forms:

- **Assignment:** `let <identifier> -> <expression>`
- **Print:** `show <identifier>`

Expressions support binary operators with standard precedence:

- `multiply` / `*` and `divide` / `/` have higher precedence than
  `plus` / `+` and `minus` / `-`.
- Operators associate left-to-right.

Supported tokens:

- Keywords: `let`, `show`, `plus`, `minus`, `multiply`, `divide`
- Symbols: `->`, `+`, `-`, `*`, `/`
- Literals: integers like `0`, `12`, `345`
- Identifiers: `x`, `total`, `value_1`

### Example Program

```text
let a -> 2 minus 5 plus 4 divide 8 multiply 6
let b -> a plus 4
let c -> 6 plus 7
let d -> b plus c
show d
```

---

## 🔬 Compilation Pipeline (Detailed)

### 1) Lexical Analysis

Implemented in `lexical.py`. The lexer scans the source text and emits tokens with
their type, value, and line number. Unexpected characters raise a syntax error.

**Output:** a flat list of tokens like `LET`, `IDENTIFIER`, `ARROW`, `NUMBER`,
`PLUS`, `MINUS`, `TIMES`, and `DIVIDE`.

### 2) Syntax Analysis

Implemented in `syntax.py`. The parser consumes tokens and builds a small AST with
these node types:

- `Assign(var = expr)`
- `Print(var)`
- `BinOp(left op right)` where `op` is `+`, `-`, `*`, or `/`

**Output:** an ordered list of AST nodes that represent the program structure.

### 3) Semantic Analysis

Implemented in `semantic.py`. The semantic pass builds a symbol table and validates
that variables used in `show` are defined earlier in the program.

**Output:** a `{name: type}` symbol table (currently all variables are `int`).

### 4) Intermediate Code Generation (ICG)

Implemented in `icg.py`. The AST is lowered into three-address code using
temporaries for nested expressions:

```
t1 = 2 - 5
t2 = 4 / 8
t3 = t2 * 6
t4 = t1 + t3
a = t4
PRINT a
```

### 5) Code Optimization

Implemented in `code_optimisation.py`. A small constant-folding pass combines
pure numeric operations for `+`, `-`, `*`, and `/` (integer division), e.g.
`a = 2 + 3` becomes `a = 5`.

### 6) Target Code Generation

Implemented in `target_code_generation.py`. The optimized ICG is translated into
an assembly-like sequence with basic arithmetic instructions:

```
SET a 5
LOAD a
MUL 2
SAVE b
OUT b
```

---

## ▶️ Running the Compiler

Run the pipeline with the built-in example program:

```bash
python main.py
```

The compiler writes the full, step-by-step output to `output.txt`.

---

## ✅ Notes

- This project is intentionally small to illustrate the classic compiler phases.
- You can replace the example program in `main.py` with the contents of `input.txt`
  to test different inputs.
