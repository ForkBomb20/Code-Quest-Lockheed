import sys
import math
import string

# A dictionary that stores all the phonetic words for the alphabet
phonetic =  {'A':'Alpha','N':'November','B':'Bravo','O':'Oscar','C':'Charlie',
'P':'Papa','D':'Delta','Q':'Quebec','E':'Echo','R':'Romeo','F':'Foxtrot',
'S':'Sierra','G':'Golf','T':'Tango','H':'Hotel','U':'Uniform','I':'India',
'V':'Victor','J':'Juliet','W':'Whiskey','K':'Kilo','X':'Xray','L':'Lima','Y':'Yankee','M':'Mike','Z':'Zulu'}

# Get the number of sets of words
cases = int(sys.stdin.readline().rstrip())

# Iterate for each set of words
for caseNum in range(cases):

    # Get the number of words in the current set
    word_cases = int(sys.stdin.readline().rstrip())

    # Repeat for each word in the current set
    for wordNum in range(word_cases):
        
        # Get teh current word in the current set and creat an empty list to store the new phonetic form
        word = sys.stdin.readline().rstrip()
        new_form = []
        
        # Iterate for each character in the current word
        for i in range(len(word)):
            
            # Edge case in case of a space
            if word[i] == ' ':
                new_form.append(word[i])

            # Capitalize the current character and get the phonetic version from the dictionary then append it to the new form list
            else:
                new_form.append(phonetic[str(word[i].upper())])

                # Another edge case for dealing with spaces
                if i != len(word):
                    try:
                        # Add dashes in between charcters but not spaces
                        if word[i+1] != ' ':
                            new_form.append('-')

                    except IndexError:
                        pass

        # Print out the word (or words) joined together from the list
        print(''.join(new_form))
                