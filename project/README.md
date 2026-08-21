# Cumulative Course Project

This directory contains the student's own end-to-end project. It is separate
from weekly homework and from ignored instructor material in
`class_materials/`. The scaffold is intentionally complete now and will be
filled in as the course progresses.

## Directory responsibilities

| Path | Purpose |
| --- | --- |
| `data/raw/` | Direct, unedited source inputs. Corrections belong in code, not manual edits. |
| `data/processed/` | Derived tables that can be deleted and recreated from raw data and code. |
| `notebooks/` | The cumulative `project_pipeline.ipynb` and any explicitly requested project analysis notebook. |
| `src/` | Reusable modules extracted from notebooks, such as configuration, cleaning, outlier, feature, and evaluation functions. |
| `reports/` | Reader-facing summaries and deliverables. |
| `reports/images/` | Figures saved by project code. |
| `model/` | Serialized fitted model objects. |
| `docs/` | Internal memos, personas, assumptions, risks, and design notes. |

Nothing should sit loose inside `data/`; it contains only `raw/` and
`processed/`. Empty directories use `.gitkeep` so GitHub preserves the required
scaffold.

## Setup

From the repository root:

```bash
python -m pip install -r project/requirements.txt
cp project/.env.example project/.env
```

Edit only the local `.env` copy. It is ignored by Git. Keep placeholders, not
real credentials, in `.env.example`.

## Project notebook path setup

When `notebooks/project_pipeline.ipynb` is created, its first code cell must be:

```python
# --- run me first: makes this notebook work wherever it lives ---
from pathlib import Path
import os, sys

if Path.cwd().name == "notebooks":
    os.chdir("..")
ROOT = Path.cwd()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
print("working from:", ROOT.name)
```

After running that cell, import modules with `from src...` and use paths such as
`data/raw/...` and `data/processed/...`. Do not use leading slashes,
backslashes, or `../data/...`.

## Stage 06 - data preprocessing

The Stage 06 project instruction handout calls for adapting homework cleaning
logic to the actual project data. When that project work is completed, it
should add:

- reusable, documented preprocessing functions in `src/cleaning.py`;
- a reproducible raw-to-processed transformation;
- the processed dataset in `data/processed/`;
- cleaning assumptions and rationale in the pipeline notebook, this README, or
  `docs/`; and
- a pipeline cell that executes the Stage 06 work and survives a top-to-bottom
  notebook run.

## Stage 07 - outlier analysis

The required Stage 07 contribution is a reusable, documented outlier function,
normally in `src/outliers.py`, that detects, flags, removes, or otherwise
handles outliers. Recommended supporting evidence includes a sensitivity table,
visual comparison, and an assumptions note such as `docs/outliers.md`. The
cumulative pipeline should compare and document the impact of the chosen
treatment rather than silently deleting extreme observations.

These sections describe the expected locations without inventing project data
or analysis that has not yet been supplied. The instructor PDFs remain the
authoritative assignment specifications in the corresponding ignored
`class_materials/stage06...` and `class_materials/stage07...` directories.

## Pre-commit checklist

- Raw inputs are unchanged and small enough to commit.
- Processed outputs are reproducible from committed code.
- No API key, `.env`, absolute local path, or notebook checkpoint is staged.
- Reusable logic lives in `src/` and has docstrings.
- The project pipeline has been restarted and run from top to bottom.
- Assumptions, thresholds, risks, and important limitations are documented.
