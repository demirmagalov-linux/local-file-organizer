import os
import shutil
import json

folder = r"direct file path"
log_file_path = os.path.join(folder, "move_log.json")

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv", ".odt"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".xml", ".jar"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".mid"],
    "Installers": [".exe", ".msi", ".dmg", ".pkg", ".apk"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".tar.xz"],
    "Disk Images": [".iso", ".iso.torrent", ".iso.sig"],
    "3D Files": [".fbx", ".blend", ".pxo"],
    "System": [".dll"],
    "Other": [".rmskin", ".circ", ".pdn"],
}

move_log = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isdir(filepath):
        continue
    if filepath == log_file_path:
        continue

    ext = os.path.splitext(filename)[1].lower()

    for category, extensions in categories.items():
        if ext in extensions:
            dest_folder = os.path.join(folder, category)
            os.makedirs(dest_folder, exist_ok=True)
            dest_path = os.path.join(dest_folder, filename)
            shutil.move(filepath, dest_path)
            print(f"Moved: {filename} → {category}/")
            move_log.append({"from": filepath, "to": dest_path})  
            break

with open(log_file_path, "w") as f:
    json.dump(move_log, f)