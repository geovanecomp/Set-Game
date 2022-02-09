# Set Game (Python)
## Introduction
This project implements a Python version of the well-known and classic game called Set. In a nutshell, this game's goal is to find the maximum number of card combinations following specific rules. These rules are regarding the attributes of a card which are: Shape (Ovals, Diamonds, Squiggles), Colors (Red, Green, Purple), Quantity (One, Two, Three), and Shade/Fill (Solid, Stripped, Open).

In a bunch of cards (usually 12) you need to find a combination of 3 cards in order to make a "_Set_" that respect the following rule: _"A Set is a collection of three cards in which each of the four attributes are all the same **or** are all different."_

Here is an example of how the real game looks like:
<p align="center">
  <img src="https://user-images.githubusercontent.com/3878792/153259078-38bfa818-c0b0-4fd5-bedf-f760bd651ed2.png" alt="Set's game example"/>
</p>


Of course, nothing is better to teach you how to play than the official website or the Wikipedia, so please, feel free to check them:
- Official Site: https://www.setgame.com/set/puzzle
- Wikipedia: https://en.wikipedia.org/wiki/Set_(card_game)

## Python Project
This project built a _SetEvaluator_ that allows a user to check if the selected cards are a "Set", check if there are any possible combination of cards that form a "Set" and it also tells you what are the cards that will make a "Set" for you - Please don't cheat using this feature ;).

Besides the best programming approaches, I also used:
- _OOP_ (Object Oriented Programming).
- _Inheritance_ that allows a properly code reuse, validation, and error handling in a single place for all classes.
- _Exception Handler_ approach to catch general _ValueErrors_.
- _Docker_.
- And most important, there are **_several automated tests_**.
