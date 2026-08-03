# review.py

import json

from checks import (
    check_public_access,
    check_encryption,
    check_versioning,
    check_logging,
    check_lifecycle
)

from report import generate_report


def load_bucket_config(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def review_bucket(bucket):

    results = {
        "Public Access Blocked": check_public_access(bucket),
        "Encryption Enabled": check_encryption(bucket),
        "Versioning Enabled": check_versioning(bucket),
        "Logging Enabled": check_logging(bucket),
        "Lifecycle Policy Enabled": check_lifecycle(bucket)
    }

    return results


if __name__ == "__main__":

    bucket = load_bucket_config("../data/sample_bucket.json")

    results = review_bucket(bucket)

    print(generate_report(results))
