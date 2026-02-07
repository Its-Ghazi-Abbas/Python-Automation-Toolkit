# File Organizer (Python)

## Overview
This Python script automatically organizes files in a folder by type into a **master folder**.  
It is designed for freelancers, small business users, and anyone who wants a clean file structure quickly.

---

## Features
- Categorizes files into: **PDFs, Images, Videos, Applications, Others**
- Moves files safely to a **master folder** called `Organized_Files`
- Default source folder is **Downloads**, but user can choose any folder
- Default output folder is the same as source, but user can choose any folder
- Counts total files scanned, moved, and skipped
- Handles files with no extension by placing them in **Others**
- Safe: skips files already existing in the destination

---

## Requirements
- Python 3.7 or higher
- Works on Windows, macOS, Linux

---

## Usage
1. Clone or download this repository.
2. Run the script:

```bash
python organizer.py

``` Follow prompts:
- Enter the folder to organize (Press Enter for default Downloads)
- Enter the output folder (Press Enter for same as source)
``` The script will create a Organized_Files folder and sort all files into categories.

``` Example Folder Structure After Running
Organized_Files/
├── PDFs/
├── Images/
├── Videos/
├── Applications/
└── Others/

## License
This project is open-source and free to use.

