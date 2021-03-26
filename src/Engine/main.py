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


def enterCommand(soundPlayer, songList, directoryPath, optionsList, volume, close, logger):
    displayOptions(logger)
    command = logger.TakeInput("Please type one of the options").lower()

    if command == "stop":
        stopSound(soundPlayer, logger)

    elif command == "play":

        songName = getFileToPlay(songList, logger)
        filePath = directoryPath + songName
        soundPlayer = playSound(filePath, volume, logger)

    elif command == "volume":
        volume = float(logger.TakeInput("What would you like the volume to be between 0 for mute and 10?"))
        volume = volume/10
        playing = pygame.mixer.get_busy()
        if playing:
            pygame.mixer.Sound.set_volume(soundPlayer, volume)

    elif command == "close":
        close = True

    else:
        logger.ShowOutput("That is not a valid command")

    return soundPlayer, volume, close


def main(directoryPath="Music/", logger=IOLogger(True)):
    soundPlayer = ""
    optionsList = ["Play", "Stop", "Volume", "Close"]
    volume = 1.0
    close = False
    if type(logger) == IOLogger:
        InitialiseLogs()
    musicFiles = getPlaylist(InputDataFile(), directoryPath)
    while True:
        soundPlayer, volume, close = enterCommand(soundPlayer, musicFiles, directoryPath, optionsList, volume, close, logger)
        if close:
            break


if __name__ == '__main__':
    main()
