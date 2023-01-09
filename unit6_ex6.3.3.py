# exercise 6.3.3 from unit 6
'''
You need to write a program that can read aloud the following sentence:

first time i'm using a package in next.py course
Guidelines:
You have to search the net for a suitable package that knows how to take text and speak it. 
Use the search for the following keywords on Google "text to speech". Install and download the
package to your computer using the pip command.

'''

import pyttsx3

def read_aloud(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

read_aloud("first time i'm using a package in next.py course")


