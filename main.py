from pprint import pprint
#get number of photos

#number of lines
numLines = int(input())
#dictionary containing all tags and their corresponding photos
tags = {}
#dictionary 
photos = {}

for i in range(numLines):
    #get everything about the photo and put it in a dictionary
    lineContent = input()
    lineContent = lineContent.split(" ")
    photos[i] = [lineContent[0], lineContent[1], lineContent[2:]]
    #add each tag to the dictionary, adding the photo ID if it was already previously added
    for tag in lineContent[2:]:
        if tag in tags:
            tags[tag].append(i)
        else:
            tags[tag] = [i]
