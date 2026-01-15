#!/bin/bash

echo "============================================================"
echo "Python 3.12 vs 3.10 Benchmark Suite"
echo "============================================================"
echo ""

# Run with Python 3.12
echo ">>> Running benchmarks with Python 3.12..."
echo ""
echo "--- CPU Bound Benchmark (Python 3.12) ---"
uv run --python 3.12 benchmark_cpu.py

echo ""
echo "============================================================"
echo ""

# Run with Python 3.10
echo ">>> Running benchmarks with Python 3.10..."
echo ""
echo "--- CPU Bound Benchmark (Python 3.10) ---"
uv run --python 3.10 benchmark_cpu.py



echo ""
echo "============================================================"
echo "Benchmark Complete!"
echo "============================================================"
