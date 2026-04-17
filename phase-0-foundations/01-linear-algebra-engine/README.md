# Project 0.1 — Linear Algebra Engine

> Vector, Matrix, Tensor ops in pure NumPy

**Phase:** 0 — Foundations

**Runs on:** Victus (CPU)

**Estimated effort:** ~5 days at 4h/day

## Goal

Build a complete linear algebra engine using only NumPy, implementing vectors, matrices, and tensors with all core operations (dot, matmul, transpose, inverse, eigenvalues, SVD, etc.).

## Why this matters

Every ML model is fundamentally linear algebra. Understanding how to implement these operations from scratch gives deep intuition for what happens "under the hood" of PyTorch, TensorFlow, and JAX.

## Deliverables

- [ ] Core linear algebra operations (vectors, matrices, tensors)
- [ ] Matrix decompositions (LU, QR, SVD, eigendecomposition)
- [ ] Visualization of transformations
- [ ] Blog post: `docs/blog-posts/01-linear-algebra-engine.md`

## DONE criterion

All core operations tested and documented. Visualizations demonstrate transformations (rotation, scaling, projection).

## Setup

```bash
cd phase-0-foundations/01-linear-algebra-engine

python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell

pip install -r requirements.txt
```

## Key papers / resources

- Gilbert Strang's Linear Algebra lectures
- "Mathematics for Machine Learning" (Deisenroth et al.)

## Status

- [ ] Started
- [ ] Derivations in notes.md
- [ ] Implementation done
- [ ] Visualizations done
- [ ] Blog post drafted
- [ ] Published
- [ ] **DONE**