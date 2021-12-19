'''
@Author Benjamin Rittenhouse
@File main.py
@Desc program to identify the structure of a sentence
'''

import spacy
from flask import *
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		sentence_inp = request.form.get('user_sentence')
		if sentence_inp != '':
			sentence = request.form['user_sentence']
			pieces = [] # pieces of sentence init
			pieces = parse_sentence(sentence)
			sj = str(pieces[0])
			sj = sj[1:len(sj)-1]

			doj = str(pieces[1])
			doj = doj[1:len(doj)-1]

			v = str(pieces[2])
			v = v[1:len(v)-1]

			poj = str(pieces[3])
			poj = poj[1:len(poj)-1]

			rendered = ""

			allwords = sentence.split(' ')
			for word in allwords:
				if word == sj:
					rendered += "<span class = 'subj'>" + sj + "</span> "
					print("Word: " + word + " SJ")
				elif word == doj:
					rendered += "<span class = 'dobj'>" + doj + "</span> "
					print("Word: " + word + " OJ")
				elif word == v:
					rendered += "<span class = 'verb'>" + v + "</span> "
					print("Word: " + word + " VERB")
				elif word == poj:
					rendered += "<span class = 'pobj'>" + poj + "</span> "
				else:
					rendered += word + " "
					print("Word: " + word + " OTHER")


			ret = rendered


			return render_template('index_updated.html', overlay = ret)
	else:
		return render_template('index.html')

nlp = spacy.load("en_core_web_lg")

# MAIN

	#words = inp.split(' ')
def parse_sentence(s):

	doc=nlp(s)

	subj = [tok for tok in doc if (tok.dep_ == "nsubj") ]
	dobj = [tok for tok in doc if (tok.dep_ == "dobj") ]
	verb = [tok for tok in doc if (tok.dep_ == "ROOT") ]
	pobj = [tok for tok in doc if (tok.dep_ == "pobj") ]

	ret = []
	ret.append(subj)
	ret.append(dobj)
	ret.append(verb)
	ret.append(pobj)

	return ret










