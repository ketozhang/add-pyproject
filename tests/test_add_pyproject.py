# SPDX-FileCopyrightText: 2023-present Keto D. Zhang <ketozhang@gmail.com>
#
# SPDX-License-Identifier: MIT
import tomlkit
import pytest

import add_pyproject

MINIMAL = """\
[project]
name = "demo"
dependencies = []
"""


def test_add_dependency(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "pyproject.toml").write_text(MINIMAL, encoding="utf-8")

    add_pyproject.main(["requests>=2"])

    result = tomlkit.loads((tmp_path / "pyproject.toml").read_text(encoding="utf-8"))
    assert result["project"]["dependencies"] == ["requests>=2"]


def test_rejects_invalid_package(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "pyproject.toml").write_text(MINIMAL, encoding="utf-8")

    with pytest.raises(ValueError):
        add_pyproject.main(["not a valid package!!"])
