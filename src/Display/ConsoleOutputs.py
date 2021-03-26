optionsList = ["play", "stop", "volume"]

def displayFiles(fileList, logger):
    for entryNumber, entry in enumerate(fileList):
        logger.ShowOutput(str(entryNumber) + ":" + entry)


def displayOptions(logger):
    logger.ShowOutput(str(optionsList))