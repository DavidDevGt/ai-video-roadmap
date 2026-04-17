# Project 0.4 — Neural Net from Scratch

> MNIST from raw NumPy, no PyTorch

**Phase:** 0 — Foundations

**Runs on:** Victus (CPU)

**Estimated effort:** ~5 days at 4h/day

## Goal

Implement a complete multilayer perceptron (MLP) training pipeline from scratch using only NumPy, including data loading, forward pass, backpropagation, optimization, and evaluation. Train on MNIST dataset.

## Why this matters

This is the culmination of Phase 0 — bringing together linear algebra, calculus, and probability into a working neural network. You'll understand every line of code in the training loop and be prepared for Phase 1 where we switch to PyTorch.

## Deliverables

- [ ] MLP architecture (input → hidden layers → output)
- [ ] MNIST data loading and preprocessing
- [ ] Complete training loop from scratch
- [ ] Training visualization (loss curves, accuracy)
- [ ] Blog post: `docs/blog-posts/04-neural-net-from-scratch.md`

## DONE criterion

Train MLP on MNIST using only NumPy and achieve >90% test accuracy.

## Setup

```bash
cd phase-0-foundations/04-neural-net-from-scratch

python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell

pip install -r requirements.txt
```

## Key papers / resources

- "Neural Networks and Deep Learning" (Nielsen)
- Andrej Karpathy's "Building a Micrograd"

## Status

- [ ] Started
- [ ] Derivations in notes.md
- [ ] Implementation done
- [ ] Visualizations done
- [ ] Blog post drafted
- [ ] Published
- [ ] **DONE**