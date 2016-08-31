import os
# path should have forward slash not backslash i.e. it should have division symbol.
path = os.path.abspath("C:/Users/sony/OneDrive/Documents/Google_Drive/Google Drive/padhai_likhai/CodingStuff/Python")

for fileOrDir in os.listdir(path):
    if " " in fileOrDir:
        newName = "_".join(fileOrDir.split())
        fullNewName = path + "/" + newName
        fullOldName = path + "/" + fileOrDir
        os.rename(fullOldName, fullNewName)
        print(fileOrDir, '-->', newName)

