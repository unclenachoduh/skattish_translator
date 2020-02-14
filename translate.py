from gtts import gTTS 

import os

def translate(source, mood):

	my_text = source

	language = "en-GB"

	output = gTTS(text=my_text, lang=language, slow=False)

	output.save("output.mp3")

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
		input_value = input("Enter your mood value : ")
		try:
			# try and convert the string input to a number
			temp = int(input_value)
			if temp > 0 and temp < 11:
				mood = int(temp)
			else:
				print("{input} is not a valid mood".format(input=input_value))
		except ValueError:
			# tell the user off
			print("{input} is not a number, please enter a number only".format(input=input_value))

	translate(text, mood)