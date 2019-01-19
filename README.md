# Project 2: Movie Trailer Website
### by Pran Kumar Sarkar

Movie trailer website project, part of the Udacity [Python Foundation Nanodegree](https://in.udacity.com/course/python-foundation-nanodegree--nd002-inpy).

## Overview:

A Python program that produces the HTML for a movie website which displays a number of movies and Tv series trailers. After website has been created, it will open automatically in your default web browser. Simply click on posters to view trailers.

## Required Libraries and Dependencies:

Python 3.x is required to run this project. The Python executable should be in your default path, in which the Python installer should have set. 

Moreover pandas should be installed. 

To install pandas open the terminal or command prompt and type:

```bash
pip install pandas
```

## Project contents:

This project consists for the following files:

* **entertainment_center.py** - main Python script to run.
* **media.py** - contains the class Movie and class TvSeries that stores movie and Tv-series details.
* **fresh_tomatoes.py** - creates the HTML file for the website (Udacity supplied and then tweaked)
* **datafile_movie.csv** - contains the data of the movie trailers.
* **datafile_tv_series.csv** - contains the data of the tv series trailers.
* **website.html** - Output html file which was created when *entertainment_center.py* was run.
* **Licence.txt** - Licencing information.
* **_config.yml** - Configuration file for github theme.

## Download:
This project can be downloaded by [clicking here](https://github.com/pks9862728888/Movie_trailer_website_generator/archive/master.zip)

## How to Run Project:

Download the project zip file to your computer and unzip the file. Or clone this repository to your desktop by typing the following code in your terminal(*for Linux*) or command prompt(*for windows*):

```bash
git clone https://github.com/pks9862728888/Movie_trailer_website_generator.git
```

Navigate to the project directory and type in the following command:

```bash
python entertainment_center.py
```

Your default browser should launch a new tab displaying the movie trailer website.

## How to add new movie/Tv_series trailer into webpage:

The data of new trailers can be directly added in respective `.csv` files and then objects are to be created by typing the following code in `entertainment_center.py` inside `main()`:

If new movie trailers are to be added, then type under this following line:
```bash
# Creating movies objects
```
this following code:
```bash

movie_data = get_trailer_data(data_movie, "name_of_new_movie_added_in_csv_file")
name_of_object = media.Movie(movie_data[0], movie_data[1], movie_data[2], movie_data[3], movie_data[4])
```
However if new Tv_series trailers are to be added, then type under this following line:
```bash
# Creating movie trailer website
```
this following code:

```bash
series_data = get_trailer_data(data_tv_series, "name_of_new_Tv_series_added_in_csv_file", 1)
name_of_object = media.TvShow(series_data[0], series_data[1], series_data[2], series_data[3], series_data[4], series_data[5])
```

Then add the new created `name_of_object` in list:

```bash
# Creating movie trailer website
fresh_tomatoes.open_movies_page([axl, tau, automata, extinction, stealth, maze_runner_the_death_cure,
                                maze_runner_the_scorch_trials, the_maze_runner, interstellar, pacific_rim,
                                pacific_rim_uprising, lucy, prometheus, edge_of_tomorrow, inception,
                                westworld_s1, westworld_s2, intelligence_s1, intelligence_s2, minority_report,
                                almost_human, name_of_object])
```
Then execute `entertainment_center.py`.

## Output after running `entertainment_center.py`:

[This](http://htmlpreview.github.com/?https://github.com/pks9862728888/Movie_trailer_website_generator/blob/master/webpage.html) is what it looks like when you run *entertainment_center.py*

## Extra Credit Description:

The following features were implemented to gain an extra credit from Udacity:

* Added the storyline of the movie to the website.
* Added the release date to the Movie class, which is also displayed on the website.
* Changed the background color to create a dark blue theme for the website.
* Changed text color to get attractive look.
* Added Tv series trailers by inheriting Movie class(*i.e. implemented inheritance*).
* Added trailer poster images border.
* Fixed display problem caused when story_lines are of different lengths.

## Vulnerabilities and Fixes:
If new movie/Tv_series data is to be shown then sometimes the trailer posters might not align themselves properly in grid, especially if their story_lines are of different lengths(such as one `single-line story_line` and the other `multi-line story_line`).


To ensure all the trailers align perfectly, the minimum length of characters of movie/Tv_series story_line should be at least 136 characters(*I have taken it as minimum number of characters*). However if the story_line is greater than 136 characters, then the exceeding characters are truncated.

## References:
1. [Python Foundation Nanodegree Udacity](https://in.udacity.com/course/python-foundation-nanodegree--nd002-inpy)
2. [Markdown formatting for README.md](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
3. [Writing Readme Free Course Udacity](https://classroom.udacity.com/courses/ud777)
4. [Sample Readme by tsega](https://github.com/tsega/movie-trailer-website/blob/master/README.md)
5. [Getting preview of Html Directly from Github](https://stackoverflow.com/questions/6551446/can-i-run-html-files-directly-from-github-instead-of-just-viewing-their-source)