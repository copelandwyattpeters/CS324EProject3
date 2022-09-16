def main():
	print("Begin")

	# load file into program
	textFile = open("prideandprejudice.txt", encoding = 'utf-8')
	
	# initialize several lists to be populated
	masterList = []
	uniqueList = []
	frequencyList = []
	frequencyCountList = []
	frequencyFrequencyList = []

	# open the three files we'll be writing to, if they do not already exist
	# they will be generated
	allFile = open("allwords.txt", "w")
	uniqueFile = open("uniquewords.txt", "w")
	freqencyFile = open("wordfrequency.txt", "w")

	# begin parsing the text line by line
	for line in textFile:
		currentLine = line.rstrip("\n")
		
		# if it's an empty line, skip it
		if (currentLine == ""):
			continue
		
		# replacement of common punctuation markers
		currentLine = currentLine.replace(",", "")
		currentLine = currentLine.replace(".", "")
		currentLine = currentLine.replace("!", "")
		currentLine = currentLine.replace("?", "")
		currentLine = currentLine.replace("'", "")
		currentLine = currentLine.replace('"', "")
		currentLine = currentLine.replace("_", "")
		currentLine = currentLine.replace("-", " ")
		currentLine = currentLine.replace(";", "")
		currentLine = currentLine.replace(":", "")
		currentLine = currentLine.replace("(", "")
		currentLine = currentLine.replace(")", "")
		currentLine = currentLine.replace("&", "")
		
		# replacement of somewhat unique punctuation I found in pride & prejudice
		# if needed this is where one would add additional unique punctuation
		# if you were doing a different book and the code didn't run properly because
		# some other, different marker I didn't come across appeared
		currentLine = currentLine.replace("“", "")
		currentLine = currentLine.replace("”", "")
		currentLine = currentLine.replace("’", "")
		currentLine = currentLine.replace("‘", "")
		currentLine = currentLine.replace("—", " ")
		
		# replace numerical numbers 0-9
		# I considered replacing with a number with its word instead
		# e.g. replace 1 with "one"
		# this would obviously affect the word frequency, I opted not to
		currentLine = currentLine.replace("1", "")
		currentLine = currentLine.replace("2", "")
		currentLine = currentLine.replace("3", "")
		currentLine = currentLine.replace("4", "")
		currentLine = currentLine.replace("5", "")
		currentLine = currentLine.replace("6", "")
		currentLine = currentLine.replace("7", "")
		currentLine = currentLine.replace("8", "")
		currentLine = currentLine.replace("9", "")
		currentLine = currentLine.replace("0", "")
		
		# convert all characters to lower case for ease of string matching later
		currentLine = currentLine.lower()
		
		# in conjunction with the if statement below this, a white space character, " "
		# will trigger .isalpha(), so delete character here
		#currentLine = currentLine.replace(" ", "")
		
		# this is a troubleshooting piece of code
		# if the code doesn't run due to some unknown character I haven't accounted for
		# run this and it will find that character so you can add it to the above character replacement lists
		#if (not currentLine.isalpha()):
		#	print(currentLine)
		#	print("Found one.")
		#	exit()
		
		#print(currentLine)
		
		# use python's build in split function to split based on location of spaces
		wordList = currentLine.split(" ")
		
		# populate the master list going line by line with one notable exception at this point
		# if there are consecutive white spaces python will generate extra empty entries ('')
		# the additional if statement takes care of that
		for i in range (len(wordList)):
			if (wordList[i] != ''):
				masterList.append(wordList[i])
	
	# output the populated master list to the allwords.txt file
	for i in range (len(masterList)):
		allFile.write(masterList[i] + "\n")
	
	# populate the unique list by checking if a current entry exists, and if not, adding it
	# note: this is an ineffecient way of doing this, I would imagine there are better ways
	for i in range (len(masterList)):
		if (masterList[i] not in uniqueList):
			uniqueList.append(masterList[i])
	
	# output the populated unique list to the uniquewords.txt file
	for i in range (len(uniqueList)):
		uniqueFile.write(uniqueList[i] + "\n")
	
	# count the number of any given word's occurance by cross referencing the unique list to the master list
	# for every unique word there is a corresponding append to frequency list to note how many times it occurs
	for i in range (len(uniqueList)):
		uniqueCount = masterList.count(uniqueList[i])
		frequencyList.append(uniqueCount)
	
	# this is the best point to sort the occurance list for output later
	frequencyList.sort()
	
	# similar to creating unique list from master list, count the unique count numbers
	for i in range (len(frequencyList)):
		if (frequencyList[i] not in frequencyCountList):
			frequencyCountList.append(frequencyList[i])
	
	# count the number of times a given number of occurances, occurs. A count of a count if you will
	for i in range (len(frequencyCountList)):
		frequencyCount = frequencyList.count(frequencyCountList[i])
		frequencyFrequencyList.append(frequencyCount)
	
	# having earlier sorted the frequency list everything should already be in corresponding order
	# and have an identical number of list entries to pair update
	# output the populated frequency count list and frequency frequency list to the wordfrequency.txt file
	for i in range (len(frequencyCountList)):
		freqencyFile.write(str(frequencyCountList[i]) + ": " + str(frequencyFrequencyList[i]) + "\n")
	
main()