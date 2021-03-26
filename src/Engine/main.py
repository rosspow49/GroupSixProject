import pygame

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Engine.trackControls import *
from src.Display.ConsoleOutputs import *
from src.Display.IOLogger import IOLogger

pygame.mixer.init()


def getPlaylist(inputType, directoryPath):
    playlist = inputType.getRawData(directoryPath)
    return playlist


def getFileToPlay(fileList, logger):
    displayFiles(fileList, logger)
    valid = False
    while not valid:
        fileIdentifier = logger.TakeInput("Please enter the track number:")
        try:
            if int(fileIdentifier) not in range(len(fileList)):
                logger.ShowOutput("This is an invalid track number.")
            else:
                valid = True
        except:
            logger.ShowOutput("That is not a number")


    if int(fileIdentifier) in range(len(fileList)):
        fileIdentifier = fileList[int(fileIdentifier)]

    return fileIdentifier


def InitialiseLogs():
    with open("Logs/InputLog.txt", "w") as inputs:
        inputs.write("")
    with open("Logs/OutputLog.txt", "w") as outputs:
        outputs.write("")


def enterCommand(soundPlayer, songList, directoryPath, optionsList, volume, logger):
    print(optionsList)
    command = logger.TakeInput("Please type one of the options").lower()

    if command == "stop":
        stopSound(soundPlayer, logger)

    elif command == "play":

        songName = getFileToPlay(songList, logger)
        filePath = directoryPath + songName
        soundPlayer = playSound(filePath, volume, logger)

    elif command == "volume":
        volume = float(input("What would you like the volume to be between 0 for mute and 10?"))
        volume = volume/10

    else:
        logger.ShowOutput("That is not a valid command")

    return soundPlayer, volume


def main():
    soundPlayer = ""
    directoryPath = "Music/"
    optionsList = ["Play", "Stop", "Volume"]
    volume = 1.0
    InitialiseLogs()
    musicFiles = getPlaylist(InputDataFile(), directoryPath)
    logger = IOLogger(True)
    while True:
        soundPlayer, volume = enterCommand(soundPlayer, musicFiles, directoryPath, optionsList, volume, logger)


if __name__ == '__main__':
    main()
