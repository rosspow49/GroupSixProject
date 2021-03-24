

def displayFiles(fileList, logger):
    for entryNumber, entry in enumerate(fileList):
        logger.ShowOutput(str(entryNumber) + ":" + entry)