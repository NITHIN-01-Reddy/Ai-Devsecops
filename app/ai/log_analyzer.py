import os


LOG_FILE = "logs/app.log"


def analyze_logs():

    if not os.path.exists(LOG_FILE):
        return {
            "error": "Log file not found"
        }

    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    error_logs = []

    for log in logs:
        if "ERROR" in log or "Exception" in log:
            error_logs.append(log.strip())

    total_errors = len(error_logs)

    if total_errors == 0:
        severity = "LOW"

        recommendation = (
            "No critical issues detected."
        )

    elif total_errors < 5:
        severity = "MEDIUM"

        recommendation = (
            "Review application exceptions and monitor logs."
        )

    else:
        severity = "HIGH"

        recommendation = (
            "Multiple failures detected. Immediate investigation recommended."
        )

    return {
        "total_logs_analyzed": len(logs),
        "errors_detected": total_errors,
        "severity": severity,
        "recent_errors": error_logs[-5:],
        "recommendation": recommendation
    }