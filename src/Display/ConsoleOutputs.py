from ..Engine.Commands import Commands

def displayFiles(fileList, logger):
    for entryNumber, entry in enumerate(fileList):
        logger.ShowOutput(str(entryNumber) + ":" + entry)


def displayOptions(logger):
    for command in Commands:
        logger.ShowOutput(command.value[0])