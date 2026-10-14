# Deloitte Australia Technology Job Simulation

Python telemetry conversion and software development planning completed through the [Deloitte Australia Technology Job Simulation on Forage](https://www.theforage.com/simulations/deloitte-au/technology-fz0w).

This personal learning project addresses two tasks in the fictional Daikibo manufacturing scenario: reconciling machine telemetry and proposing an internal machine-health dashboard. It represents a virtual job simulation, not employment or an official Deloitte software product.

## Tasks completed

### Task 1 - Telemetry data conversion

- Convert two JSON telemetry representations into one consistent structure.
- Split a location path into country, city, area, factory and section.
- Rename flat status and temperature fields and extract nested device details.
- Convert timezone-aware ISO timestamps into exact integer Unix epoch milliseconds.
- Load JSON fixtures with UTF-8 encoding and paths relative to the project.
- Verify results with Python's `unittest`, including timestamp boundaries, timezone offsets and input preservation.

The submitted coding task passed the three supplied tests. This repository separates conversion logic from the tests and uses independently authored demo fixtures for public distribution.

### Task 2 - Software development proposal

Prepare a proposal for a single-page, intranet-only dashboard covering **four factories and nine machines per factory (36 machines)**. The proposal includes company-account authentication, expandable factory/device views, status history, an effort estimate, milestones and ongoing support.

The indicative estimate is **120 person-hours**: 72 for development, 24 for testing and 24 for integration/deployment, across three working weeks. These are planning estimates, not measured delivery hours.

Read the [proposal](docs/development-proposal.md) or its [PDF version](docs/development-proposal.pdf). The deliverable for Task 2 is a proposal; a working dashboard is not implemented in this repository.

## Tech stack

- **Python 3** for conversion logic and scripts.
- **JSON** for input fixtures and the expected output.
- **datetime, pathlib and json** from the Python standard library.
- **unittest** for automated checks.
- **ReportLab** for optional PDF generation.
- **Markdown and Git** for documentation and version control.

SQL, Excel and Power BI were not used in these two tasks.

## Project structure

```text
deloitte-technology-forage/
|-- main.py                       # Run the test suite
|-- src/
|   |-- __init__.py
|   `-- telemetry.py              # Conversion functions
|-- tests/
|   |-- __init__.py
|   `-- test_telemetry.py          # Fixture and edge-case checks
|-- data/
|   |-- README.md                 # Demo data provenance and assumptions
|   |-- data-1.json
|   |-- data-2.json
|   `-- data-result.json
|-- docs/
|   |-- development-proposal.md   # Editable proposal content
|   `-- development-proposal.pdf
|-- scripts/
|   `-- build_proposal.py          # Rebuild the portfolio PDF
|-- requirements.txt              # No third-party runtime/test dependencies
|-- requirements-docs.txt         # Optional PDF dependency
|-- .gitignore
|-- .gitattributes                # Preserve PDFs and normalize text line endings
|-- README.md
|-- ATTRIBUTION.md
`-- GITHUB_UPLOAD.md              # Windows upload commands
```

The local working copy may also contain `private_reference/`. This folder is ignored by Git and omitted from the public project archive.

## Setup and run

Use Python 3.10 or newer for a consistent setup. From the project directory:

```bash
git clone https://github.com/Yash-GenAI12/deloitte-technology-forage.git
cd deloitte-technology-forage
```

Run the tests:

```bash
python --version
python main.py
```

The conversion and test suite require no third-party packages. A successful run ends with `OK` and no test failures. To run discovery directly:

```bash
python -m unittest discover -s tests -v
```

### Use the conversion functions

```python
import json
from pathlib import Path
from src.telemetry import main as convert_telemetry

input_data = json.loads(Path("data/data-1.json").read_text(encoding="utf-8"))
result = convert_telemetry(input_data)
print(json.dumps(result, indent=2, ensure_ascii=False))
```

Run this example from the repository root. `convertFromFormat1()` and `convertFromFormat2()` can also be imported directly from `src.telemetry`.

### Regenerate the proposal PDF

The PDF is already included. To edit and rebuild it, update `docs/development-proposal.md`, then run:

```bash
python -m venv .venv
```

On Windows, activation is optional; use the environment interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-docs.txt
.\.venv\Scripts\python.exe scripts/build_proposal.py
```

On macOS/Linux:

```bash
.venv/bin/python -m pip install -r requirements-docs.txt
.venv/bin/python scripts/build_proposal.py
```

The builder uses standard PDF fonts and project-relative paths. It needs no original course template, logo or wireframe.

## Assumptions and limits

- Inputs follow the two documented schemas; missing required fields raise normal Python exceptions.
- Format 1 locations contain exactly five slash-separated components.
- Format 2 timestamps include a timezone; naive local times are rejected.
- Sub-millisecond precision is floored; timestamps remain integers.
- The proposal assumes existing telemetry/history interfaces, internal authentication and intranet hosting. Its schedule is subject to confirming these dependencies.

## Public repository contents

The public data files are fictional demo records. The portfolio proposal preserves the authored scope, estimates and plan without reproducing the supplied cover, logo or wireframe. Original course resources, submission screenshots, certificates and credentials are excluded.

See [attribution and provenance](ATTRIBUTION.md) and the [GitHub upload guide](GITHUB_UPLOAD.md).
