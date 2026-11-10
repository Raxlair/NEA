def fileCouter(filePath):
    with open(filePath, "a+") as file:
        file.seek(0)
        if file.read() != "": #reads from the file if there is already a number in the file, if not it will set the counter to 0
            file.seek(0)
            screenshotCount = int(file.read())
        else:
            screenshotCount = 0

        screenshotCount = screenshotCount + 1 
        file.truncate(0) #resets the file and then writes the new number to the file
        file.write(str(screenshotCount))
        return screenshotCount