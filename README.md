# add-pyproject

[![PyPI - Version](https://img.shields.io/pypi/v/add-pyproject.svg)](https://pypi.org/project/add-pyproject)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/add-pyproject.svg)](https://pypi.org/project/add-pyproject)

It just adds python dependencies to pyproject.toml

-----

## Installation

```console
pip install add-pyproject
```

## Usage

### Hatch

```toml
[project]
# ...
dependencies = [
  "foobar"
]

[tool.hatch.envs.default]
dependencies = [
  "add-pyproject"
]

[tool.hatch.envs.default.scripts]
add = "python -m add_pyproject {args}"
```

```console
$ hatch run add numpy>=1.26
```

## License

`add-pyproject` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
