# SCM File Anonymizer Script

Installation:

1. Set up virtual environment.
2. Install [PyDrive] package.
3. Set up Google Drive client secrets (feel free to follow Sebastian Theiler's
   [article][connect-google-drive-to-python-using-pydrive]).
4. Run `quickstart.py` script

```
optional arguments:
  -h, --help    show this help message and exit
  -q, --query
                file name to search in Google Drive
  -t, --trashed
                optional y/n depending on whether to search in the trash bin
```

[PyDrive]:
    https://github.com/gsuitedevs/PyDrive
[connect-google-drive-to-python-using-pydrive]:
    https://medium.com/analytics-vidhya/how-to-connect-google-drive-to-python-using-pydrive-9681b2a14f20
