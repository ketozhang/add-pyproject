# SPDX-FileCopyrightText: 2023-present Keto D. Zhang <ketozhang@gmail.com>
#
# SPDX-License-Identifier: MIT


import argparse

import add_pyproject


def main():
    parser = argparse.ArgumentParser(
        prog="add-pyproject",
        description="Add python dependencies to pyproject.toml",
    )
    parser.add_argument(
        "packages",
        nargs="+",
        metavar="PACKAGE",
        help="package requirement to add (e.g. 'requests>=2')",
    )
    args = parser.parse_args()
    add_pyproject.main(args.packages)


if __name__ == "__main__":
    main()
