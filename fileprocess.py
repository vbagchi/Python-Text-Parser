'''
Preliminaries:
1) Importing packages 
2) Local variables that are used along with their corresponding file paths 

textfile - replace with local location of the original text file where the important words are to be extracted from 

'''

import io 
from nltk import corpus, FreqDist, word_tokenize
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import csv

textfile = "example.txt"
'''
Now, if such a file does not already exist, we create a new file called "filteredtext.txt" which 
contains the exact text of the original file without the stop words. This piece of code is only needed to be run once to 
find out and save these important words for a certain text file. 
To be careful: If "filteredtext.txt" already exists from a previous run, 
may only append words to all over again, giving an errenous count of words. 
'''
# word_tokenize accepts a string as an input 

stop_words = set(stopwords.words('english')) 
file1 = open(textfile) 
  
# This reads in file content as a stream  
line = file1.read()
words = line.split() 

#this stores the words without the stop words in a new text file
for r in words: 
    if not r in stop_words: 
        appendFile = open('filteredtext.txt','a+') 
        appendFile.write(" "+r) 
        appendFile.close()
        
file1.close()

'''
This piece of code uses the word_tokenize function to split the file into words or "tokens" and has it stored in a set called impwords.

**Replace filtext with location where "filteredtext.txt" from above is stored.
'''
#This is the local path of the above generated "filteredtext.txt" file 
filtext = "/Users/filteredtext.txt"

#opens and reads in file 
file2 = open(filtext) 
text = file2.read()
words = word_tokenize(text)

ordered_tokens = set()
impwords = []

#makes sure that there aren't any repeated tokens 
for word in words:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        impwords.append(word)
     

#prints the list of important words -- only for visual confirmation - can remove this section  
for k in impwords:
    print(k)

#closes the file 
file2.close()
