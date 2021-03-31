def getFileToPlay(fileList, logger):
    validFileIdentifier = False
    while not validFileIdentifier:
        fileIdentifier = logger.takeInput("Please enter the track number:")
        try:
            fileIdentifier = int(fileIdentifier)
            if fileIdentifier not in range(len(fileList)):
                raise ValueError
            fileName = fileList[fileIdentifier]
            validFileIdentifier = True
        except:
            logger.showOutput("That is an invalid track number")
    return fileName