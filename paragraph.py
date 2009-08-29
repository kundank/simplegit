import re

def get_para(filename):
	"""reads a file and tokenizes it to words and returns the words as a list"""
		#a regular expression to split double-enter(2 times \n) boundaries
	regex=re.compile('\n\n\n*')
		
	#open the file for reading
	file = open(filename, "r")
	#read the whole file into the doc object. it will be one long string
	doc = file.read()
	
	#a list comprehension.. uses the regular expression to split doc into words. note that all words are lowecased
	para=[s.lower() for s in regex.split(doc)]
	
	return para
