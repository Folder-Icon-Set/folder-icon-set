"""Folder Icon Set — Set a custom icon on a Windows folder via desktop.ini."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='folder_icon_set',
        description='Set a custom icon on a Windows folder via desktop.ini.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Folder Icon Set')
    print('A labeled folder without a third-party skin pack.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
