import json

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words = sentence.split(' ')

wordsLetters = {word:len(words) for word in words}


with open('wordsLetters.json', 'w') as fp:
    json.dump(wordsLetters, fp)