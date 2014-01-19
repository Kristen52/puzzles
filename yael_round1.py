#
# Programming again! Practice interview questions given by Yael.
# 12/5/2012
#
## given a string such as "one two three", would return the same string with the words in reverse order "three two one".


sample_string = 'one two three four five six'

def stringReverse(input):
    """Input a string of words separated by spaces, output the same words in reverse order.
    Time O(n) Space O(n). It cannot be faster than O(n) since strings are not mutable, thus
    each charachter must be copied into the final string. It cannot take less space since
    O(n) space is required for the input variable."""
    
    temp = ""
    final = ""
    i = 0
    while i in range(len(input)):
        if (input[i] != " "):
            temp = temp + input[i]  # reassemble letters in the same word in order 
        else:
            final = temp + " " + final # reassemble words in reverse order 
            temp = "" # reset the temp variable
        i = 1 + i
    return  temp + " " + final
            

print stringReverse(sample_string)

## - to describe an algorithm to determine if a string is a palindrome
sampleString = "racecar"

def palindromeString(input_string):
    """Takes a string, and returns True if it's a palindrome and False if not. O(n) time is minimum
    because you must iterate over at least 1/2 the letters to compare, O(n) space is minimum since
    the initial variable takes n space."""
    
    p = 0
    q = len(input_string) - 1
    palindrome = True

    while p < q and palindrome == True:
        palindrome = (input_string[p] == input_string[q])    # iterate over the letters, checking for any that
        p = p + 1                                            # would disqualify the word from being a palindrome
        q = q - 1

    return palindrome

print palindromeString(sampleString)


## - Given an array of integers in any order and a number 'n', return the number of pairs in the array that add up to n.
intArray = [5, 2, 4, 7, 3, 9, 2]
number = 7
## Return value = 2 (5+2 and 4+3)

def addsToN(intArray, number):
    """This minimizes big O time complexity but not space complexit. Time O(n),
    space depends on the python hash implemented for the set."""

    count = 0
    hashedNumbers = set()
    
    for x in intArray:
        if x in hashedNumbers:
            count += 1
        hashedNumbers.add(number-x)
    return count

print addsToN(intArray, number)



## - Given an m x n array filled with 0s and 1s, if a 0 exists in a cell fill that cell's row and columns with 0s.

def mnArrayToString(mnArray):
    """A pretty way to print out the array"""
    for i in mnArray:
        print i

mInt = 4
nInt = 5

mnarray = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

mnarray[3][3] = 0
mnarray[1][0] = 0

def fillWith0(mnarray):
    """Takes an array of 0 and 1, replaces any rows or columns that contain 0 with all 0's. Assumes the array
    contains at least one element, and that it is a proper MxN array (each row/column has the same number of
    elements). The time complexity is O(nxm). This function occurs in place."""

    print "initial array:"
    mnArrayToString(mnarray)

    m = [] #rows that should be all 0
    n = [] #columns that should be all 0

    for x in range(len(mnarray)):     #identifies all the 0s in the array (time complexity O(nxm))
        for y in range(len(mnarray)):
            if mnarray[x][y] == 0:
                m += [x]
                n += [y]

    for x in m:     #replaces all the rows that should be 0 with 0s (time complexity O(nxm))
        for y in range(len(mnarray)):
            mnarray[x][y] = 0

    for j in n:      #replaces all the columns that should be 0 with 0s (time complexity O(nxm))
        for k in range(len(mnarray[0])):
            mnarray[k][j] = 0
            
    print "final array"

    mnArrayToString(mnarray)


fillWith0(mnarray)
        

## - delete a node from a linked list when all she has a pointer to the node itself

# assumption: bi-directional

class Node:

    def __init__ (self, value, previousNode = None, nextNode = None):
        self.value = value
        self.previousNode = previousNode
        self.nextNode = nextNode

    def __str__ (self):
      return str(self.previousNode == None) + " " + str(self.value) + " " + str(self.nextNode == None)

class LinkedList:
    def __init__ (self, nodeArray):
        self.nodeArray = nodeArray
        self.initialNode = nodeArray[0]
        if len(self.nodeArray) > 1:
            self.nodeArray[0].nextNode = nodeArray[1]
            self.nodeArray[-1].previousNode = nodeArray[-2]
        if len(nodeArray) > 2:
            for i in range(len(nodeArray)-2):
                self.nodeArray[i+1].previousNode = nodeArray[i]
                self.nodeArray[i+1].nextNode = nodeArray[i+2]

    def __str__(self):
        outString = ""

        currentNode = node
        outString += str(currentNode)
        
        while (currentNode.nextNode != None):
            outString += '\n' + str(currentNode.nextNode)
            currentNode = currentNode.nextNode

        currentNode = node

        while (currentNode.previousNode != None):
            outString = str(currentNode.nextNode) + '\n' + outString
            currentNode = currentNode.previousNode
            
        return outString


    #(print by iterating over the list assembled in init)

first = Node(1)
second = Node(2)
third = Node(3)
     
tester = LinkedList([first, second, third])

def removeNode(node):
    if node.previousNode != None:
        node.previousNode.nextNode = node.nextNode
    else:
        if node.nextNode != None:
            node.nextNode.previousNode = None
            print "2"
    if node.nextNode != None:
        node.nextNode.previousNode = node.previousNode
        print "3"
    else:
        if node.previousNode != None:
            node.previousNode.nextNode = None
    if node.nextNode != None:
        print str(tester, node.nextNode)
    elif node.previousNode != None:
        print str(tester, node.previousNode)
    else:
        print "you removed the final node"

removeNode(third)


## - transform a general tree into a binary tree

## - design a data structure to hold information about the contents of a document and be able to tell whether a word appears in a document and at what places
## - build a binary tree given two strings that represent the infix and prefix walk through the tree
## You have an array with duplicates. remove the duplicates.  What is the complexity (space and time)

