from flask import Flask, render_template
import re

app = Flask(__name__)

log_file = "auth.log"

def analyze_logs():
    failed_attempts = {}

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                ip = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line).group(1)
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    return failed_attempts


@app.route("/")
def dashboard():
    data = analyze_logs()
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)