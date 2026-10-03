"""Hosts File Guard — Edit the Windows hosts file with a preview, checksum, and one-click rollback to the last good copy."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='hosts_file_guard',
        description='Edit the Windows hosts file with a preview, checksum, and one-click rollback to the last good copy.',
    )
    parser.add_argument('path', nargs='?', help='Hosts draft file')
    parser.add_argument('--apply', help='Write after preview')
    parser.add_argument('--rollback', help='Restore last backup')
    args = parser.parse_args()
    print('Hosts File Guard')
    print('A safer way to edit C:\\Windows\\System32\\drivers\\etc\\hosts.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
