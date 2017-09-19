#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def main():

    secret = random.randint(1, 30)
    index = 0

    while True:
        index += 1

        guess = int(raw_input("Guess the number: "))


        if guess == secret:
            print "You won!"
            break
        elif guess > secret:
            print "Guess lower number"
        elif guess < secret:
            print "Guess higher number"

if __name__ == "__main__":
    main()