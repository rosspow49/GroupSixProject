from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Display.ConsoleOutputs import *
from src.Display.ConsoleInputs import *
from src.Display.IOLogger import IOLogger
from src.Engine.Commands import Commands
from src.Engine.TrackControls import *
from src.Engine.VolumeControls import *

pygame.mixer.init()


def getPlaylist(inputType, directoryPath, logger):
    try:
        playlist = inputType.getRawData(directoryPath)
    except FileNotFoundError:
        logger.showOutput("Error. Directory was not found. Switching to stub.")
        inputSource = InputDataStub()
        playlist = inputSource.getRawData(directoryPath)
    return playlist

def initialiseLogs():
    with open("Logs/InputLog.txt", "w") as inputs:
        inputs.write("")
    with open("Logs/OutputLog.txt", "w") as outputs:
        outputs.write("")


def enterCommand(soundPlayer, songList, directoryPath, volume, close, logger):
    displayCommands(logger)
    command = logger.takeInput("Please type one of the options").lower()

    # stop
    if command in Commands.STOP.value:
        stopSound(soundPlayer, logger)

    # play
    elif command in Commands.PLAY.value:
        displayFiles(songList, logger)
        songName = getFileToPlay(songList, logger)
        filePath = directoryPath + songName
        soundPlayer = playSound(filePath, volume, logger)

    # volume control
    elif command in Commands.VOLUME.value:
        volume = getVolume(logger)
        setVolume(volume, soundPlayer)

    # pause/play
    elif command in Commands.PAUSE.value:
        playPause(logger)

    # close program
    elif command in Commands.CLOSE.value:
        close = True

    else:
        logger.showOutput("That is not a valid command")

    return soundPlayer, volume, close


def main(directoryPath="Music/", logger=IOLogger(True)):
    soundPlayer = ""
    volume = 1.0
    close = False
    if type(logger) == IOLogger:
        initialiseLogs()
    musicFiles = getPlaylist(InputDataFile(), directoryPath, logger)
    while True:
        soundPlayer, volume, close = enterCommand(soundPlayer, musicFiles, directoryPath, volume, close, logger)
        if close:
            break


if __name__ == '__main__':
    main()
