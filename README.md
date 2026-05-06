# politxe

`politxe` is a small Matplotlib styling helper for publication-style
scientific plots.

## Installation

From this folder:

```bash
python -m pip install .
```

For local development:

```bash
python -m pip install -e ".[examples]"
```

## Verification

Using a virtual environment to create an isolated venv:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install politxe
```

## Usage

```python
import matplotlib.pyplot as plt
from politxe import politxe

fig, ax = plt.subplots()
ax.plot([0, 1, 2], [0, 1, 0], label="signal")
ax.legend()

politxe(ax)
plt.show()
```

See `politxe_example.py` for a complete example.
