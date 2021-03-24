import pygame

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
pygame.mixer.init()


def PlaySound(filePath, currentMusic, directoryPath):
    stopSound(currentMusic)
    soundPlayer = pygame.mixer.Sound(directoryPath + "/" + filePath)
    soundPlayer.play()
    print("Now playing:",filePath)

    return soundPlayer

def stopSound(soundPlayer):
    if pygame.mixer.get_busy():
        soundPlayer.stop()
    else:
        print("There is no song playing at the moment")

def getPlaylist(inputType, directoryPath):
    playlist = inputType.getRawData(directoryPath)
    return playlist

def displayFiles(fileList):
    for entryNumber, entry in enumerate(fileList):
        print(entryNumber, ":", entry)

def GetFileToPlay(fileList):
    displayFiles(fileList)

    fileIdentifier = input("Please enter the file name or corresponding number")
    while fileIdentifier not in fileList and int(fileIdentifier) not in range(len(fileList)):
        print("This is an incorrect identifier")
        fileIdentifier = input("Please enter the file name or corresponding number")

    if int(fileIdentifier) in range(len(fileList)):
        fileIdentifier = fileList[int(fileIdentifier)]

    return fileIdentifier

def EnterCommand(soundPlayer, songList, directoryPath):
    command = input("Please enter a command")


    if command == "stop":
        stopSound(soundPlayer)


    # change to a multi step process
    elif command == "play":

        songName = GetFileToPlay(songList)
        soundPlayer = PlaySound(songName, soundPlayer, directoryPath)



    else:
        print("That is not a valid command")
    return soundPlayer



def main():
    soundPlayer = ""
    directoryPath = "Music"
    musicFiles = getPlaylist(InputDataFile(), directoryPath)
    while True:
        soundPlayer = EnterCommand(soundPlayer, musicFiles, directoryPath)
        #fileName = GetFileToPlay(musicFiles)
        #soundPlayer = PlaySound(fileName, soundPlayer)


if __name__ == '__main__':
    main()
