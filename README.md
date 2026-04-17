# ai-video-roadmap

> From linear algebra to a production video-generation SaaS. Ten months. Built in public.

![status](https://img.shields.io/badge/status-phase%200-blue)
![progress](https://img.shields.io/badge/progress-0%2F30%20projects-lightgrey)
![time](https://img.shields.io/badge/commitment-20h%2Fweek-red)
![license](https://img.shields.io/badge/license-MIT-green)

I'm [David](https://github.com/DavidDevGt), a software engineer from Guatemala. I'm spending the next ~10 months going from derivative rules to shipping a working video-generation system — and I'm documenting every step.

This is not a course. It's a build log. Code, math notes, failed experiments, benchmarks, and blog posts — all in one place.

---

## Why this repo exists

Most AI tutorials stop at "run this notebook" and most papers assume you already know everything. I want the middle path: **understand the math deeply enough to derive it, implement it from scratch, and then ship a real system on real hardware.**

The end goal is a working video-generation SaaS where I understand every layer — from `∂L/∂W` to CUDA kernels to rate limiting. No black boxes.

## Who this is for

- **Me first.** This is how I learn.
- Engineers transitioning into AI infra / GPU / ML who want a concrete reference.
- Anyone curious about what it actually takes to build modern video generation.

If you find it useful, star it. If you find a bug in my math, open an issue — I'd love that.

---

## The plan

Seven phases. Each ends with a shippable artifact (a blog post, a demo, or a deployed service). No phase-skipping.

| # | Phase | Focus | Key deliverable |
|---|---|---|---|
| 0 | Foundations | NumPy-only math: linalg, calculus, probability | MLP from scratch on MNIST |
| 1 | Bridge to DL | PyTorch, autograd, optimizers, ResNet | ResNet-18 >92% on CIFAR-10 |
| 2 | Transformers | Attention, RoPE, GQA, FlashAttention | nanoGPT + Triton FA2 kernel |
| 3 | Diffusion | DDPM, Flow Matching, DiT, Latent Diffusion | DiT generating CIFAR-10 |
| 4 | Video | 3D VAE, temporal attention, Wan 2.2 | Wan 2.2 running on 8GB GPU |
| 5 | Modern LLMs | LoRA, DPO, inference engines | DPO implementation + mini-engine |
| 6 | Infra & GPU | CUDA, distributed, vLLM, SaaS | Public video-gen API endpoint |

See [`ROADMAP.md`](./ROADMAP.md) for the full project list, DONE criteria, and paper lists.
See [`docs/progress.md`](./docs/progress.md) for the weekly log.

### Progress

- [ ] Phase 0 — Foundations
- [ ] Phase 1 — Bridge to DL
- [ ] Phase 2 — Transformers
- [ ] Phase 3 — Diffusion
- [ ] Phase 4 — Video
- [ ] Phase 5 — Modern LLMs
- [ ] Phase 6 — Infra & GPU

---
