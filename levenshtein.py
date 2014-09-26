import sys

# returns the levenshtein distance

def getDistance( word1, word2 ):
    matrix = []
    w1Length = len( word1 )
    w2Length = len( word2 )

    # initialize string match matrix
    for index in range( w1Length + 1 ):
        matrix.append( [index] ) 
    for index in range( 1, w2Length + 1 ):
        matrix[0].append( index )

    # fill out string match matrix
    for i in range( 1, w1Length + 1 ):
        for j in range( 1, w2Length + 1 ):
            if word1[i-1] == word2[j-1]:
                matrix[i].append( matrix[i-1][j-1] )
            else:
                matrix[i].append( min( matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1] ) + 1 )

    # the shortest levenshtein difference will be in the lower right corner of the matrix
    distance = matrix[ w1Length ][ w2Length ]
    return distance

# this function prints a matrix in standard form, rather than as a list
# it only serves debugging purposes

def printMatrix( matrix, rows, cols ):
    # utility function for debugging, print out levenshtein matrix as a matrix
    for i in range( rows ):
        for j in range( cols ):
            print( matrix[i][j], end="" )
        print ()

# this function checks if two words are in the same network, or "family"

def isFamily( word1, word2 ):
    # if the length of the words differs by more then three, they can't be family
    if abs( len( word1 ) - len( word2) ) < 4:
        # otherwise, run the matrix test
        if getDistance( word1, word2 ) < 4:
             return True
             
    # if it hasn't returned in the if statement, return false
    return False

# this function parses command line arguments and notifies the user
# if they're attempting to use inappropriate arguments

def parseCommandLine( args ):
    #if there's not more than two and less than four agruments, bail out
    if len( args ) < 2 or len( args ) > 3:
        print( "Usage -- levenshtein.py [word] [word list file, default = randomlist.txt]" )
        sys.exit()
    else: 
        if len( args ) == 3:
            fin = open( args[2] )
        else:
            fin = open( 'randomlist.txt' )
        word = args[1]
        return fin, word

