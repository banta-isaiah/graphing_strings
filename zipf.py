import math
import turtle
from collections import Counter

def file_to_string(f_name):
    text_file = open(f_name, 'r')
    text = text_file.read()
    text_file.close()
    text = text.lower()
    return text


def strip_chars(string):
    text = file_to_string(string)
    stripped_text = ''
    for char in text:
        if 96 < ord(char) < 122:
            stripped_text += char
        else:
            stripped_text += ' '
            
    return stripped_text


def string_to_word_list(string):
    text = strip_chars(string)
    text = ' '.join(text.split())
    words = text.split()
    return words
            
                  
def word_dic_freq(string):
    words = string_to_word_list(string)
    word_freq = Counter(words)
    return word_freq


def graph_words(tr, dic):
    data = word_dic_freq(dic)
    x = 0
    for key in data:
        y = data[key] / 10
        tr.goto(x, y)
        tr.dot(3)
        x += 1
        
    

    
    
    
    
    
    
    
        
        
def main():
    tr = turtle.Turtle()
    tr.hideturtle()
    tr.speed()
    graph_words(tr, 'C:/Users/Xannatas/Coding/Python/king_james.txt')
    screen = tr.getscreen()
    screen.exitOnClick()
main()
