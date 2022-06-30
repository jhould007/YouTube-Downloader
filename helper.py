# A place to store all utility functions
import os
from pathlib import Path
import re
import shutil

# Creates a directory in Downloads
def createFolder(name): 
    downloadPath = str(os.path.join(Path.home(), "Downloads"))
    path = os.path.join(downloadPath, name)
    os.mkdir(path)
    return str(path)

# Delete a non-empty directory from Downloads
def deleteFolder(folderName):
    downloadPath = downloadPath = str(os.path.join(Path.home(), "Downloads"))
    folderPath = downloadPath + "/" + folderName
    if os.path.isdir(folderPath): 
        shutil.rmtree(folderPath)

deleteFolder("hello")

# Processes a string into a format that can be used as a folder name
# Removes emojis and illegal characters
def cleanString(data):
#    print("Original string: " + str(data))
    emoji = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    result = re.sub(emoji, '', data).strip()
    result = result.replace("<", "")
    result = result.replace(">", "")
    result = result.replace(":", "")
    result = result.replace("\"", "")
    result = result.replace("/", "")
    result = result.replace("\\", "")
    result = result.replace("|", "")
    result = result.replace("?", "")
    result = result.replace("*", "")
    result = result.replace("  ", " ")
    result = result.replace("   ", " ")
#    print("New string: " + result)
    return result
