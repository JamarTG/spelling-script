import pyttsx3
from random_word import RandomWords
from pydictionary import Dictionary
import os,sys


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

def readMeaning(word):
    with HiddenPrints():
        hasDef = bool(Dictionary(word).meanings())

    if(hasDef):
        engine.say(Dictionary(word).meanings())
        engine.runAndWait()
    else:
        engine.say("No definition found")
        engine.runAndWait()

def readSynonyms(word):
    with HiddenPrints():
        hasSynonym = bool(Dictionary(word).synonyms())

        if(hasSynonym):
            engine.say(Dictionary(word).synonyms())
            engine.runAndWait()
        else:
            engine.say("No synonyms found")
            engine.runAndWait()

def readAntonyms(word):
    with HiddenPrints():
        hasAntonym = bool(Dictionary(word).antonyms())

    if(hasAntonym):
        engine.say(Dictionary(word).antonyms())
        engine.runAndWait()
    else:
        engine.say("No antonyms found")
        engine.runAndWait()

def showMenu():
    print("""
    d   -> get definitions 
    s   -> get synonyms
    a   -> get antonyms
    r   -> repeat word
    sp  -> spell word
    """)

random_word = RandomWords()

engine   = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',200)

number = int(input("NUMBER OF WORDS?"))
spellings = []
score  = 0

for i in range(number):
    theRandomWord = random_word.get_random_word(hasDictionaryDef="true") 
    if('-' in theRandomWord):
        hyphen = "The word has a hypen"
    if(' '):
        hyphen = "The word has a space"
    else:
        hyphen = ""

    if i == 0:
        engine.say("Your word is " + theRandomWord)
    else:
        engine.say("Your next word is " + theRandomWord) 
    

    engine.runAndWait()
    if(hyphen == '-'):
        engine.say("Your word has an hyphen")
        engine.runAndWait()
    if(hyphen == ' '):
        engine.say("Your word has a space")
        engine.runAndWait()

    spelled = False
    while(spelled is False):
        cmd = input("cmd::[m -> menu]")
        if(cmd.lower() == 'd'):
            readMeaning(theRandomWord)
        elif(cmd.lower() == 's'):
            readSynonyms(theRandomWord)
        elif(cmd.lower() == 'a'):
            readAntonyms(theRandomWord)
        elif(cmd.lower() == 'm'):
            showMenu()
        elif(cmd.lower() == 'sp'):
            sp = input("->")
            if(sp.lower() == theRandomWord.lower()):
                engine.say("That is correct")
                engine.runAndWait()
                score+=1
            else:
                engine.say("That is incorrect")
                engine.runAndWait()
            
            spellings.append((sp,theRandomWord))
            spelled = True

        elif(cmd.lower() == 'r'):
            engine.say("the word is "+ theRandomWord)
            engine.runAndWait()
        else:
            engine.say("That is not a valid command")
            engine.runAndWait()
print()
print(f""" you got {score} out of {number}
    {(score/number)*100}%
""")

for words in spellings:
    print(f"{words[0]} <-> {words[1]}") 