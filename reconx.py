#!/usr/bin/env python3

import argparse
import json
from utils.banner import print_banner
from colorama import Fore, init
from core.dns import get_ip
from core.http import get_headers
from core.sslcheck import get_ssl_info
from core.ports import scan_ports
from core.directories import check_directories

init(autoreset=True)

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="ReconX - Modular Recon Framework")
    parser.add_argument("target")
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--output")

    args = parser.parse_args()
    target = args.target
    results = {}

    print(Fore.CYAN + f"\n[+] ReconX scanning {target}\n")

    results["IP"] = get_ip(target)

    if args.full:
        results["HTTP"] = get_headers(target)
        results["SSL"] = get_ssl_info(target)
        results["Open Ports"] = scan_ports(target)
        results["Directories"] = check_directories(target)

    print(Fore.GREEN + "\n[+] Scan Complete\n")
    print(json.dumps(results, indent=4))

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)

if __name__ == "__main__":
    main()



