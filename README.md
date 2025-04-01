# How to run

## Windows

Install Python using the Microsoft store

`python -m venv .venv`
Create virtual environment

`venv/Scripts/activate`
Active environment

`pip install -r requirements.txt`
Install required libraries

`python main.py`
Run the game

`deactivate`
Close the enviroment

## MacOS

`brew install python`
Install python

`python3 -m venv .venv`
Create virtual environment

`source .venv/bin/activate`
Active environment

`pip3 install -r requirements.txt`
Install required libraries

`python3 main.py`
Run the game

`deactivate`
Close the enviroment


# Game mechanics

Press `q` to add a ball

Press `e` to remove all balls

Press `a` to apply force in a left and upright motion

Press `d` to apply force in a right and upright motion

Press `w` to apply force in an upright motion

## Mass slider
When creating a ball, the ball's mass will be determined by the mass slider.

## Force slider
The force slider determines the amount of force applied to all balls after pressing `a`, `w` or `d`.

