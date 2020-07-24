# What does this file even do? Looks like it writes to hangulOrganized.txt.

fileHandle = open("..\KCC150_Korean_sentences_UTF8.txt", "r", encoding="utf-8")
corpusContents = fileHandle.read()
blockDict = {}
dictBlocksAtLeast1 = {}
dictPreviousBlocks = {}
dictNextBlocks = {}
dictPairs = {}
validCount = 0      # counts ALL the syllable blocks in the corpus (it ends up being 458,345,295)
# maximum value is 14.882.952, the value for *da*
# 11172 possible blocks
percentageOfMaxDict = {}
import math
fileToWriteHandle = open("hangulOrganized.txt", "w", encoding="utf-8")

# creating the dictionary keys. All keys have a zero value--{가: 0,각: 0, etc.}

#for i in range(44032,55204):       # dictionary keys are numbers, e.g. 49281
#    blockDict[i] = 0

#for i in range(44032,55204):        # dictionary keys are hangul, e.g. 상
#    blockDict[chr(i)] = 0

# counting and inserting the dictionary values: the number of instances of the sylblock. This dictionary is of the format {가: 9820,각: 1210, etc.}

#for j in corpusContents:
#    if ord(j) >= 44032 and ord(j) <= 55203:
#        blockDict[j] += 1

# making new dictionaries. "dictBlocksAtLeast1" is the same as blockDict, but it only contains blocks with at least one instance. "dictPreviousBlocks" and "dictNextBlocks" are only being set up here; for now, they're getting keys that are only those blocks with at least one instance, each with a value of 0...so they look like: {가: 0,각: 0, etc.}

#for i in range(44032,55204):
#    if blockDict[chr(i)] > 0:
#        dictBlocksAtLeast1[chr(i)] = blockDict[chr(i)]
#        dictPreviousBlocks[chr(i)] = 0
#        dictNextBlocks[chr(i)] = 0

corpusContentsIndex = 0
for j in corpusContents:    # each 'j' is an actual character of the corpus
    if ord(j) >= 44032 and ord(j) <= 55203 and corpusContentsIndex > 0:     # if j is Hangul, and it's not the first character...
        if ord(corpusContents[corpusContentsIndex-1]) >= 44032 and ord(corpusContents[corpusContentsIndex-1]) <= 55203:     # if the previous character is Hangul...
            dictPairs[corpusContents[corpusContentsIndex-1]+j] = dictPairs.setdefault(corpusContents[corpusContentsIndex-1]+j, 0) + 1
    corpusContentsIndex += 1

for k in dictPairs.keys():
    try:
        fileToWriteHandle.write(k + ": " + str(dictPairs[k]) + "\n")
    except:
        print("Couldn't write this key for some reason", k)

#print(dictPairs)
        

#maxLog = math.log(14882953)

#for i in range(44032,55204):
    #keyName = "char" + str(i)
    #percentageOfMaxDict[keyName] = blockDict[chr(i)] / 14882952
    #percentageOfMaxDict255[keyName] = 255*blockDict[chr(i)] / 14882952
    #blockDictLog[keyName] = math.log(blockDict[chr(i)]+1) / maxLog
    

#print(blockDictLog)




fileHandle.close()