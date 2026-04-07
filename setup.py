from setuptools import setup

APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "packages" : ["tkinter"],
    # "iconfile" : "icon.icns",
    "plist": {
        "CFBundleName": "File Sorter",
        "CFBundleDisplayName": "File Sorter",
        "CFBundleIdentifier": "com.rahul.filesorter",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0.0",
    }
}


setup(
    app = APP,
    data_files = DATA_FILES,
    options = {"py2app" : OPTIONS},
    setup_requires = ["py2app"],
)