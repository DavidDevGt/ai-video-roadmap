"""
Generic utilities for fs, json, env, and pathlib
"""

import hashlib
import json
import os
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional


# =============================================================================
# File System
# =============================================================================


def ensure_dir(path: str | Path) -> Path:
    """Ensure directory exists, create if not."""
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def find_file(name: str, start: str | Path = ".") -> Optional[Path]:
    """Find file by name recursively."""
    start = Path(start)
    for p in start.rglob(name):
        if p.is_file():
            return p
    return None


def copytree(
    src: str | Path, dst: str | Path, ignore: Optional[List[str]] = None
) -> None:
    """Copy directory tree, optionally ignoring patterns."""
    ignore = ignore or []
    src, dst = Path(src), Path(dst)
    for src_path in src.rglob("*"):
        rel = src_path.relative_to(src)
        if any(
            part.startswith(".") or matches_ignore(rel, ignore) for part in rel.parts
        ):
            continue
        dst_path = dst / rel
        if src_path.is_dir():
            dst_path.mkdir(parents=True, exist_ok=True)
        else:
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dst_path)


def matches_ignore(path: Path, patterns: List[str]) -> bool:
    """Check if path matches any ignore pattern."""
    name = path.name
    for p in patterns:
        if p.startswith("*"):
            if name.endswith(p[1:]):
                return True
        elif p.endswith("*"):
            if name.startswith(p[:-1]):
                return True
        elif p == name:
            return True
    return False


def file_hash(path: str | Path) -> str:
    """Compute MD5 hash of file."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"Not a file: {path}")
    return hashlib.md5(path.read_bytes()).hexdigest()


def dir_size(path: str | Path) -> int:
    """Get total size of directory in bytes."""
    path = Path(path)
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())


# =============================================================================
# JSON & Serialization
# =============================================================================


def save_json(data: Any, path: str | Path, indent: int = 2) -> None:
    """Save data as JSON."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=indent))


def load_json(path: str | Path) -> Any:
    """Load data from JSON."""
    return json.loads(Path(path).read_text())


def update_json(path: str | Path, upd: Dict) -> None:
    """Update JSON file in place."""
    path = Path(path)
    data = json.loads(path.read_text()) if path.exists() else {}
    data.update(upd)
    path.write_text(json.dumps(data, indent=2))


# =============================================================================
# Environment
# =============================================================================


def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get environment variable."""
    return os.environ.get(key, default)


def set_env(key: str, value: str) -> None:
    """Set environment variable."""
    os.environ[key] = value


def require_env(key: str) -> str:
    """Get required environment variable or raise."""
    val = os.environ.get(key)
    if val is None:
        raise RuntimeError(f"Required env var not set: {key}")
    return val


# =============================================================================
# Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).parent.parent


def phase_dir(phase: int) -> Path:
    """Get phase directory by number."""
    return PROJECT_ROOT / f"phase-{phase}-foundations"


def data_dir(name: str = "data") -> Path:
    """Get data directory."""
    return PROJECT_ROOT / name


def cache_dir(name: str = ".cache") -> Path:
    """Get cache directory."""
    d = PROJECT_ROOT / name
    d.mkdir(exist_ok=True)
    return d


# =============================================================================
# String Helpers
# =============================================================================


def truncate(s: str, length: int = 80, suffix: str = "...") -> str:
    """Truncate string to max length."""
    if len(s) <= length:
        return s
    return s[: length - len(suffix)] + suffix


def slugify(s: str) -> str:
    """Convert string to URL-safe slug."""
    return s.lower().replace(" ", "-").replace("_", "-")


# =============================================================================
# CLI Helpers
# =============================================================================


def confirm(prompt: str, default: bool = False) -> bool:
    """Ask for confirmation (y/n)."""
    suffix = " [Y/n]" if default else " [y/N]"
    while True:
        ans = input(prompt + suffix).lower().strip()
        if not ans:
            return default
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
