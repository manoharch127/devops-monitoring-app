from flask import Flask, render_template
import socket
import psutil
import time
import os

app = Flask(__name__)

start_time = time.time()

@app.route('/')
def dashboard():
    hostname = socket.gethostname()
    uptime = int(time.time() - start_time)
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    return render_template(
        'index.html',
        hostname=hostname,
        uptime=uptime,
        cpu=cpu,
        memory=memory,
        status="Running",
        version="v1.0.0"
    )

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

@app.route('/simulate-incident')
def simulate_incident():
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
