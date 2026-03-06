import re

log_file = "auth.log"
alert_file = "suspicious_activity.log"

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:

            ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)

            if ip_match:
                ip = ip_match.group(1)

                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

for ip, count in failed_attempts.items():
    if count >= 3:
        alert = f"ALERT: {ip} attempted login {count} times"

        print(alert)

        with open(alert_file, "a") as f:
            f.write(alert + "\n")