# Project 0.3 — Probability Applied

> Distributions, sampling, MLE

**Phase:** 0 — Foundations

**Runs on:** Victus (CPU)

**Estimated effort:** ~5 days at 4h/day

## Goal

Implement probability distributions, sampling methods, and maximum likelihood estimation from scratch. Build intuition for Bayesian inference, Monte Carlo methods, and statistical estimation.

## Why this matters

Probability is the language of uncertainty in ML. From loss functions (cross-entropy) to sampling (Gibbs, MCMC) to Bayesian methods, a deep understanding of probability is essential for modern ML practitioners.

## Deliverables

- [ ] Common probability distributions (Gaussian, Bernoulli, Categorical, etc.)
- [ ] Sampling methods (inverse CDF, rejection sampling, Gibbs)
- [ ] MLE and MAP estimation
- [ ] Visualization of distributions and sampling
- [ ] Blog post: `docs/blog-posts/03-probability-applied.md`

## DONE criterion

Implement complete probability module with all major distributions, sampling, and MLE capabilities.

## Setup

```bash
cd phase-0-foundations/03-probability-applied

python -m venv .venv
.\.venv\Scripts\Activate.ps1  # PowerShell

pip install -r requirements.txt
```

## Key papers / resources

- "Probability Theory" (Jaynes)
- "Pattern Recognition and Machine Learning" (Bishop) Chapter 1-2

## Status

- [ ] Started
- [ ] Derivations in notes.md
- [ ] Implementation done
- [ ] Visualizations done
- [ ] Blog post drafted
- [ ] Published
- [ ] **DONE**