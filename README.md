# sphinx-doctest
Testrepo for generating Python api-documentation from docstrings, using sphinx,
and publish to GitHub pages.

It contains a simple python source file with some documentation, and a test,
to verify that the test directory is excluded from the documentation.

## Install and run
```shell
pipenv install --dev
pipenv run pytest
```

## Documentation
The API-documentation for this repo is generated from docstrings in the Python
source code, using the [Sphinx tool](https://www.sphinx-doc.org/).

### Generate documentation
Go to the docs-directory and run the following commands:
```shell
pipenv run sphinx-apidoc -o . ../ ../processing/tests
pipenv run make html
```

Then open the `_build/html/index.html` file to view the documentation.
