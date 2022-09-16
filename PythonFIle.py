

bookText = open('myText1.txt', 'r')
bookLines2 = []
bookLines = bookText.readlines()
currentWord = ''
for x in range(0, len(bookLines)):
    line = bookLines[x]
    line += "*"
    for y in range(len(line)):
        if line[y] == ' ':
            currentWord = currentWord.lower()
            bookLines2 += [currentWord]
            currentWord = ''
        elif line[y] == "*":
            currentWord = currentWord.lower()
            bookLines2 += [currentWord]
            currentWord = ''
        elif line[y] == "-":
            currentWord = currentWord.lower()
            bookLines2 += [currentWord]
            currentWord = ''
        elif 65 <= ord(line[y]) <= 90 or 97 <= ord(line[y]) <= 122 :
            currentWord += line[y]
bookText.close()

allWords = open('allwords.txt', 'w')
for words in range(0, len(bookLines2)):
    if len(bookLines2[words]) > 0:
        allWords.write(bookLines2[words])
        allWords.write('\n')
allWords.close()


wordDict = {}
for x in range(len(bookLines2)):
    word = bookLines2[x]
    if word not in wordDict:
        wordDict[word] = 1
    else:
        value = wordDict.get(word)
        value += 1
        wordDict[word] = value

uniqueList = []
for x in wordDict:
    if wordDict[x] == 1:
        uniqueList += [x]

uniqueWords = open('uniquewords.txt', 'w')
for words in range(0, len(uniqueList)):
    uniqueWords.write(uniqueList[words])
    uniqueWords.write('\n')
uniqueWords.close()


frequencyList = []       
for x in wordDict:
    value = wordDict[x]
    frequencyList += [value]
frequencySet = set(frequencyList)
frequencyList = list(frequencySet)
frequencyList.sort()
print(frequencyList)
count = 0
newList = []
for x in frequencyList:
    for y in wordDict:
        if wordDict[y] == x:
            count += 1
    newList += [[x,count]]
    count = 0

wordFrequency = open('wordfrequency.txt', 'w')
for counts in newList:
    wordFrequency.write(str(counts[0]))
    wordFrequency.write(": ")
    wordFrequency.write(str(counts[1]))
    wordFrequency.write('\n')
wordFrequency.close()
    
            
        




