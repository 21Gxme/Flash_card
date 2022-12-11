# Project : Flash card
Flash card is a simple application that helps you to learn new words. It is a very useful
tool for students and people who want to learn a new language. In addition,it will help you
to learn other subjects like math, history, geography, e.g. memorizing the year about historical events, 
the capital of countries, the multiplication table, etc.


## Overview & Features
Flash card have 2 modes and 2 methods to learn.

#### MODES
- Show mode: You can see the vocabulary only. You can't see the meaning of the vocabulary.
If you want to see the meaning of the vocabulary, you can type the "S" to show meaning.
- Game mode: You can see the vocabulary only. and you have just 3 lives to guess 
the meaning of the vocabulary. if you guess the meaning wrong . you will lose 1 lives.
and if you guess the meaning right, you will get 1 lives. (maximum lives is 3.)

#### METHODS TO GET VOCABULARY
- CSV file: You can import the vocabulary from a CSV file. The CSV file must have 2 columns. 
You can write the vocabulary in the first column and the meaning in the second column.
- User input: You can input the vocabulary by yourself. It will be stored in a dictionary form.


## Installation
To install the application, you need to have installed the following programs:
- Python 3.8 or higher

3 modules to import
- Import random
- Import csv
- Import os

## Usage
#### Please use  Mac OS to run application
To run the application, you need to run the following command:
```bash
python flash_card.py
`````
#### recommend to use terminal to run the application.


## Program Design
The program is designed using the Object-Oriented Programming (OOP) paradigm.
The program is divided into 5 classes:
- FlashCard: This class is the main
- FlashCardGame: This class is the game
- FlashCardShow: This class is the show
- Read_write: This class is the read and write csv file
- Get_vocabulary: This class is the get vocabulary from user input 

## Code structure
The program is divided into 5 files:
- flash_card.py: This file contains the main function.
- flash_card_game.py: This file contains the class FlashCardGame.
- flash_card_show.py: This file contains the class FlashCardShow.
- read_write.py: This file contains the class Read_write.
- get_vocabulary.py: This file contains the class Get_vocabulary.
