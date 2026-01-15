"""
CPU Bound Benchmark: Fibonacci Series Computation
Tests raw CPU performance between Python versions
"""

import time
import sys

# Allow conversion of very large integers to strings
sys.set_int_max_str_digits(0)


def fibonacci_recursive(n: int) -> int:
    """Classic recursive Fibonacci - O(2^n) - very CPU intensive."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Iterative Fibonacci for very large numbers."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_matrix(n: int) -> int:
    """Matrix exponentiation method - O(log n) but with big integer math."""
    if n <= 1:
        return n

    def matrix_mult(a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]

    def matrix_pow(m, p):
        if p == 1:
            return m
        if p % 2 == 0:
            half = matrix_pow(m, p // 2)
            return matrix_mult(half, half)
        else:
            return matrix_mult(m, matrix_pow(m, p - 1))

    base = [[1, 1], [1, 0]]
    result = matrix_pow(base, n)
    return result[0][1]


def benchmark_recursive(n: int = 35) -> float:
    """Benchmark recursive Fibonacci (CPU intensive due to call overhead)."""
    print(f"  Computing fib({n}) recursively...")
    start = time.perf_counter()
    result = fibonacci_recursive(n)
    elapsed = time.perf_counter() - start
    print(f"  Result: {result}, Time: {elapsed:.3f}s")
    return elapsed


def benchmark_iterative_large(n: int = 100000) -> float:
    """Benchmark iterative Fibonacci for large n (big integer arithmetic)."""
    print(f"  Computing fib({n}) iteratively (big integers)...")
    start = time.perf_counter()
    result = fibonacci_iterative(n)
    elapsed = time.perf_counter() - start
    digits = len(str(result))
    print(f"  Result has {digits} digits, Time: {elapsed:.3f}s")
    return elapsed


def benchmark_matrix_large(n: int = 500000) -> float:
    """Benchmark matrix method for very large n."""
    print(f"  Computing fib({n}) using matrix exponentiation...")
    start = time.perf_counter()
    result = fibonacci_matrix(n)
    elapsed = time.perf_counter() - start
    digits = len(str(result))
    print(f"  Result has {digits} digits, Time: {elapsed:.3f}s")
    return elapsed


def run_benchmark(iterations: int = 3) -> None:
    """Run all CPU benchmarks."""
    print("=" * 60)
    print("CPU BOUND BENCHMARK: Fibonacci Computation")
    print("=" * 60)
    print(f"Python version: {sys.version}")
    print("-" * 60)

    results = {
        "recursive": [],
        "iterative_large": [],
        "matrix_large": [],
    }

    for i in range(iterations):
        print(f"\n--- Iteration {i + 1}/{iterations} ---")

        print("\n[1] Recursive Fibonacci (tests function call overhead):")
        results["recursive"].append(benchmark_recursive(35))

        print("\n[2] Iterative Large Fibonacci (tests big integer performance):")
        results["iterative_large"].append(benchmark_iterative_large(100000))

        print("\n[3] Matrix Large Fibonacci (tests big integer multiplication):")
        results["matrix_large"].append(benchmark_matrix_large(500000))

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Python version: {sys.version.split()[0]}")
    print()

    for name, times in results.items():
        avg = sum(times) / len(times)
        print(f"{name}:")
        print(f"  Average: {avg:.3f}s")
        print(f"  Min: {min(times):.3f}s, Max: {max(times):.3f}s")


if __name__ == "__main__":
    run_benchmark(iterations=3)
