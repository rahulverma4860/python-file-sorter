# 📁 File Sorter App for macOS

A Python desktop app that organizes messy folders into category-based subfolders like Images, Documents, Videos, Audio, Archives, and Others.

## ✨ Features

* Select any folder from your system
* Preview file categories before sorting
* Confirm before execution
* Smart file categorization
* Duplicate file handling with auto-renaming
* Case-insensitive extension support
* Packaged as a macOS `.app` using `py2app`

## 🛠 Tech Stack

* Python
* Tkinter
* py2app
* os
* shutil

## 📸 Screenshots

### Main App Window

![App View](Screenshots/Sorter_1.png)

### Folder Selection

![Folder Selection](Screenshots/Sorter_2.png)

### Folder Selected

![Folder Selected](Screenshots/Sorter_3.png)

### Confirmation Popup

![Confirmation](Screenshots/Sorter_4.png)

### Files Moved Result

![Files Moved](Screenshots/Sorter_5.png)

### Sorted Folder Output

![Sorted Folder](Screenshots/Sorter_6.png)

## ▶️ Run Locally

```bash
python main.py
```

## 📦 Build the macOS App

```bash
python setup.py py2app
```

Then open:

```bash
dist/File_Sorter.app
```

## 📂 Project Structure

```text
main.py  
sorter.py  
setup.py  
README.md  
requirements.txt  
Screenshots/  
```

## 🚀 Future Improvements

* Progress bar during sorting
* Drag and drop folder support
* Custom category editing
* Dark mode interface
* Windows version

## 👨‍💻 Author

**Rahul Verma**
Python Developer | Automation Enthusiast