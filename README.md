# my_notes

A personal collection of notes, code snippets, learning notebooks, and small standalone projects. Everything is organised into three top-level areas.

## `docs/` — notes & learning material

| Path | Contents |
|---|---|
| `docs/notebooks/statistics/` | Least squares, Metropolis sampling, the [Kalman filter](docs/notebooks/statistics/) |
| `docs/notebooks/PDEs/` | Heat equation and other PDE explorations |
| `docs/notebooks/finance/` | Random number generators, the Markowitz model |
| `docs/notebooks/machine learning/` | ML experiments (e.g. MNIST with TensorFlow) |
| `docs/notebooks/LLM/` | Large-language-model experiments |
| `docs/notebooks/_lib_py/` | Shared helper code imported by the notebooks |
| `docs/latex/` | LaTeX documents (`notes/`, `crochet/`) |

Notebooks are written to teach: intuition first, then the math, then runnable examples. New ones can be scaffolded with the `/new-notebook` command (see [`.claude/commands/`](.claude/commands/)).

## `snippets/` — short, language-grouped code samples

Reference snippets grouped by language/tool: `Bash`, `CPP`, `Python`, `go`, `Haskell`, `java`, `php`, `R`, `arduino`, `raspberry-pi`, `Makefile`, `PBS`.

## `repos/` — small standalone projects (backups)

| Project | Description |
|---|---|
| [CannyEdgeDetector](repos/CannyEdgeDetector/) | Canny edge-detection implementation |
| [EikonalEquation](repos/EikonalEquation/) | Eikonal equation solver |
| [GitTagHelper](repos/GitTagHelper/) | Utility to keep a repo's tags organised |
| [MaJOrCA](repos/MaJOrCA/) | Multiple JObs CreAtor — batch/PBS job generator |
| [MazeGenerator](repos/MazeGenerator/) | Generate and solve random mazes |
| [MineSweeper](repos/MineSweeper/) | Minesweeper implementation |
| [PUlSe](repos/PUlSe/) | Python Utilities Suite |
| [sudoku](repos/sudoku/) | Sudoku solver |

## Conventions

- Notebooks target Python 3 (numpy / matplotlib / scipy / pandas).
- Generated artefacts (`__pycache__/`, `.ipynb_checkpoints/`, `*.pyc`, editor backups) are git-ignored.
