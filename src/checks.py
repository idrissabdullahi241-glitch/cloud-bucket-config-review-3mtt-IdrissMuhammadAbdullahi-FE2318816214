# checks.py

def check_public_access(bucket):
    return not bucket.get("PublicAccess", False)

def check_encryption(bucket):
    return bucket.get("Encryption", False)

def check_versioning(bucket):
    return bucket.get("Versioning", False)

def check_logging(bucket):
    return bucket.get("Logging", False)

def check_lifecycle(bucket):
    return bucket.get("LifecyclePolicy", False)
