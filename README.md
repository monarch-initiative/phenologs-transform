# phenolog-transform

| [Documentation](https://monarch-initiative.github.io/phenolog_transform) |

transform raw phenolog output to kgx format

## Requirements

- Python >= 3.10
- [Poetry](https://python-poetry.org/docs/#installation)

## Starting a new project

Upon creating a new project from the `cookiecutter-monarch-ingest` template, you can install and test the project:

```bash
cd phenolog-transform
make install
make test
```

There are a few additional steps to complete before the project is ready for use. 

#### GitHub Repository

1. Create a new repository on GitHub.
1. Enable GitHub Actions to read and write to the repository (required to deploy the project to GitHub Pages).
   - in GitHub, go to  Settings -> Action -> General -> Workflow permissions and choose read and write permissions
1. Initialize the local repository and push the code to GitHub. For example:

   ```bash
   cd phenolog-transform
   git init
   git remote add origin https://github.com/<username>/<repository>.git
   git add -A && git commit -m "Initial commit"
   git push -u origin main
   ```

#### Transform Code and Configuration

1. Edit the `download.yaml`, `transform.py`, `transform.yaml`, and `metadata.yaml` files to suit your needs.
   - For more information, see the [Koza documentation](https://koza.monarchinitiative.org) and [kghub-downloader](https://github.com/monarch-initiative/kghub-downloader).
1. Add any additional dependencies to the `pyproject.toml` file.
1. Adjust the contents of the `tests` directory to test the functionality of your transform.

#### Documentation

1. Update this `README.md` file with any additional information about the project.
1. Add any appropriate documentation to the `docs` directory.

Once you have completed these steps, you can remove this section from the `README.md` file.

## Installation

```bash
cd phenolog-transform
make install
# or
poetry install
```

> **Note** that the `make install` command is just a convenience wrapper around `poetry install`.

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

Download the data for the phenolog_transform transform:

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

### Testing

To run the test suite:

```bash
make test
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
