# FRE 5040 Bootcamp Repository

This repository separates instructor-provided class material, standalone weekly
homework, and the cumulative course project. Keeping those three areas distinct
is a course requirement and prevents scratch lecture output from becoming part
of a graded submission.

## Repository map

```text
bootcamp_mark_langlois/
├── class_materials/                 # instructor handouts; local and gitignored
│   ├── stage00_preclass-setup/
│   ├── stage01_problem-framing-and-scoping/
│   ├── ...
│   ├── stage06_data-preprocessing/
│   ├── stage07_outliers-risk-assumptions/
│   └── readings/README.md           # local guide to every course reading
├── homework/                        # standalone, graded weekly work
│   ├── homework00/
│   │   └── python_tutorial.ipynb
│   └── homework03/
│       ├── homework03_python-fundamentals_submission.ipynb
│       ├── data/raw/
│       ├── data/processed/
│       └── src/
├── project/                         # cumulative project, extended each stage
│   ├── data/raw/
│   ├── data/processed/
│   ├── notebooks/
│   ├── src/
│   ├── reports/images/
│   ├── model/
│   ├── docs/
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
├── .gitignore
└── README.md
```

## The three work areas

- `class_materials/` contains clean instructor copies and lecture-generated
  scratch files. It is ignored by Git, and class notebooks should be run from
  their own stage directories.
- `homework/homeworkNN/` contains one self-contained weekly submission. Folder
  numbers match stage numbers and are zero-padded. A homework notebook belongs
  at the homework folder root, not in a `notebooks/` subfolder.
- `project/` is the student's own cumulative dataset and analysis. It uses the
  complete scaffold from the beginning and grows through the semester.

Homework work may be adapted into the project, but the two deliverables remain
separate. Homework instructions govern homework; project instructions govern
the cumulative project.

## Environment setup

Create and activate an isolated Python environment, then install the project
dependencies from the location required by the course structure:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r project/requirements.txt
```

On Windows PowerShell, activate the environment with
`.venv\\Scripts\\Activate.ps1`.

If a task needs configuration, copy `project/.env.example` to `project/.env`
and fill in local values. Never commit a real `.env` file or API key.

## Working conventions

1. Keep source data direct and unedited in `data/raw/`.
2. Write reproducible derived data to `data/processed/`.
3. Put reusable functions in `src/`; keep notebooks focused on explanation and
   orchestration.
4. Use relative paths with forward slashes and no leading slash.
5. Restart and run a submission notebook top to bottom before committing.
6. Commit small data files needed for grading; do not commit class materials,
   secrets, caches, or notebook checkpoints.

The project notebook is the path exception because it lives inside
`project/notebooks/`. Its first cell should change the working directory to
`project/` when necessary and add that directory to `sys.path`; after that,
project code should use paths such as `data/raw/prices.csv`, never `../data/...`.

## Current runnable homework

To run Homework 03:

```bash
cd homework/homework03
jupyter lab homework03_python-fundamentals_submission.ipynb
```

The full course repository-structure handout and the comprehensive reading
guide are available locally under `class_materials/`.
