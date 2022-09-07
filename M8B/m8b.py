import sys
import random
import json

ans = True
brief = 'You have selected to play the Magic 8 Ball. Ask the ball a question to receive your answer.\nTo quit, double tap the Enter key- until then the Magic 8 Ball awaits...'
sentencestarter = 'The Magic 8 Ball says: '
replies_file = open('replies.json')
json_array = json.load(replies_file)
array_size = len(json_array)
print(brief)

while ans:

    question = input("Ask the Magic 8 Ball a question: ")
    answer = (random.randint(1, array_size) - 1)

    if question == " ":
        sys.exit()
    else:
        print(sentencestarter + json_array[answer])