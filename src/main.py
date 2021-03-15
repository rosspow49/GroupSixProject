import pygame
pygame.mixer.init()
import os


def PlaySound(filePath, currentMusic):
    if not currentMusic == "":
        currentMusic.stop()
    pygame.mixer.init()
    s = pygame.mixer.Sound("../Music/" +filePath)
    s.play()
    print("Now playing:",filePath)

    return s



def GetFileList():
    files = os.listdir("../Music")
    return files

def displayFiles(fileList):
    for entryNumber, entry in enumerate(fileList):
        print(entryNumber, ":", entry)

def GetFileToPlay(fileList):
    displayFiles(fileList)

    fileIdentifier = input("Please enter the file name or corresponding number")
    while fileIdentifier not in fileList  and  int(fileIdentifier) not in range(len(fileList)):
        print("This is an incorrect identifier")
        fileIdentifier = input("Please enter the file name or corresponding number")

    if int(fileIdentifier) in range(len(fileList)):
        fileIdentifier = fileList[int(fileIdentifier)]

    return fileIdentifier


def main():
    soundPlayer = ""
    musicFiles = GetFileList()
    while True:
        fileName = GetFileToPlay(musicFiles)
        soundPlayer = PlaySound(fileName, soundPlayer)

main()