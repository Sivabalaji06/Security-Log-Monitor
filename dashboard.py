import matplotlib.pyplot as plt
import re

log_file = "auth.log"

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line).group(1)
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

ips = list(failed_attempts.keys())
attempts = list(failed_attempts.values())

plt.bar(ips, attempts)
plt.title("SOC Attack Detection Dashboard")
plt.xlabel("Attacker IP Address")
plt.ylabel("Failed Login Attempts")

plt.show()