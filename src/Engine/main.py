import pygame

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Engine.trackControls import *
from src.Display.ConsoleOutputs import *
from src.Display.IOLogger import IOLogger
from src.Engine.volumeControls import *

pygame.mixer.init()


def getPlaylist(inputType, directoryPath, logger):
    try:
        playlist = inputType.getRawData(directoryPath)
    except FileNotFoundError:
        logger.ShowOutput("Error. Directory was not found. Switching to stub.")
        inputSource = InputDataStub()
        playlist = inputSource.getRawData(directoryPath)
    return playlist


def getFileToPlay(fileList, logger=IOLogger(True)):
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


def enterCommand(soundPlayer, songList, directoryPath, volume, close, logger):
    displayOptions(logger)
    command = logger.TakeInput("Please type one of the options").lower()

    if command == "stop":
        stopSound(soundPlayer, logger)

    elif command == "play":
        songName = getFileToPlay(songList, logger)
        filePath = directoryPath + songName
        soundPlayer = playSound(filePath, volume, logger)

    elif command == "volume":
        volume = getVolume(logger)
        setVolume(volume, soundPlayer)

    elif command == "close":
        close = True

    else:
        logger.ShowOutput("That is not a valid command")

    return soundPlayer, volume, close


def main(directoryPath="Music/", logger=IOLogger(True)):
    soundPlayer = ""
    volume = 1.0
    close = False
    if type(logger) == IOLogger:
        InitialiseLogs()
    musicFiles = getPlaylist(InputDataFile(), directoryPath, logger)
    while True:
        soundPlayer, volume, close = enterCommand(soundPlayer, musicFiles, directoryPath, volume, close, logger)
        if close:
            break


if __name__ == '__main__':
    main()
