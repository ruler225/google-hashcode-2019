from pprint import pprint
#get number of photos


#number of lines
numLines = int(input())
#dictionary containing all tags and their corresponding photos
tags = {}
#dictionary 
photos = {}

used = []

horizontal = []
vertical = []

#def tagsInCommon(photoID, tag,):

    


for i in range(numLines):
    #get everything about the photo and put it in a dictionary
    lineContent = input()
    lineContent = lineContent.split(" ")
    photos[i] = [lineContent[0], lineContent[1], lineContent[2:]]
    if lineContent[0] == 'H':
        horizontal.append(i)
    else:
        vertical.append(i)
    #add each tag to the dictionary, adding the photo ID if it was already previously added
    for tag in lineContent[2:]:
        if tag in tags:
            tags[tag].append(i)
        else:
            tags[tag] = [i]


numSlides = len(horizontal) + len(vertical)//2

if len(vertical) % 2 == 1:
    numSlides += 1
print(numSlides)
pendingVertical = False

for tag in tags:
    for photo in tags[tag]:
        if photo not in used:
            if photos[photo][0] == 'H':
                print(photo)
                used.append(photo)
            elif pendingVertical and photo not in used:
                print(photo, used[-1])
                used.append(photo)
                pendingVertical = False
            else:
                used.append(photo)
                pendingVertical = True



