from lexical import Lexer
from syntax import Parser
from semantic import SemanticAnalyzer
from icg import ICG
from code_optimisation import Optimizer
from target_code_generation import CodeGenerator


def compile_code(code, output_path="output.txt"):
    output_lines = []

    def emit(text=""):
        print(text)
        output_lines.append(text)

    emit("\n===== COMPILATION STARTED =====")

    # Phase 1
    emit("\n[1] Lexical Analysis")
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    type_width = max((len(tok.type) for tok in tokens), default=4)
    value_width = max((len(str(tok.value)) for tok in tokens), default=5)
    for tok in tokens:
        emit(f"  {tok.type:<{type_width}} -> {tok.value:<{value_width}} (line {tok.line})")

    # Phase 2
    emit("\n[2] Syntax Analysis")
    parser = Parser(tokens)
    ast = parser.parse()
    for node in ast:
        emit(f"  {node}")

    # Phase 3
    emit("\n[3] Semantic Analysis")
    semantic = SemanticAnalyzer()
    symbols = semantic.analyze(ast)
    for name, dtype in symbols.items():
        emit(f"  {name} -> {dtype}")

    # Phase 4
    emit("\n[4] Intermediate Code")
    icg = ICG().generate(ast)
    for idx, line in enumerate(icg, start=1):
        emit(f"  {idx}. {line}")

    # Phase 5
    emit("\n[5] Optimized Code")
    opt = Optimizer().optimize(icg)
    for idx, line in enumerate(opt, start=1):
        emit(f"  {idx}. {line}")

    # Phase 6
    emit("\n[6] Target Code")
    target = CodeGenerator().generate(opt)
    for idx, line in enumerate(target, start=1):
        emit(f"  {idx}. {line}")

    emit("\n===== COMPILATION SUCCESSFUL =====")

    with open(output_path, "w") as f:
        f.write("\n".join(output_lines) + "\n")


if __name__ == "__main__":
    code = """
    let x -> 5
    let y -> x plus 3
    show y
    """
    compile_code(code)