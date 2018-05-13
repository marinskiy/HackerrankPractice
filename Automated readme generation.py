import os


def getFoldersNames(path):
    folders = []
    for item in os.listdir(path):
        if not os.path.isfile(item) and item not in ('.git', '.idea'):
            folders.append(item)
    return folders


def getFilesNames(path):
    files = os.listdir(path)
    return files


folders = getFoldersNames(os.getcwd())
for folder in folders:
    print('- ' + folder)
    subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
    for subfolder in subfolders:
        print('    ' + subfolder)
        files = getFilesNames(os.path.join(os.getcwd(), folder, subfolder))
        for file in files:
            print('        - [' + file + ']'
                  + '(https://github.com/marinskiy/HackerrankPractice/blob/master/'
                  + folder.replace(' ', '%20') + '/' + subfolder.replace(' ', '%20') + '/'
                  + file.replace(' ', '%20') + ')')
