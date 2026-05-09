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

Using a Python 3.9+ virtual environment:

```bash
# Replace python3.12 with any Python 3.9+ interpreter available on your machine.
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install ".[examples]"
python -m pip check
```

## Publishing to TestPyPI from GitHub

This repository includes a GitHub Actions workflow at
`.github/workflows/publish-testpypi.yml`. To let GitHub publish to TestPyPI,
add a Trusted Publisher on TestPyPI for the existing `politxe` project:

```text
Owner: bustinduy
Repository: politxe
Workflow filename: publish-testpypi.yml
Environment name: testpypi
```

After that, publishing a new TestPyPI release is:

```bash
source .venv/bin/activate
# Update version in pyproject.toml first; TestPyPI versions are immutable.
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
git add pyproject.toml README.md src examples .github/workflows/publish-testpypi.yml
git commit -m "Release v0.1.1"
git tag v0.1.1
git push origin main --tags
```

The tag push runs GitHub Actions and uploads the package to TestPyPI.

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

See `examples/politxe_example.py` for a complete example.

## License

This project is licensed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).
