# Project 2: Movie Trailer Website
### by Pran Kumar Sarkar

Movie trailer website project, part of the Udacity [Python Foundation Nanodegree](https://in.udacity.com/course/python-foundation-nanodegree--nd002-inpy).

## What it is and does

A Python program that produces the HTML for a movie website that displays a number of movie and Tv series trailers. Click on a poster to play its trailer.

## Required Libraries and Dependencies

Python 3.x is required to run this project. The Python executable should be in your default path, which the Python installer should have set.

## Project contents

This project consists for the following files:

* **entertainment_center.py** - main Python script to run.
* **media.py** - contains the class Movie and class TvSeries that stores movie and Tv-series details.
* **fresh_tomatoes.py** - creates the HTML file for the website (Udacity supplied and then tweaked)
* **datafile_movie.csv** - contains the data of the movie trailers.
* **datafile_tv_series.csv** - contains the data of the tv series trailers.
* **website.html** - Output html file which was created when *entertainment_center.py* was run.

## How to Run Project

Download the project zip file to your computer and unzip the file. Or clone this repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal window in Linux, the command prompt in Windows).

Navigate to the project directory and type in the following command:

```bash
python entertainment_center.py
```

Your default browser should launch a new tab displaying the movie trailer website.

## Extra Credit Description

The following features were implemented to gain an extra credit from Udacity:

* Added the storyline of the movie to the website.
* Added the release date to the Movie class, which is also displayed on the website.
* Changed the background and text colour to create a dark blue theme for the website.
* Added drop shadow to the movie poster images.
* Added Tv series trailers by inheriting Movie class.
* Added trailer poster images border.

## Vulnerabilities and fixes
To ensure all the trailers align perfectly, the minimum len of characters of movie/Tv_series story_line should be at least 136 characters. However if the story_line is greater than 136 characters, then the exceeding characters are truncated.


