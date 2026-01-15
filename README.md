# Python 3.12 vs 3.10 Benchmark

Comparing Python 3.12.8 with 3.10 for CPU-bound tasks using Fibonacci computation.

## Requirements

- [uv](https://docs.astral.sh/uv/) - Python package manager

## How to Run

```bash
./run_benchmarks.sh
```

Or run individual benchmarks:

```bash
# Python 3.12
uv run --python 3.12 benchmark_cpu.py

# Python 3.10
uv run --python 3.10 benchmark_cpu.py
```

## Benchmark Results

### CPU Bound Benchmark (Fibonacci Computation)

| Test | Python 3.10 | Python 3.12 | Improvement |
|------|-------------|-------------|-------------|
| **Recursive fib(35)** | 1.560s | 0.927s | **40.6% faster** |
| Iterative fib(100,000) | 0.122s | 0.121s | ~same |
| Matrix fib(500,000) | 0.066s | 0.068s | ~same |

### Key Findings

1. **Recursive function calls are ~40% faster in Python 3.12** - This is due to Python 3.11/3.12's "Faster CPython" project which introduced:
   - Specializing adaptive interpreter
   - Inline function calls
   - Reduced frame object overhead

2. **Big integer arithmetic is nearly identical** - The iterative and matrix methods show no significant difference, as they're dominated by big integer multiplication.

## Test Details

- **Recursive Fibonacci**: Tests function call overhead with O(2^n) complexity
- **Iterative Large Fibonacci**: Tests big integer performance computing fib(100,000) - result has 20,899 digits
- **Matrix Fibonacci**: Tests big integer multiplication computing fib(500,000) - result has 104,494 digits

Each benchmark runs 3 iterations and reports average, min, and max times.
