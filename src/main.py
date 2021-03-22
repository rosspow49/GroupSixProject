import pygame

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
pygame.mixer.init()


def PlaySound(filePath, currentMusic):
    if not currentMusic == "":
        currentMusic.stop()
    pygame.mixer.init()
    s = pygame.mixer.Sound("../Music/" +filePath)
    s.play()
    print("Now playing:",filePath)

    return s


def getPlaylist(inputType):
    directoryPath = "../Music"
    inputType.setDirectoryPath(directoryPath)
    playlist = inputType.getRawData()
    return playlist

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
    musicFiles = getPlaylist(InputDataFile())
    while True:
        fileName = GetFileToPlay(musicFiles)
        soundPlayer = PlaySound(fileName, soundPlayer)

if __name__ == '__main__':
    main()
