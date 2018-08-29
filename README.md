# CopyCat Gaming Inc.

I'm currently learning Python and decided to use Python to run this application in the Command Line

## Using Python

After completing the application using React I wanted to run the application in the Command Line and output the results via a new python file (attackStatistics.py) and in the command line.


## The Character Classes and Attack Method (copyCat.py)

I created a Warrior Class that takes user inputs via the Command Line. Each class will have at least an attack object (function/method) and a levelUp object (function/method). I decided to have a different constructor function for each character type instead of a single Character constructor function because depending on game mechanics I'm leaving each Character to have uniquely defined characteristics.

The Attack Method takes in numerous user input, tests to ensure the inputs meet each input specification, and creates an object of the attack statistics and then creates and writes the results in an 'attackStatistics.py' file. It also prints the attack statistics in the Command Line

The LevelUp Method increases the specific Character's level, strength, and vitality. Each Character Type will have a unique LevelUp method since leveling up may impact each Character Type differently.

NOTE: Some inputs are commented out in the Warrior Class becuase it's not initially necessary to use the specific attributes to run this program.

## File Structure

The execute_application.py file executes the program

The copyCat.py file has the Character Classes (Warrior Class)

The characters.py file has the character data

After you run the program a attackStatistics.py file should be created with the data. This file will remain and will continuously update with the new results

## Setup

Uses Python 3

To Execute in the Command Line type the following:

python execute_application.py
