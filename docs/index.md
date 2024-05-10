# phenolog-transform

transform raw phenolog output to kgx format

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements

- Python >= 3.10
- [Poetry](https://python-poetry.org/docs/#installation)

## Installation

```bash
cd phenolog-transform
make install
# or
poetry install
```

> **Note** that the `make install` command is a convenience wrapper around `poetry install`.

Once installed, you can check that everything is working as expected:

```bash
# Run the pytest suite
make test
# Download the data and run the Koza transform
make download
make run
```

## Usage

This project is set up with a Makefile for common tasks.  
To see available options:

```bash
make help
```

### Download and Transform

To download the data for the phenolog_transform transform:

```bash
poetry run phenolog_transform download
```

To run the Koza transform for phenolog-transform:

```bash
poetry run phenolog_transform transform
```

To see available options:

```bash
poetry run phenolog_transform download --help
# or
poetry run phenolog_transform transform --help
```

---

> This project was generated using [monarch-initiative/cookiecutter-monarch-ingest](https://github.com/monarch-initiative/cookiecutter-monarch-ingest).  
> Keep this project up to date using cruft by occasionally running in the project directory:
>
> ```bash
> cruft update
> ```
>
> For more information, see the [cruft documentation](https://cruft.github.io/cruft/#updating-a-project)
