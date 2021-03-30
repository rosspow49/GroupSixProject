from ..Engine.Commands import Commands

def displayFiles(fileList, logger):
    for entryNumber, entry in enumerate(fileList):
        logger.showOutput(str(entryNumber) + ":" + entry)


def displayOptions(logger):
    for command in Commands:
        logger.showOutput(command.value[0])