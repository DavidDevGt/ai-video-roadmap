# Project 0.2 — Gradient Playground

> Autograd, backprop from scratch

**Phase:** 0 — Foundations

**Runs on:** Victus (CPU)

**Estimated effort:** ~5 days at 4h/day

## Goal

Implement automatic differentiation (autograd) engine from scratch, including backpropagation through neural networks, chain rule, and gradient computation for arbitrary computation graphs.

## Why this matters

Autograd is the heart of every deep learning framework (PyTorch, JAX). Building it from scratch reveals how `loss.backward()` actually works and prepares you for understanding and modifying framework internals.

## Deliverables

- [ ] Autograd engine with forward and backward passes
- [ ] Support for common operations (matmul, relu, sigmoid, softmax)
- [ ] Neural network training loop from scratch
- [ ] Visualization of gradients and training dynamics
- [ ] Blog post: `docs/blog-posts/02-gradient-playground.md`

## DONE criterion

Implement complete autograd system capable of training a 2-layer MLP on a toy dataset.

## Setup

```bash
cd phase-0-foundations/02-gradient-playground

python -m venv .venv
.\.venv\Scripts\Activate.psdl  # PowerShell

pip install -r requirements.txt
```

## Key papers / resources

- "Automatic Differentiation in Machine Learning: A Survey" (Baydin et al.)
- CS231n assignments on backpropagation

## Status

- [ ] Started
- [ ] Derivations in notes.md
- [ ] Implementation done
- [ ] Visualizations done
- [ ] Blog post drafted
- [ ] Published
- [ ] **DONE**