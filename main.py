#this is a library I wrote for computing levenshtein distance
from levenshtein import * 


# To Calculate the friendship network of a word up to three degrees of separation,
# we simply calculate a levenshtein matrix, and the bottom right number will be the
# levenshtein distance between the two words. If this is 3 or less, than the words
# are in the same network. Oh, and just by the way, this is basically the first program
# I've written from the ground up in python. So if I did a obvious python no-no,
# I apologize.

# PS - In case it isn't obvious, I didn't think this algorithm up on my own. It's a well
# known algorithm I found on wikipedia. The implementation is my own though :)

# ~Aaron Pool

inputFile, wordToMatch = parseCommandLine( sys.argv[:] )

for line in inputFile:
    if isFamily( wordToMatch, line.rstrip() ):
        print( line )

