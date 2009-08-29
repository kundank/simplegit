import re

def get_words(sentence):
                #a regular expression to split double-enter(2 times \n) boundaries
                regex=re.compile('\W*')
                        
                #open the file for writing
                f= open('words.txt', "w")
                f.write(sentence)
                f.close

                file=open('words.txt',"r")        
                doc = file.read()
                
                #a list comprehension.. uses the regular expression to split doc into words. note that all words are lowecased
                para=[s.lower() for s in regex.split(doc)]
                
                return para
