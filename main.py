import argparse
import sys

# =========================
# IMPORT COMPILER PHASES
# =========================

# Adjust module names based on your file structure
from lexical import Lexer, LexerError
from syntax import Parser
from semantic import semantic_analysis
from icg import intermediate_code_generation
from code_optimisation import optimize_tac
from target_code_generation import TargetCodeGenerator


# =========================
# CORE PIPELINE FUNCTION
# =========================

def compile(source_code):
    try:
        print("\n===== COMPILATION STARTED =====\n")

        # 1. LEXER
        print("[1] Lexical Analysis...")
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()

        print("Tokens:")
        for t in tokens:
            print(t)

        # 2. PARSER
        print("\n[2] Syntax Analysis...")
        parser = Parser(tokens)
        ast = parser.parse()

        print("AST:")
        for stmt in ast:
            print(stmt)

        # 3. SEMANTIC
        print("\n[3] Semantic Analysis...")
        sem_out = semantic_analysis(ast)

        # 4. ICG
        print("\n[4] Intermediate Code Generation...")
        tac = intermediate_code_generation(sem_out)

        # 5. OPTIMIZATION
        print("\n[5] Optimization...")
        opt = optimize_tac(tac)

        # 6. CODE GEN
        print("\n[6] Code Generation...")
        tcg = TargetCodeGenerator()
        final = tcg.generate(opt)

        print("\n===== SUCCESS =====\n")
        return final

    except Exception as e:
        print("\n❌ COMPILATION FAILED")
        print(e)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    args = parser.parse_args()

    try:
        with open(args.source) as f:
            code = f.read()
    except:
        print("File not found")
        sys.exit(1)

    compile(code)


if __name__ == "__main__":
    main()