fileHandle = open("corpusKCC150_Korean_sentences_UTF8.txt", "r", encoding="utf-8")
corpusContents = fileHandle.read()
blockDict = {}
blockDictLog = {}
validCount = 0      # counts ALL the syllable blocks in the corpus (it ends up being 458,345,295)
# maximum value is 14.882.952, the value for *da*
# 11172 possible blocks
    # average centile is 111.72
percentageOfMaxDict = {}
percentageOfMaxDict255 = {}
import math

# creating the dictionary keys. This dictionary is of the format {가: 9820,각: 1210, etc.}

#for i in range(44032,55204):       # dictionary keys are numbers, e.g. 49281
#    blockDict[i] = 0

for i in range(44032,55204):        # dictionary keys are hangul, e.g. 상
    blockDict[chr(i)] = 0
# Now we have a dictionary with all the Hangul syllable blocks as keys, but each just has a value of 0.

# inserting the dictionary values: the number of instances of the sylblock:

for j in corpusContents:
    #print(corpusContents[j])
    if ord(j) >= 44032 and ord(j) <= 55203:
        #print(ord(corpusContents[j]))
        #blockDict[ord(corpusContents[j])] += 1
        blockDict[j] += 1
        #validCount += 1

# making new dictionary(ies) for calculations. New dictionary is of the format {"char44032": 2.519, "char44033": 1.185, etc.}

maxLog = math.log(14882953)

for i in range(44032,55204):
    keyName = "char" + str(i)
    #percentageOfMaxDict[keyName] = blockDict[chr(i)] / 14882952
    #percentageOfMaxDict255[keyName] = 255*blockDict[chr(i)] / 14882952
    blockDictLog[keyName] = math.log(blockDict[chr(i)]+1) / maxLog


#print(percentageOfMaxDict)
#print(percentageOfMaxDict255)
#print(blockDictLog)






# On November 11, 2020, I wanted to sort Hangul blocks by frequency, so I did the following:
dictionaryForRanking = {}
blocksInDecreasingFrequency = ''
keysForRanking = []
valuesForRanking = []


for k in range(44032,55204):        # dictionary keys are hangul, e.g. 상
    dictionaryForRanking[chr(k)] = 0

for m in corpusContents:
    #print(corpusContents[j])
    if ord(m) >= 44032 and ord(m) <= 55203:
        #print(ord(corpusContents[j]))
        #blockDict[ord(corpusContents[j])] += 1
        dictionaryForRanking[m] += 1

for x in dictionaryForRanking.values():
    valuesForRanking.append(x)
for y in dictionaryForRanking.keys():
    keysForRanking.append(y)

while len(valuesForRanking) > 0:
    maxValue = max(valuesForRanking)
    for n in keysForRanking:
        if dictionaryForRanking[n] == maxValue:
            blocksInDecreasingFrequency = blocksInDecreasingFrequency + n
            keysForRanking.remove(n)
            break
    valuesForRanking.remove(maxValue)

print(blocksInDecreasingFrequency)












fileHandle.close()
