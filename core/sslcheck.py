import ssl
import socket

def get_ssl_info(domain):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(3)
            s.connect((domain, 443))
            cert = s.getpeercert()
            return {
                "Issuer": cert.get("issuer"),
                "Valid From": cert.get("notBefore"),
                "Valid Until": cert.get("notAfter")
            }
    except:
        return {"error": "SSL not available"}