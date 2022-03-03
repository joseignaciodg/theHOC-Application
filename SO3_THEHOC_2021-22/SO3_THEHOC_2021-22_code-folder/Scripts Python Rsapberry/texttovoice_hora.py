import os
import sys

name = "hora.txt"

with open(name, 'r') as file:
    data = file.read().replace('\n', '')

def robot(text):
        os.system("espeak -s 130 ' " + text + " ' ")

robot(data)
