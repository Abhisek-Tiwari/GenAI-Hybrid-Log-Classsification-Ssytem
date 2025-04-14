import re

def classify_with_regex(text):
    regex_patterns = {
        r"User User\d+ logged (in|out)." : "User Action",
        r"Account with ID .* created by .*" : "User Action",
        r"Backup (started|ended) at .*" : "System_notification",
        r"Backup completed successfully" : "System notification",
        r"System updated to version .*" : "System notification",
        r"File .* uploaded successfully by user .*" : "System notification",
        r"System reboot initiated by user .*" : "System notification",
        r"Disk cleanup completed successfully" : "System notification"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            return label
    return None