from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('Status request successfull')
    return {"version": "v1", "status": "ok"}

@app.route("/metrics")
def metrics():
    app.logger.info('Metrics request successfull')
    return {"rps": "0"}

if __name__ == "__main__":
    logging.basicConfig(filename="app.log", level=logging.DEBUG)
    app.run(host='0.0.0.0')
