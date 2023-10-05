# SPDX-FileCopyrightText: 2023-present Keto D. Zhang <ketozhang@gmail.com>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from add_pyproject.cli import add_pyproject

    args = sys.argv[1:]
    sys.exit(add_pyproject(args[0]))
