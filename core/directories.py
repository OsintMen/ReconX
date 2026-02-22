import requests

COMMON_DIRS = ["admin","login","dashboard","api","backup"]

def check_directories(domain):
    found = []
    for d in COMMON_DIRS:
        try:
            r = requests.get(f"http://{domain}/{d}", timeout=3)
            if r.status_code in [200,301,302]:
                found.append({"directory": d, "status": r.status_code})
        except:
            pass
    return found