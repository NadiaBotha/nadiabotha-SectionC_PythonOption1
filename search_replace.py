#Function that creates a new string, by looking for a substring in a main string and replacing it
#with a new string defined by the user.
def search_and_replace(userString, substringToFind, replacementString, counter):
    #Exception handling, which prevents the program from crashing if the user enters a substring that is not in the main
    #string.
    #Try block is executed if the substring is in the main string.
    try:
        #Define the startingIndex and endIndex in the main string, to look for the substring.
        startingIndex = counter
        endIndex = startingIndex + len(substringToFind)
        #Increment the counter, so when the function is executed again the startIndex and endIndex, move
        #to the right with 1 character.
        counter=counter+1

        #Slice the characters that are between the startingIndex and endIndex in the main string. This
        #is the string that we will use to compare with the substring.
        currentString = userString[startingIndex:endIndex]
        display_string = ""

        #If the sliced string (between the startingIndex and endIndex) is equal to the substring defined, the
        #substring is found and we have to replace it.
        if(currentString == substringToFind):
            #If the substring is found at the beginning of the main string, then final string with the replacement will be
            #the replacemenetString + the rest of the main string.
            if(startingIndex == 0):
                display_string = replacementString + userString[endIndex:len(userString)]

            #If the substring is found in the middle of the main string, then the final string is the start of the main string +
            #the replacement string + the end of the main string.
            elif(startingIndex > 0 and endIndex < len(userString)):
                display_string = userString[0:startingIndex] + replacementString + userString[endIndex:len(userString)]

            #If the substring is found at the end of the main string, then the final string is the beginning of the main string +
            #the replacementString.
            elif(endIndex == len(userString)):
                display_string = userString[0:startingIndex] + replacementString

            else:
                display_string = "Error: The substring entered is not found in the main string"

        #If the substring is not found(the sliced string is not equal to the substring), then the function is called recursively
        #and the startingIndex and endIndex moves one to the right in the main string.
        else:
            display_string = search_and_replace(userString, substringToFind, replacementString, counter)   

    #The error message is displayed if the substring is not in the main string.
    except:
        display_string = "ERROR: The substring entered is not found."
        
    #Return the new string, which has the substring replaced by the user defined string.
    return display_string
