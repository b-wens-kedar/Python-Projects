#Press the green "Run" button at the bottom to start the translator 

#initializing functions
def fileCheck(fileName):
    try:
        fileObj = open(fileName) #will try to open the file specified
        return 0
    except IOError: #will handle the exception
        print("Could not locate the file " + fileName)
        return 1

def dictionaryList(fileName):

    #declare variables
    allAbreviations =[]
    allTranslations =[]

    #open file with translations
    fileOpen = open(fileName)

    for line in iter(fileOpen):
        wordsInTheLine = line.split()
        
        #all abreviations in a list
        allAbreviations.append(wordsInTheLine[0])
        
        #all translations in a list
        translation =''
        tNumberOfWords = len(wordsInTheLine)
        for x in range(2,tNumberOfWords):
            translation = translation+wordsInTheLine[x]+' '
        allTranslations.append(translation)
    
    #returning the two list(allAbreviations,allTranslations)
    return(allAbreviations,allTranslations)

def compare(messageWords,allAbreviations,allTranslations):

    #initialize variable
    finalMessage =''

    #a loop that compares each word from the user
    #  to the list of abreviations
    for wordPosition in range(0,len(messageWords)):
        currentWord = messageWords[wordPosition]  
        try:
            #looks for a match using the index function 
            matchingPosition = allAbreviations.index(currentWord.upper())
            
            #if found the matching  line in the translations
            # list is added to the final message
            finalMessage = "The full form of '"+currentWord+"' is "+allTranslations[matchingPosition].title()+". 🤗"
        except:
            #if no match is found
            #the original word is added to the final message
            finalMessage = "Sorry,😔 I don't know the meaning of '"+currentWord+"' \nDo you know the meaning of the abbreviation😀? You can update the abbreviation list in the 'Translations.txt' file displayed above."

    return(finalMessage)

#initializing and declaring variables
txtMessage=''
messageWords=''
translationsFileName='Translations.txt'

#getting input
txtMessage=input("please enter the message or \
abbreviation you would like to translate.(no punctuation please, examples: 'omg', 'lol', 'asap'):\n")

#getting every word in the provided message
#using the message.split() function
messageWords = txtMessage.split()

fileFound = fileCheck(translationsFileName)

if fileFound==0:
    allAbreviations,allTranslations=dictionaryList(translationsFileName)

    translatedMessage=compare(messageWords,allAbreviations,allTranslations)

    print(translatedMessage)
else:
     print("Could not translate message, file containing translation terms could not be located.")
