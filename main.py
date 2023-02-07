from flask import Flask, request, jsonify, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import yaml

app = Flask(__name__)
limiter = Limiter(app=app, key_func=get_remote_address)

client_ips = []

@app.route("/")
@limiter.limit("10/minute") # limit to 10 requests per minute per client IP
def index():

    try:

        client_ip = request.remote_addr
        client_ips.append(client_ip)

        accept_header = request.headers.get("Accept")
        
        if "html" in accept_header:
            response = make_response(f"<html><body><p>Your IP address is: {client_ip}</p></body></html>")
            response.headers["Content-Type"] = "text/html"

        elif "xml" in accept_header:
            response = make_response(f"<ip>{client_ip}</ip>")
            response.headers["Content-Type"] = "application/xml" 

        elif "yaml" in accept_header:
            response = make_response(yaml.dump({"ip": client_ip}))
            response.headers["Content-Type"] = "application/x-yaml"

        elif "txt" in accept_header:
            response = make_response(f'ip:{client_ip}')
            response.headers["Content-Type"] = "application/txt"
        
        else:
            response = make_response("Error: supported formats: xml, yaml, html, txt")

        return response
    
    except Exception as e:
            return f"An error occurred: {str(e)}"

@app.route("/history")
def history():

    try:

        return jsonify(client_ips)

    except Exception as e:
            return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run()