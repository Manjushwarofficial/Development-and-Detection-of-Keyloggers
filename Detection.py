import psutil

# Keywords to look for in running processes
suspect_keywords = ["key", "log", "pynput", "hook"]

def detect_suspect_processes():
    print("Scanning for keylogger processes...\n")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for keyword in suspect_keywords:
                if keyword in proc.info['name'].lower():
                    print(f"⚠️ Suspicious Process Found: {proc.info['name']} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

detect_suspect_processes()
