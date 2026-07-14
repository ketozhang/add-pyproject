# SPDX-FileCopyrightText: 2023-present Keto D. Zhang <ketozhang@gmail.com>
#
# SPDX-License-Identifier: MIT
import tomlkit
from packaging.requirements import InvalidRequirement, Requirement


def _validate(package: str) -> str:
    try:
        Requirement(package)
    except InvalidRequirement as e:
        raise ValueError(f"Invalid package: {package!r}") from e
    return package


def main(packages: list[str]):
    """Adds packages to pyproject.toml"""
    packages = [_validate(p) for p in packages]

    with open("pyproject.toml", "rt", encoding="utf-8") as f:
        pyproject = tomlkit.load(f)

    for package in packages:
        print(f"Adding {package} to pyproject.toml")
        pyproject["project"]["dependencies"].append(package)

    with open("pyproject.toml", "w", encoding="utf-8") as f:
        tomlkit.dump(pyproject, f)
