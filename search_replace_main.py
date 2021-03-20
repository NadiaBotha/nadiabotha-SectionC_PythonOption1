#Import all the methods from search_replace
from search_replace import*

#Request the user to input the main string, the substring and the replacement string.
userString = input("Please enter a string: ")
userSubstring = input("Please enter the substring you wish to find: ")
userStringReplacement = input("Please enter a srring to replace the given substring: ")
#Initialize the counter to 0.
counter = 0

#Get the new string by calling the search_and_replace function with the user inputs as
#function arguments.
display_string = search_and_replace(userString, userSubstring, userStringReplacement, counter)

#Display the new string.
print(display_string)

