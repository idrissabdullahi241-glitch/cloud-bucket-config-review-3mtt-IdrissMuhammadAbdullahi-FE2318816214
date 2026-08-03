# report.py

def generate_report(results):
    report = "\n===== Cloud Bucket Configuration Review =====\n\n"

    for control, status in results.items():
        report += f"{control}: {'PASS' if status else 'FAIL'}\n"

    failures = list(results.values()).count(False)

    if failures == 0:
        risk = "LOW"
    elif failures <= 2:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    report += f"\nOverall Risk Level: {risk}\n"

    return report
