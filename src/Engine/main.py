import pygame

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Display.ConsoleOutputs import *
pygame.mixer.init()
from src.Display.IOLogger import IOLogger


def PlaySound(filePath, currentMusic, directoryPath, logger):
    if pygame.mixer.get_busy():
        currentMusic.stop()
    pygame.mixer.init()
    soundPlayer = pygame.mixer.Sound(directoryPath + "/" + filePath)
    soundPlayer.play()
    logger.ShowOutput("Now playing:" + filePath)

    return soundPlayer

def stopSound(soundPlayer, logger):
    if pygame.mixer.get_busy():
        soundPlayer.stop()
        logger.ShowOutput("Song stopped.")
    else:
        logger.ShowOutput("There is no song playing at the moment")

def getPlaylist(inputType, directoryPath):
    playlist = inputType.getRawData(directoryPath)
    return playlist

def getFileToPlay(fileList, logger):
    displayFiles(fileList, logger)

    fileIdentifier = logger.TakeInput("Please enter the track number:")
    while int(fileIdentifier) not in range(len(fileList)):
        logger.ShowOutput("This is an invalid track number.")
        fileIdentifier = logger.TakeInput("Please enter the track number:")

    if int(fileIdentifier) in range(len(fileList)):
        fileIdentifier = fileList[int(fileIdentifier)]

    return fileIdentifier

def InitialiseLogs():
    with open("Logs/InputLog.txt", "w") as inputs:
        inputs.write("")
    with open("Logs/OutputLog.txt", "w") as outputs:
        outputs.write("")

def enterCommand(soundPlayer, songList, directoryPath):
    command = input("Please enter a command")

    if command == "stop":
        stopSound(soundPlayer)

    elif command == "play":

        songName = getFileToPlay(songList, logger)
        soundPlayer = playSound(songName, soundPlayer, directoryPath, logger)

    else:
        logger.ShowOutput("That is not a valid command")

    return soundPlayer


def main():
    soundPlayer = ""
    directoryPath = "Music"
    InitialiseLogs()
    musicFiles = getPlaylist(InputDataFile(), directoryPath)
    while True:
        soundPlayer = enterCommand(soundPlayer, musicFiles, directoryPath)


if __name__ == '__main__':
    main()
