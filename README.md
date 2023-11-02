# High Performance Manufacturing 
Environmental Practices, Environmental Performance & Lean (moderating variable)

## Folder Structure
```
hpm/
│
├── .venv/ # Virtual environment folder
│
├── notebooks/          # Jupyter notebooks
│   ├── exploratory/    # Initial explorations and analyses
│   └── final/          # Final, cleaned-up notebooks
│
├── data/               # All data files
│   ├── raw/            # Unprocessed data
│   ├── processed/      # Cleaned and transformed data
│
├── output/             # Any output files, charts, tables, etc.
│
├── scripts/            # Python or other scripts
│
└── reports/            # Generated analysis as HTML, PDF, LaTeX, etc.
    └── figures/        # Generated graphics and figures used in the report
```
## Installation

1. Clone the repository: `git clone git@github.com:johnmalcolm/hpm.git`
2. Navigate to the project directory: `cd hpm`
3. Create a virtual environment: `python3 -m venv .venv`
4. Activate the virtual environment:
    - On macOS and Linux: `source .venv/bin/activate`
    - On Windows: `.\.venv\Scripts\activate`
5. Install the required packages: `pip install -r requirements.txt`

## Usage with VSCode

1. Ensure that you have [Visual Studio Code (VSCode)](https://code.visualstudio.com/) installed.

2. Ensure the [VSCode Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) is installed.

3. Open the project directory in VSCode.

4. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS) and type "Python: Select Interpreter". Choose the interpreter that corresponds to the virtual environment you created (`.venv`).

5. Navigate to the `notebooks/` directory in the VSCode explorer to open and edit the Jupyter notebooks. You can run cells directly in VSCode.

- Raw data files are stored in the `data/raw/` directory.
- Processed data files are stored in the `data/processed/` directory.

