# AI Video Systems Roadmap - Complete Project List

## Phase 0 — Foundations (NumPy-only)

**Goal:** Build MLPs from scratch, understand the math deeply.

| # | Project | Description | Done |
|---|---|---|---|
| 0.1 | Linear Algebra Engine | Vector, Matrix, Tensor ops in pure NumPy | ☐ |
| 0.2 | Calculus Engine | Autograd, backprop from scratch | ☐ |
| 0.3 | Probability & Stats | Distributions, sampling, MLE | ☐ |
| 0.4 | MLP from Scratch | MNIST from raw NumPy, no PyTorch | ☐ |

**Papers:** None (foundational math)
**Done criteria:** Train MLP on MNIST >90% accuracy using only NumPy

---

## Phase 1 — Bridge to Deep Learning

**Goal:** Master PyTorch, build real CNNs.

| # | Project | Description | Done |
|---|---|---|---|
| 1.1 | PyTorch Fundamentals | Tensors, autograd, modules | ☐ |
| 1.2 | Optimizers from Scratch | SGD, Adam, weight decay | ☐ |
| 1.3 | CNNs & ResNet | ResNet-18 architecture | ☐ |
| 1.4 | CIFAR-10 Training | ResNet-18 >92% on CIFAR-10 | ☐ |

**Papers:** ResNet paper (He et al., 2015)
**Done criteria:** ResNet-18 achieves >92% on CIFAR-10

---

## Phase 2 — Transformers

**Goal:** Implement attention from scratch, understand modern architectures.

| # | Project | Description | Done |
|---|---|---|---|
| 2.1 | Attention from Scratch | Multi-head, scaled dot-product | ☐ |
| 2.2 | nanoGPT | GPT-2 implementation from scratch | ☐ |
| 2.3 | RoPE & GQA | Rotary Position Embedding, Grouped Query Attention | ☐ |
| 2.4 | FlashAttention-2 | Triton kernel implementation | ☐ |
| 2.5 | Fine-tuning | LoRA fine-tuning on custom dataset | ☐ |

**Papers:** Attention is All You Need, GPT-2, FlashAttention
**Done criteria:** nanoGPT generates coherent text, FA2 matches PyTorch speed

---

## Phase 3 — Diffusion Models

**Goal:** Build DDPM, DiT, understand generative models.

| # | Project | Description | Done |
|---|---|---|---|
| 3.1 | DDPM from Scratch | Implement denoising diffusion | ☐ |
| 3.2 | DDIM Sampling | Fast sampling techniques | ☐ |
| 3.3 | Flow Matching | Alternative to DDPM | ☐ |
| 3.4 | DiT (Diffusion Transformer) | ViT-based diffusion model | ☐ |
| 3.5 | Latent Diffusion | VAE + diffusion in latent space | ☐ |
| 3.6 | CIFAR-10 Generation | DiT generating CIFAR-10 images | ☐ |

**Papers:** DDPM, DDIM, Flow Matching, DiT
**Done criteria:** DiT generates CIFAR-10 images

---

## Phase 4 — Video Generation

**Goal:** Extend to temporal dimension, video models.

| # | Project | Description | Done |
|---|---|---|---|
| 4.1 | 3D CNNs for Video | Spatiotemporal convolutions | ☐ |
| 4.2 | 3D VAE | Video autoencoder | ☐ |
| 4.3 | Temporal Attention | Attention across frames | ☐ |
| 4.4 | Video Diffusion | Text-to-video generation | ☐ |
| 4.5 | Wan 2.2 Integration | Run Wan 2.2 on 8GB GPU | ☐ |
| 4.6 | Video Generation Demo | Generate short videos | ☐ |

**Papers:** Wan 2.2 paper, Video Diffusion papers
**Done criteria:** Generate 5-second videos on consumer GPU

---

## Phase 5 — Modern LLMs

**Goal:** RLHF, inference optimization.

| # | Project | Description | Done |
|---|---|---|---|
| 5.1 | LoRA Implementation | Low-rank adaptation | ☐ |
| 5.2 | DPO Implementation | Direct Preference Optimization | ☐ |
| 5.3 | vLLM Study | Understand inference engines | ☐ |
| 5.4 | Mini Inference Engine | Simple inference server | ☐ |

**Papers:** LoRA, DPO
**Done criteria:** Run inference on fine-tuned model

---

## Phase 6 — Infrastructure & Production

**Goal:** Deploy as SaaS, GPU optimization.

| # | Project | Description | Done |
|---|---|---|---|
| 6.1 | CUDA Basics | GPU programming fundamentals | ☐ |
| 6.2 | Distributed Training | Multi-GPU setup | ☐ |
| 6.3 | Model Serving | API endpoint for video generation | ☐ |
| 6.4 | Rate Limiting & Auth | Production API features | ☐ |
| 6.5 | SaaS Launch | Public video-gen API | ☐ |

**Done criteria:** Public API endpoint with video generation

---

## Running Projects

To check progress, run:
```bash
python scripts/check_progress.py
```

## Inspiration

This roadmap is inspired by:
- Andrej Karpathy's "Building a NanoGPT"
- Jeremy Howard's fast.ai
- Yann LeCun's "A Path Towards Autonomous Machine Learning"