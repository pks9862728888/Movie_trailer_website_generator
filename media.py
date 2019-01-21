#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Defines classes for creation of movie trailer website"""
import webbrowser


class Movie:
    """
    This class provides a way to store movie related information.

    Attributes:
        title: A string to store the title of the movie.
        story_line: A string to store the basic plot of the movie.
        you_tube_trailer_url: A string to store the URL of the movie trailer.
        poster_image_url: A string to store the URL of the movie poster.
        release_date: A string to store the release date of the movie.

    Methods:
        show_trailer(self): Shows trailers on web browser.
    """

    def __init__(self, title, story_line, you_tube_trailer_url,
                 poster_image_url, release_date):
        self.title = title
        self.story_line = story_line
        self.you_tube_trailer_url = you_tube_trailer_url
        self.poster_image_url = poster_image_url
        self.release_date = release_date

    def show_trailer(self):
        """Shows the movie trailers in web browser."""
        webbrowser.open(self.you_tube_trailer_url)


class TvShow(Movie):
    """
    This class provides a way to store Tv series related information.
    It inherits Movie class.

    Attributes:
        title: A string to store the title of the movie.
        story_line: A string to store the basic plot of the movie.
        you_tube_trailer_url: A string to store the URL of the movie trailer.
        poster_image_url: A string to store the URL of the movie poster.
        release_date: A string to store the release date of the movie.
        season: An integer to store the season of Tv series.
    """

    def __init__(self, title, story_line, you_tube_trailer_url,
                 poster_image_url, release_date, season):
        Movie.__init__(self, title, story_line, you_tube_trailer_url,
                       poster_image_url, release_date)
        self.season = season
