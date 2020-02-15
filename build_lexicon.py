import json

phonemes = ["ska", "skay", "skee", "sko", "skoo", "skop", "skip", "scoop", "ba", "bay", "be", "bo", "boo", "bop", "beep", "boop", "da", "day", "dee", "doh", "do", "dop", "dip", "doop", "saw", "zay", "zee", "zo", "zoo", "BLANK"]

onewords = []
twowords = []
threewords = []
fourwords = []

words_dict = {}

for a in phonemes:
	for b in phonemes:
		for c in phonemes:
			for d in phonemes:

				phoneme_list = []
				if a != "BLANK":
					phoneme_list.append(a)
				if b != "BLANK":
					phoneme_list.append(b)
				if c != "BLANK":
					phoneme_list.append(c)
				if d != "BLANK":
					phoneme_list.append(d)

				if len(phoneme_list) < 1:
					continue

				check = False
				x = 0
				y = 1

				while y < len(phoneme_list):
					if phoneme_list[x] == phoneme_list[y]:
						check = True
					x += 1
					y += 1

				if check == True:
					continue

				word = "_".join(phoneme_list)

				phoneme_count = word.count("_") + 1

				if word not in words_dict:

					if phoneme_count == 1:
						onewords.append(word)
					if phoneme_count == 2:
						twowords.append(word)
					if phoneme_count == 3:
						threewords.append(word)
					if phoneme_count == 4:
						fourwords.append(word)

					words_dict[word] = ""


all_words = []

for w in onewords:
	all_words.append(w)

for w in twowords:
	all_words.append(w)

for w in threewords:
	all_words.append(w)

for w in fourwords:
	all_words.append(w)


f = open("lexicon.txt","w+")
for w in all_words:
	f.write(w + "\n")

f.close()

