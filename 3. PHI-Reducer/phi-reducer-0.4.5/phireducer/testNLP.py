import spacy 

nlp = spacy.load('en')
test = open('testcase.xml').read()

doc = nlp(test)

print (doc)