# initial commit

# installed es-core-news-lg from spaCy docs

import spacy 

nlpModel = spacy.load('es_core_web_lg') # load model

def conjugate(verb, tense):
	# takes spanish infinitive verb as input
	# also takes desired tense (present, preterite, future, etc.)
	# returns the conjugated verb
	doc = nlp(verb)	# parse verb using spacy
	if doc[0].pos = "VERB":
		return doc[0].conjugate(tense=tense)
	else:
		return "Not a verb" # handles non-verb input 

user_verbInput = input("Enter a Spanish verb: ")

