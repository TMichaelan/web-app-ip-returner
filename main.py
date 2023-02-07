from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return f"Your IP address is: {request.remote_addr}"

if __name__ == "__main__":
    app.run()