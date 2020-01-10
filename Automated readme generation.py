import os
import functools


def getFoldersNames(path):
    folders = []
    for item in os.listdir(path):
        if not os.path.isfile(item) and item not in ('.git', '.idea'):
            folders.append(item)
    return folders


def getFilesNames(path):
    files = os.listdir(path)
    return files


def getProblemURLandScore(path):
    inFile = open(path, 'r', encoding='utf-8')
    url = inFile.readline().split()[-1]
    score = inFile.readline().split()[-1]
    inFile.close()
    return url, score


def getTotalNumberOfProblems():
    totalNumber = 0
    folders = getFoldersNames(os.getcwd())
    for folder in folders:
        subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
        for subfolder in subfolders:
            totalNumber += len(getFilesNames(os.path.join(os.getcwd(), folder, subfolder)))
    return totalNumber


readmeFile = open('README.md', 'w', encoding='utf-8')
print('<p align="center"><a href="https://www.hackerrank.com/marinskiy"><img src="https://i0.wp.com/gradsingames.com/wp-content/uploads/2016/05/856771_668224053197841_1943699009_o.png" ></a></p>', file=readmeFile)
print(file=readmeFile)
print('# Solutions to Hackerrank practice problems', file=readmeFile)
print('This repository contains ' + str(getTotalNumberOfProblems()) + ' solutions to Hackerrank practice problems with Python 3, C++ and Oracle SQL.', file=readmeFile)
print(file=readmeFile)
print('Updated daily :) If it was helpful please press a star.', file=readmeFile)
print(file=readmeFile)
print('[![GitHub last commit](https://img.shields.io/github/last-commit/marinskiy/HackerrankPractice.svg)](https://github.com/marinskiy/HackerrankPractice) ', file=readmeFile)
print('[![GitHub commit activity the past week, 4 weeks, year](https://img.shields.io/github/commit-activity/y/marinskiy/HackerrankPractice.svg)](https://github.com/marinskiy/HackerrankPractice)', file=readmeFile)
print('[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/marinskiy/HackerrankPractice.svg)](https://github.com/marinskiy/HackerrankPractice) ', file=readmeFile)
print('[![GitHub stars](https://img.shields.io/github/stars/marinskiy/HackerrankPractice.svg)](https://github.com/marinskiy/HackerrankPractice)', file=readmeFile)
print(file=readmeFile)

folders = getFoldersNames(os.getcwd())
for folder in sorted(folders):
    print('- ' + folder, file=readmeFile)
    subfolders = getFoldersNames(os.path.join(os.getcwd(), folder))
    for subfolder in sorted(subfolders):
        print('    ' + subfolder, file=readmeFile)
        files = getFilesNames(os.path.join(os.getcwd(), folder, subfolder))
        for file in sorted(files):
            if file.endswith(('.cpp', '.py', '.sql')):
                url, score = getProblemURLandScore(os.path.join(os.getcwd(), folder, subfolder, file))
                print('        - ' + "".join(file.split(".")[1:-1])[1:]
                      + ' | [Problem](' + url
                      + ')'
                      + ' | [Solution]'
                      + '(https://github.com/marinskiy/HackerrankPractice/blob/master/'
                      + folder.replace(' ', '%20') + '/' + subfolder.replace(' ', '%20') + '/'
                      + file.replace(' ', '%20') + ')'
                      + ' | Score: ' + str(score), file=readmeFile)

readmeFile.close()
