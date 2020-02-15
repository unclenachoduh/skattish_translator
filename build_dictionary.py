from random import randrange
from nltk.tokenize import word_tokenize
import re, json

lex = open("lexicon.txt").read().split("\n")

dictionary = {"skat": "skat", "skatman": "skat man"}

skat_dictionary = {"skat": "skat"}

english = open("english_words_5000.txt").read().lower().split("\n")

tom = open("tom_delonge.txt").read().lower()

tom = re.sub("…", " ", tom)
tom = re.sub("-", " ", tom)
tom = re.sub("\.", " ", tom)
tom = re.sub("\s+", " ", tom)

tom = word_tokenize(tom)


english_words = []


for w in english:
	english_words.append(w)


i = 0

for word in english_words:

	if word not in dictionary:

		l = int(len(word) / 2)

		value = 0

		if l < 2:
			value = randrange(0, 29)
		elif l < 3:
			value = randrange(29, 841)
		elif l < 4:
			value = randrange(841, 23577)
		else:
			value = randrange(23577, len(lex))

		if lex[value] not in skat_dictionary:
			dictionary[word] = lex[value]
			skat_dictionary[lex[value]] = word
		else:
			while lex[value] in skat_dictionary:
				value += 1
			dictionary[word] = lex[value]
			skat_dictionary[lex[value]] = word

for word in tom:

	if word not in dictionary:

		if re.search('[a-zA-Z]', word) and not re.search('[0-9]', word) :

			l = int(len(word) / 2)

			value = 0

			if l < 2:
				value = randrange(0, 29)
			elif l < 3:
				value = randrange(29, 841)
			elif l < 4:
				value = randrange(841, 23577)
			else:
				value = randrange(23577, len(lex))

			if lex[value] not in skat_dictionary:
				dictionary[word] = lex[value]
				skat_dictionary[lex[value]] = word
			else:
				while lex[value] in skat_dictionary:
					value += 1
				dictionary[word] = lex[value]
				skat_dictionary[lex[value]] = word

j = json.dumps(dictionary)
f = open("dictionary.json","w")
f.write(j)
f.close()

j = json.dumps(skat_dictionary)
f = open("skat_dictionary.json","w")
f.write(j)
f.close()



# ##### Test that dictionary works #####
# my_string = "this is a sample string"

# translated_words = []

# for w in my_string.split():
# 	translated_words.append(dictionary[w])

# print(" ".join(translated_words))

# translated_words = []

# for w in my_string.split():
# 	translated_words.append(dictionary[w])

# print(" ".join(translated_words))

# my_string = "this is a sample sentence"

# translated_words = []

# for w in my_string.split():
# 	translated_words.append(dictionary[w])

# print(" ".join(translated_words))

# my_string = "this is a sample dog"

# translated_words = []

# for w in my_string.split():
# 	translated_words.append(dictionary[w])

# print(" ".join(translated_words))