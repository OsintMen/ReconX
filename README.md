# 🔥 ReconX

**ReconX** is a **modular Python reconnaissance framework** for **authorized security testing**.  
It is designed for bug bounty hunters, pentesters, and security enthusiasts to perform recon quickly and efficiently.

> ⚠️ **Disclaimer:** Only use this tool on domains you own or are authorized to test. **Unauthorized scanning is illegal.**

---

## ✨ Features

- **Resolve target IP addresses**  
- **Fetch HTTP headers** and detect server technologies  
- **Check SSL certificate validity**  
- **Scan common ports**  
- **Discover common directories** (admin, login, dashboard, api, etc.)  
- **Dynamic ASCII banner** at the start of each scan  
- **Modular and easy to extend**  

---

## 🛠 Installation

1. **Clone the repository**

```bash
git clone https://github.com/OsintMen/reconx.git
cd reconx

2.Install required packages

pip3 install -r requirements.txt

🚀 Usage

Quick Scan (IP only)

python3 reconx.py example.com  

Full Scan (headers, SSL, ports, directories)

python3 reconx.py example.com --full

Save Results to JSON

python3 reconx.py example.com --full --output results.json




📝 Output

The tool prints:

Target IP

HTTP headers and server info

SSL certificate details (issuer, valid from/until)

Open ports

Found directories

Optional JSON export
