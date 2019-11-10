import random
from gtts import gTTS
from playsound import playsound
import os.path
import json

def generate_good_job():
    if os.path.exists("good_job.mp3"):
        good_job = ("good_job.mp3")
        try_again = ("try_again.mp3")

    else:    
        # generate the good_job audio file
        good_job_raw = gTTS(text="Good Job", lang="en-uk")
        good_job_raw.save("good_job.mp3")
        good_job = ("good_job.mp3")

    return good_job

def generate_try_again():
    if os.path.exists("try_again.mp3"):
        try_again = ("try_again.mp3")

    else:
        # generate the try_again audio file    
        try_again_raw = gTTS (text="Try again", lang="en-uk")
        try_again_raw.save("try_again.mp3")
        try_again = ("try_again.mp3")

    return try_again

def generate_word(word):
    if os.path.exists(word + ".mp3"):
        file_name = (word + ".mp3")

    else:
        # generate any word with "how do you spell" at the front
        file_name =(str(word)+".mp3")
        text_to_speech = gTTS(text=("How do you spell " + word +"?"), lang="en-uk")
        text_to_speech.save(file_name)
    
    return file_name
    

if __name__ == '__main__':

    with open("weekly-spelling-lists.json") as f:
        weekly_spelling_list = json.load(f)

    good_job = generate_good_job()
    try_again = generate_try_again()


    # Pick a list to quiz
    choices = {i: d for i, d in enumerate(weekly_spelling_list, start=1)}
    print('Spelling List Options')
    print('\n'.join(f'{i}. {d}' for i, d in choices.items()))
    choice = int(input('Enter your choice: '))
    week = choices[choice]
    words = weekly_spelling_list[week]
    random.shuffle(words)
    print()

    # Run the quiz!
    misspelled_words = []
    for i, word in enumerate(words, start=1):
        print(f'{i}.', end=' ')
        sound_file = generate_word(word=word)
        
        while (True):
            playsound(sound_file)
            guess = input(f'How do you spell {word}?\n> ').lower()
            if guess == word:
                print('Good job!')
                playsound(good_job)
                break
                
            else: 
                playsound(try_again)
                misspelled_words.append(word)

    # Print results info
    print('All done!')
    print()
    if misspelled_words:
        print(f'Here are the words you should work on:', end=' ')
        print(', '.join(set(misspelled_words)))

