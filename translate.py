import json, re
from gtts import gTTS
from random import randrange
from pydub import AudioSegment
from nltk.tokenize import word_tokenize

def translate(source, mood):

	if len(source) > 250:
		return "Sentence must be 250 characters or less"

	my_text = source

	# Doctor input

	my_text = re.sub("…", " ", my_text)
	my_text = re.sub("-", " ", my_text)
	my_text = re.sub("\.", " ", my_text)
	my_text = re.sub("\s+", " ", my_text)

	lex = open("lexicon.txt").read().split("\n")
	dictionary = json.loads(open("dictionary.json").read())
	skat_dictionary = {}
	for key in dictionary:
		skat_dictionary[dictionary[key]] = key

	my_text = my_text.lower()

	translated_words = []

	new_words = False

	# Translate

	for w in word_tokenize(my_text):
		if re.search('[a-zA-Z]', w):
			# Add new words to dictionary
			if w not in dictionary:

				new_words = True

				l = int(len(w) / 2)

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
					dictionary[w] = lex[value]
					skat_dictionary[lex[value]] = w
				else:
					while lex[value] in skat_dictionary:
						value += 1
					dictionary[w] = lex[value]
					skat_dictionary[lex[value]] = w

			translated_words.append(dictionary[w])

	if new_words == True:
		j = json.dumps(dictionary)
		f = open("dictionary.json","w")
		f.write(j)
		f.close()

	# Add doodle-y feature
	new_translated_words = []

	for w in translated_words:
		parts = w.split("_")

		prev = False

		new_word_parts = []

		for p in parts:

			if prev == True:
				new_word_parts.append(p)
				prev = False
				continue
			
			a = randrange(0, 5)
			b = randrange(0, 5)
			c = randrange(0, 5)

			if a == b:
				prev = True
				if p[-1] == "p":
					p += "_iddy"
				else:
					if c > 2:
						p += "_dill"
					else:
						p += "_dilly"

			new_word_parts.append(p)

		new_translated_words.append("_".join(new_word_parts))

	translation = re.sub("_", " ", ". ".join(new_translated_words))

	# TTS
	language = "en-GB"
	output = gTTS(text=translation, lang=language, slow=False)
	output.save("voice_output.mp3")

	# Music Overlay
	sound1 = AudioSegment.silent(3500) + AudioSegment.from_mp3("voice_output.mp3") + AudioSegment.silent(3000)
	
	sound2 = AudioSegment.from_mp3("Handprints_happy.mp3")

	if mood == 1:
		sound2 = AudioSegment.from_mp3("Sonos_angry.mp3")
	elif mood == 2:
		sound2 = AudioSegment.from_mp3("Gypsy_Dance_bright.mp3")
	elif mood == 3:
		sound2 = AudioSegment.from_mp3("Quiet_calm.mp3")
	elif mood == 4:
		sound2 = AudioSegment.from_mp3("Loneliest_Road_in_America_US_50_dark.mp3")
	elif mood == 5:
		sound2 = AudioSegment.from_mp3("The_Black_Cat_dramatic.mp3")
	elif mood == 6:
		sound2 = AudioSegment.from_mp3("Jazz_Mango_funky.mp3")
	elif mood == 8:
		sound2 = AudioSegment.from_mp3("Getting_There_inspirational.mp3")
	elif mood == 9:
		sound2 = AudioSegment.from_mp3("Chances_romantic.mp3")
	elif mood == 10:
		sound2 = AudioSegment.from_mp3("Called_Upon_sad.mp3")
	elif mood == 11:
		sound2 = AudioSegment.from_mp3("Nighttime_Stroll_nostalgic.mp3")


	output = sound1.overlay(sound2, position=0)
	output = output.fade_out(duration=3000)

	# save the result
	output.export("output.mp3", format="mp3")

	return "Success"

if __name__ == "__main__":
	text = input("Enter your sentence : ") 
	mood = None
	while mood is None:
		print('1 Angry')
		print('2 Bright')
		print('3 Calm')
		print('4 Dark')
		print('5 Dramatic')
		print('6 Funky')
		print('7 Happy')
		print('8 Inspirational')
		print('9 Romantic')
		print('10 Sad')
		print('11 Nostalgic')
		input_value = input("Enter your mood value : ")
		try:
			# try and convert the string input to a number
			temp = int(input_value)
			if temp > 0 and temp < 12:
				mood = int(temp)
			else:
				print("{input} is not a valid mood".format(input=input_value))
		except ValueError:
			# tell the user off
			print("{input} is not a number, please enter a number only".format(input=input_value))

	print(translate(text, mood))