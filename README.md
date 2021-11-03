# Groover Test

# Installing

```
pip install git+https://github.com/pleasedontbelong/groover.git#egg=groover
```

# Usage

- Inside python:

```sh
from groover import ...

```

- As a module, it will print a JSON representation of the atoms on the groover

```sh
python -m groover ...
```

# Development

## Install on development mode

In order to launch the tests, you must install the packages inside `requirements.dev.txt`.

Inside a virtualenv call:

```sh
pip install -r requirements.dev.txt
```

## Tests

Tests were made with pytest using coverage.

```sh
pytest .
```

You can also launch the tests on different python versions:

```sh
tox
```

## Lint

Currently using `flake8` for checking pep8 and autoformatting using `black`.

```sh
flake8 .
black . --check
```

Started 22h05
