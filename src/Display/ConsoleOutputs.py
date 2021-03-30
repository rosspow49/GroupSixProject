optionsList = ["play", "stop", "volume", "close"]

def displayFiles(fileList, logger):
    for entryNumber, entry in enumerate(fileList):
        logger.ShowOutput(str(entryNumber) + ":" + entry)


def displayOptions(logger):
    logger.ShowOutput(str(optionsList))