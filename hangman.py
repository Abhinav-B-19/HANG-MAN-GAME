# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:44:37 2020

@author: abm
"""
import pandas as pd
import csv
import random
import re

with open(r"C:\Users\abm\Downloads\words.csv",newline='') as f:
    reader=csv.reader(f)
    data = list(reader)
    

def getRandom():
    a = random.choice(data)
    t = str(a)[1:-1].upper()
    word = t.replace("'","")
    return word
    
    
def play(word):
    word_completion = "-"* len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    print("Let's Play Hangman.")
    print(displayHangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Enter your guess: ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You have already guessed',guess)
            elif guess not in word:
                print(guess, "is not in word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job!,", guess , "is in the WORD..!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                
                #for i, letter in enumerate(word):
                    #if letter == guess:
                        #indices.append(i)
                #the below line represent the above loop.
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
                                
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the word ",guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -=1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
            
            
        else:
            print("Not a valid guess")
            
        print(displayHangman(tries))
        print(word_completion)
    if guessed:
          print("Congrats,you have guessed the word! You win!.")
    else:
          print("Sorry, you ran out of tries. The word was", word, "May be next time!")
            
       
        
    
def displayHangman(tries):
    stages = [  #6 final state: head,torso, both arms and both legs pass
              """
              +--------
              |       |
              |       o
              |      \\|/
              |       |
              |      / \\
              |
              =
              """,
              #5 head, torse, both arm and one leg
              """
              +--------
              |       |
              |       o
              |      \\|/
              |       |
              |      /
              |
              =
              """,
              #4 head , torse , two arm
              """
              +--------
              |       |
              |       o
              |      \\|/
              |       
              |      
              |
              =
              """,
              #3 head , torse , one arm
              """
              +--------
              |       |
              |       o
              |      \\|
              |       
              |      
              |
              =
              """,
              #2 head , torse
              """
              +--------
              |       |
              |       o
              |       |
              |       
              |      
              |
              =
              """,
              #1 head
              """
              +--------
              |       |
              |       o
              |      
              |       
              |      
              |
              =
              """,
              #0 initial
              """
              +--------
              |       |
              |       
              |      
              |       
              |      
              |
              =
              """
    ]
    return stages[tries]
    

    

def main():
    word = getRandom()
    
    play(word)
    
 
    while input("Do you want to play again(Y/N): ").upper() == 'Y':
        word = getRandom()
        play(word)
        

main()