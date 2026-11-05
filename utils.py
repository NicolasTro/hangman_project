#!/usr/bin/env python3
import random

def get_random_word():
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        words = []
        for line in file:
            word = line.strip()
            if word.isalpha():
                words.append(word)
        
        return random.choice(words)
