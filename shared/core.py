"""
Shared utilities
"""

import numpy as np
from typing import Callable, Optional, Tuple, Union
import time

EPSILON = 1e-10


# =============================================================================
# Validation
# =============================================================================


def assert_shape(a: np.ndarray, shape: Tuple[int, ...], name: str = "array") -> None:
    """Assert that array has expected shape."""
    if a.shape != shape:
        raise ValueError(f"{name} expected shape {shape}, got {a.shape}")


def assert_2d(a: np.ndarray, name: str = "array") -> None:
    """Assert that array is 2D."""
    if a.ndim != 2:
        raise ValueError(f"{name} must be 2D, got {a.ndim}D")


def assert_vector(a: np.ndarray, name: str = "array") -> None:
    """Assert that array is 1D."""
    if a.ndim != 1:
        raise ValueError(f"{name} must be 1D, got {a.ndim}D")


def assert_square(a: np.ndarray, name: str = "matrix") -> None:
    """Assert that matrix is square."""
    assert_2d(a, name)
    if a.shape[0] != a.shape[1]:
        raise ValueError(f"{name} must be square, got shape {a.shape}")


# =============================================================================
# Shape Manipulation
# =============================================================================


def ensure_column_vector(v: np.ndarray) -> np.ndarray:
    """Ensure 1D array becomes column vector (n, 1)."""
    if v.ndim == 1:
        return v.reshape(-1, 1)
    return v


def ensure_1d(v: np.ndarray) -> np.ndarray:
    """Ensure array is 1D, flatten if needed."""
    return v.flatten()


# =============================================================================
# Numeric Comparisons
# =============================================================================


def is_zero(x: float) -> bool:
    """Check if value is effectively zero."""
    return abs(x) < EPSILON


def isclose(a: float, b: float, rel_tol: float = 1e-9) -> bool:
    """Check if two floats are close."""
    return abs(a - b) < max(rel_tol * max(abs(a), abs(b)), EPSILON)


# =============================================================================
# Random Generation
# =============================================================================


def set_seed(seed: int) -> None:
    """Set global random seed for reproducibility."""
    np.random.seed(seed)


def randn(*shape: int, seed: Optional[int] = None) -> np.ndarray:
    """Generate random array from standard normal distribution."""
    if seed is not None:
        state = np.random.get_state()
        np.random.seed(seed)
        result = np.random.randn(*shape)
        np.random.set_state(state)
        return result
    return np.random.randn(*shape)


def rand(*shape: int, seed: Optional[int] = None) -> np.ndarray:
    """Generate uniform random array in [0, 1)."""
    if seed is not None:
        state = np.random.get_state()
        np.random.seed(seed)
        result = np.random.rand(*shape)
        np.random.set_state(state)
        return result
    return np.random.rand(*shape)


# =============================================================================
# Activation Functions
# =============================================================================


def sigmoid(x: np.ndarray) -> np.ndarray:
    """Numerically stable sigmoid: sigma(x) = 1 / (1 + exp(-x))."""
    return np.where(x >= 0, 1 / (1 + np.exp(-x)), np.exp(x) / (1 + np.exp(x)))


def sigmoid_grad(x: np.ndarray) -> np.ndarray:
    """Derivative of sigmoid: d/dx sigma(x) = sigma(x) * (1 - sigma(x))."""
    s = sigmoid(x)
    return s * (1 - s)


def relu(x: np.ndarray) -> np.ndarray:
    """ReLU activation: max(0, x)."""
    return np.maximum(0, x)


def relu_grad(x: np.ndarray) -> np.ndarray:
    """Derivative of ReLU: 1 if x > 0 else 0."""
    return (x > 0).astype(x.dtype)


def leaky_relu(x: np.ndarray, alpha: float = 0.01) -> np.ndarray:
    """Leaky ReLU: x if x > 0 else alpha * x."""
    return np.where(x > 0, x, alpha * x)


def leaky_relu_grad(x: np.ndarray, alpha: float = 0.01) -> np.ndarray:
    """Derivative of Leaky ReLU: 1 if x > 0 else alpha."""
    return np.where(x > 0, 1, alpha)


# =============================================================================
# Softmax & Log-Sum-Exp
# =============================================================================


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Numerically stable softmax."""
    x = x - np.max(x, axis=axis, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)


def log_softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Numerically stable log-softmax."""
    x = x - np.max(x, axis=axis, keepdims=True)
    return x - np.log(np.sum(np.exp(x), axis=axis, keepdims=True))


def logsumexp(x: np.ndarray, axis: int = -1, keepdims: bool = False) -> np.ndarray:
    """Numerically stable log-sum-exp."""
    x_max = np.max(x, axis=axis, keepdims=True)
    x = x - x_max
    result = np.log(np.sum(np.exp(x), axis=axis, keepdims=keepdims))
    return result + x_max if keepdims else result + np.squeeze(x_max, axis=axis)


# =============================================================================
# Loss Functions
# =============================================================================


def cross_entropy(pred: np.ndarray, labels: np.ndarray, eps: float = 1e-9) -> float:
    """Cross-entropy loss: -sum(y * log(p)) / n."""
    pred = np.clip(pred, eps, 1 - eps)
    return -np.mean(np.sum(labels * np.log(pred), axis=1))


def accuracy(pred: np.ndarray, labels: np.ndarray) -> float:
    """Compute accuracy: mean(argmax(pred) == labels)."""
    return np.mean(np.argmax(pred, axis=1) == labels)


def one_hot(labels: np.ndarray, num_classes: int) -> np.ndarray:
    """Convert labels to one-hot encoding."""
    return np.eye(num_classes)[labels]


# =============================================================================
# Gradient Checking
# =============================================================================


def gradient_check(
    f: Callable[[np.ndarray], np.ndarray],
    x: np.ndarray,
    grad: np.ndarray,
    eps: float = 1e-5,
) -> float:
    """Check numerical gradient against analytical gradient.

    Uses central differences: (f(x+eps) - f(x-eps)) / (2*eps)

    Args:
        f: Function that computes loss/forward pass
        x: Input array to check gradients for
        grad: Analytical gradient to compare against
        eps: Perturbation amount

    Returns:
        Maximum relative error between numerical and analytical gradients.
    """
    x = x.copy()
    num_grad = np.zeros_like(grad)
    it = np.nditer(x, flags=["multi_index"])

    while not it.finished:
        idx = it.multi_index
        old_val = x[idx]

        x[idx] = old_val + eps
        f_plus = f(x)

        x[idx] = old_val - eps
        f_minus = f(x)

        x[idx] = old_val
        num_grad[idx] = (f_plus - f_minus) / (2 * eps)

        it.iternext()

    diff = np.abs(num_grad - grad)
    denom = np.maximum(np.abs(num_grad) + np.abs(grad), 1e-8)
    return np.max(diff / denom)


# =============================================================================
# Debug & Profiling
# =============================================================================


def timeit(func: Callable, *args, **kwargs) -> Tuple[float, any]:
    """Time function execution.

    Returns:
        Tuple of (elapsed time in seconds, function result).
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return elapsed, result


def describe(x: np.ndarray, name: str = "array") -> str:
    """Generate descriptive string for array."""
    return f"{name}: shape={x.shape}, dtype={x.dtype}, min={x.min():.4f}, max={x.max():.4f}, mean={x.mean():.4f}"


def print_array(x: np.ndarray, name: str = "array", precision: int = 4) -> None:
    """Pretty print array with header."""
    np.set_printoptions(precision=precision, suppress=True, linewidth=120)
    print(f"{name} {x.shape}:")
    print(x)
    print()
