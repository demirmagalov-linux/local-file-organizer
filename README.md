# Local File Organizer

A Python tool that automatically sorts any directory folder into categorized subfolders, with full undo support.

## What it does

Running the organizer scans your Downloads folder and moves files into subfolders based on their type - images, videos, documents, installers, archives, and more. Every move is logged to a JSON file, so you can reverse the entire operation with the undo script if needed.

## Scripts

**local_file_organizer.py** - sorts files into categorized folders and saves a log of every move.

**undo.py** - reads the log and moves every file back to its original location, then deletes the log.

## Supported categories

Images, Videos, Documents, Audio, Code, Installers, Archives, Disk Images, 3D Files, System, and Other.

## How to use

1. Open `local_file_organizer.py` and set the `folder` variable to the path you want to organize
2. Run it with `python local_file_organizer.py`
3. If you want to reverse it, run `python undo.py`

## Requirements

Python 3. No external libraries needed - only `os`, `shutil`, and `json` from the standard library.

## Notes

The script skips subfolders and the log file itself. Files with unrecognized extensions are left in place.
