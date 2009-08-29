import re

def get_sentence(para):
	"""reads a file and tokenizes it to sentences and returns the sentences as a list"""
	
	#a regular expression to split at full-stop i.e.'.' boundaries
	regex=re.compile('[.\n?!]')
	
	f = open('para.txt', 'w') # open for 'w'riting
	f.write(para) # write text to file
	f.close() # close the file

	
	#open the file for reading
	file = open('para.txt', "r")
	
	#read the whole file into the doc object. it will be one long string
	doc = file.read()
	
	#a list comprehension.. uses the regular expression to split doc into words. note that all words are lowecased
	sentence=[s.lower() for s in regex.split(doc)]
	
	return sentence
