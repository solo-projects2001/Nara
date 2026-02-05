# nara/ux/cli.py
"""
Enterprise CLI for Nara Meta-System

Commands:
- nara whoami
- nara run "<intent>"
"""

import argparse
from nara.core.loop import run


def main():
    parser = argparse.ArgumentParser(prog="nara", description="Nara Meta-System CLI")

    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("whoami")

    run_cmd = sub.add_parser("run")
    run_cmd.add_argument("intent", type=str)

    args = parser.parse_args()

    if args.cmd == "whoami":
        print("Name: Nara")
        print("Type: Meta-System (control layer)")
        print("Offline-only, deterministic, auditable.")
        return

    if args.cmd == "run":
        result = run(args.intent)
        print(result)
        return

    parser.print_help()
