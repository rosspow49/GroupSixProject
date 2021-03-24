import pygame

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Display.ConsoleOutputs import *

pygame.mixer.init()


def playSound(filePath, currentMusic, directoryPath):
    stopSound(currentMusic)
    soundPlayer = pygame.mixer.Sound(directoryPath + "/" + filePath)
    soundPlayer.play()
    print("Now playing:", filePath)

    return soundPlayer

def stopSound(soundPlayer):
    if pygame.mixer.get_busy():
        soundPlayer.stop()
        print("Song stopped.")
    else:
        print("There is no song playing at the moment")

def getPlaylist(inputType, directoryPath):
    playlist = inputType.getRawData(directoryPath)
    return playlist

def getFileToPlay(fileList):
    displayFiles(fileList)

    fileIdentifier = input("Please enter the track number: ")
    while int(fileIdentifier) not in range(len(fileList)):
        print("This is an incorrect identifier")
        fileIdentifier = input("Please enter the track number: ")

    if int(fileIdentifier) in range(len(fileList)):
        fileIdentifier = fileList[int(fileIdentifier)]

    return fileIdentifier

def enterCommand(soundPlayer, songList, directoryPath):
    command = input("Please enter a command")


    if command == "stop":
        stopSound(soundPlayer)


    # change to a multi step process
    elif command == "play":

        songName = getFileToPlay(songList)
        soundPlayer = playSound(songName, soundPlayer, directoryPath)

    else:
        print("That is not a valid command")
    return soundPlayer


def main():
    soundPlayer = ""
    directoryPath = "Music"
    musicFiles = getPlaylist(InputDataFile(), directoryPath)
    while True:
        soundPlayer = enterCommand(soundPlayer, musicFiles, directoryPath)


if __name__ == '__main__':
    main()
