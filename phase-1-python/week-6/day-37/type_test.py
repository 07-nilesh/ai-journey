def greet(name: str) -> None:
    print(f"Hello, {name}")

greet(42)  # Passing an int instead of a str

"""
Python doesn't have a built-in strict compiler to do this at runtime.
That is exactly what mypy is: it is an external Static Type Checker for Python.
It acts as a compile-time pass that reads your type hints and catches bugs before your code ever runs

Why mypy is Essential for AI & Data Pipelines?
Complex Data Structuring:
Defensive Documentation:
CI/CD Gatekeeper:
"""