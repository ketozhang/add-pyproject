# add-pyproject

[![PyPI - Version](https://img.shields.io/pypi/v/add-pyproject.svg)](https://pypi.org/project/add-pyproject)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/add-pyproject.svg)](https://pypi.org/project/add-pyproject)

A CLI that just adds python dependencies directly into `pyproject.toml`

<table align="center">
<tr>
<td colspan="2">
  
```console
$ python -m add_pyproject numpy>=1.26
```

</td>
</tr>

<tr>
<td>

Before
```toml
[project]
name = "mypackage"
version = "0.1.0"
dependencies = ["foobar"]
```

</td>

<td>

After
```toml
[project]
name = "mypackage"
version = "0.1.0"
dependencies = ["foobar", "numpy>=1.26"]
```
</td>
</tr>
</table>

-----

## Installation

```console
pip install add-pyproject
```

## Integration

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


