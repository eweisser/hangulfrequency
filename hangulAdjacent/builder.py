# This program was designed to generate strings in Hangul with various characteristics.

import re
import random

fileHandle = open("hangulOrganized.txt", "r", encoding="utf-8")
pairsString = fileHandle.read()         # a single large string holding the contents of the file
pairsList = pairsString.splitlines()    # a list, with each element e.g. '강혁: 2839'
pairsDictio = {}        # a dictionary, with each key-value pair e.g. '강혁': 2839
sortedKeys = []         # a list of the previous dictionary's keys, sorted 
sortedValues = []       # a list of the previous dictionary's values, sorted 

matchingConnectorKeys = []
matchingConnectorValues = []

for each in pairsList:
    hangulCombo = each[0:2]
    instanceCount = int(re.search("[0-9]+",each).group())
    pairsDictio[hangulCombo] = instanceCount

#put the keys in order:
sortedKeys = sorted(pairsDictio,key=pairsDictio.get,reverse=False) # false for ascending, true for descending
sortedValues = sorted(pairsDictio.values()) #low to high

print(sortedKeys)

# now to generate some wackiness:
firstChar = random.choices(sortedKeys, weights = sortedValues, k = 1)[0]
print(firstChar)
print("********")
resultString = firstChar[0]
currentCombo = firstChar
for block in range(50):
    matchingConnectorKeys.clear()
    matchingConnectorValues.clear()
    for x in sortedKeys:                # go through every two-block combo possible...
        if currentCombo[1] == x[0]:      # if the latest character's second block matches the combo's first block...
            matchingConnectorKeys.append(x)     # add the combo to this list
            matchingConnectorValues.append(pairsDictio[x])      # add its count to this list
    currentCombo = random.choices(matchingConnectorKeys, weights = matchingConnectorValues, k = 1)[0]
    resultString = resultString + currentCombo[0]
print(resultString)
    







fileHandle.close()