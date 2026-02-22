import requests

def get_headers(domain):
    try:
        r = requests.get(f"http://{domain}", timeout=5)
        return {
            "Status": r.status_code,
            "Server": r.headers.get("Server"),
            "X-Powered-By": r.headers.get("X-Powered-By"),
            "All-Headers": dict(r.headers)
        }
    except Exception as e:
        return {"error": str(e)}