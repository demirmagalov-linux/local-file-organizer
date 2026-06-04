import os
import shutil
import json

log_path = r"direct file path"

if os.path.exists(log_path):
    with open(log_path, "r") as f:
        for entry in json.load(f):
            try: shutil.move(entry["to"], entry["from"])
            except Exception as e: print(f"Skipped: {e}")
    os.remove(log_path)
