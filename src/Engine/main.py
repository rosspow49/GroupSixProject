import pygame

from src.Data.InputDataFile import InputDataFile

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

def getPlaylist(inputType, directoryPath):
    playlist = inputType.getRawData(directoryPath)
    return playlist

def displayFiles(fileList, logger):
    for entryNumber, entry in enumerate(fileList):
        logger.ShowOutput(str(entryNumber) + ":" + entry)

def GetFileToPlay(fileList, logger):
    displayFiles(fileList, logger)

    fileIdentifier = TakeInput("Please enter the file name or corresponding number")
    while int(fileIdentifier) not in range(len(fileList)):
        logger.ShowOutput("This is an incorrect identifier")
        fileIdentifier = TakeInput("Please enter the corresponding number of the song you want to play")

    if int(fileIdentifier) in range(len(fileList)):
        fileIdentifier = fileList[int(fileIdentifier)]

    return fileIdentifier

def InitialiseLogs():
    with open("Logs/InputLog.txt", "w") as inputs:
        inputs.write("")
    with open("Logs/OutputLog.txt", "w") as outputs:
        outputs.write("")

def EnterCommand(soundPlayer, songList, directoryPath, logger = IOLogger):
    command = logger.TakeInput("Please enter a command")

    if command == "stop":
        if pygame.mixer.get_busy():
            soundPlayer.stop()
        else:
            logger.ShowOutput("There is no song playing at the moment")

    elif command == "play":

        songName = GetFileToPlay(songList, logger)
        soundPlayer = PlaySound(songName, soundPlayer, directoryPath, logger)

    else:
        logger.ShowOutput("That is not a valid command")

    return soundPlayer

def main():
    soundPlayer = ""
    directoryPath = "Music"
    InitialiseLogs()
    musicFiles = getPlaylist(InputDataFile(), directoryPath)
    while True:
        soundPlayer = EnterCommand(soundPlayer, musicFiles, directoryPath)


if __name__ == '__main__':
    main()
