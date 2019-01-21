#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stores details of movies and displays them on a website."""
import pandas as pd
import media
import fresh_tomatoes


def get_trailer_data(data, object_name, flag=0):
    """
    This function gets name, story_line, you_tube_trailer, poster_image_url,
    release_date of movies or Tv series.

    :param:
        (DataFrame) data: Stores DataFrame containing movie/Tv series details
        (str) object_name: Stores name of film/Tv_series.
        (int) flag: If flag=0 then no season information is fetched.
                    If flag=1 then season information is fetched.
    :return:
        (str) name: Name of the movie or Tv_series.
        (str) story_line: Small summary of film/Tv_series.
        (str) yt_trailer_url: You tube trailer link.
        (str) poster_image_url: Poster image link.
        (str) release_date: Date of release of movie/Tv_series
        (str) season: The season information of Tv_series if flag=1
    """
    name = object_name
    story_line = data.loc[object_name, 'story_line']
    yt_trailer_url = data.loc[object_name, 'you_tube_trailer_url']
    poster_image_url = data.loc[object_name, 'poster_image_url']
    release_date = data.loc[object_name, 'release_date']

    # Restricting story_line to 136 characters for fixed grid size.
    if len(story_line) > 136:
        story_line = story_line[0:136] + "..."

    # Getting season information if Tv series
    if flag:
        season = data.loc[object_name, 'season']
        return [name, story_line, yt_trailer_url,
                poster_image_url, release_date, season]
    else:
        return [name, story_line, yt_trailer_url,
                poster_image_url, release_date]


def main():
    """
    Creates Movie objects and initializes these objects with title,
    story_line, you_tube_trailer_url, poster_image_url, & release_date.

    Also creates Tv series objects and initializes these objects with
    title, story_line, you_tube_trailer_url, poster_image_url,
    release_date, and season.
    """
    # Reading movies and TvSeries datafiles
    data_movie = pd.read_csv("datafile_movie.csv", index_col='title')
    data_tv_series = pd.read_csv("datafile_tv_series.csv", index_col='title')

    # Creating movies objects
    movie_data = get_trailer_data(data_movie, "A-X-L")
    axl = media.Movie(movie_data[0], movie_data[1], movie_data[2],
                      movie_data[3], movie_data[4])

    movie_data = get_trailer_data(data_movie, "Tau")
    tau = media.Movie(movie_data[0], movie_data[1], movie_data[2],
                      movie_data[3], movie_data[4])

    movie_data = get_trailer_data(data_movie, "Automata")
    automata = media.Movie(movie_data[0], movie_data[1],
                           movie_data[2], movie_data[3],
                           movie_data[4])

    movie_data = get_trailer_data(data_movie, "Extinction")
    extinction = media.Movie(movie_data[0], movie_data[1],
                             movie_data[2], movie_data[3],
                             movie_data[4])

    movie_data = get_trailer_data(data_movie, "Stealth")
    stealth = media.Movie(movie_data[0], movie_data[1],
                          movie_data[2], movie_data[3],
                          movie_data[4])

    movie_data = get_trailer_data(data_movie, "Maze Runner: The Death Cure")
    maze_runner_the_death_cure = media.Movie(movie_data[0], movie_data[1],
                                             movie_data[2], movie_data[3],
                                             movie_data[4])

    movie_data = get_trailer_data(data_movie, "Maze Runner: The Scorch Trials")
    maze_runner_the_scorch_trials = media.Movie(movie_data[0], movie_data[1],
                                                movie_data[2], movie_data[3],
                                                movie_data[4])

    movie_data = get_trailer_data(data_movie, "The Maze Runner")
    the_maze_runner = media.Movie(movie_data[0], movie_data[1],
                                  movie_data[2], movie_data[3],
                                  movie_data[4])

    movie_data = get_trailer_data(data_movie, "Interstellar")
    interstellar = media.Movie(movie_data[0], movie_data[1],
                               movie_data[2], movie_data[3],
                               movie_data[4])

    movie_data = get_trailer_data(data_movie, "Pacific Rim")
    pacific_rim = media.Movie(movie_data[0], movie_data[1],
                              movie_data[2], movie_data[3],
                              movie_data[4])

    movie_data = get_trailer_data(data_movie, "Pacific Rim: Uprising")
    pacific_rim_uprising = media.Movie(movie_data[0], movie_data[1],
                                       movie_data[2], movie_data[3],
                                       movie_data[4])

    movie_data = get_trailer_data(data_movie, "Lucy")
    lucy = media.Movie(movie_data[0], movie_data[1],
                       movie_data[2], movie_data[3],
                       movie_data[4])

    movie_data = get_trailer_data(data_movie, "Prometheus")
    prometheus = media.Movie(movie_data[0], movie_data[1],
                             movie_data[2], movie_data[3],
                             movie_data[4])

    movie_data = get_trailer_data(data_movie, "Edge of Tomorrow")
    edge_of_tomorrow = media.Movie(movie_data[0], movie_data[1],
                                   movie_data[2], movie_data[3],
                                   movie_data[4])

    movie_data = get_trailer_data(data_movie, "Inception")
    inception = media.Movie(movie_data[0], movie_data[1],
                            movie_data[2], movie_data[3],
                            movie_data[4])

    # Creating TvSeries objects
    series_data = get_trailer_data(data_tv_series, "Westworld: S1", 1)
    westworld_s1 = media.TvShow(series_data[0], series_data[1], series_data[2],
                                series_data[3], series_data[4], series_data[5])

    series_data = get_trailer_data(data_tv_series, "Westworld: S2", 1)
    westworld_s2 = media.TvShow(series_data[0], series_data[1], series_data[2],
                                series_data[3], series_data[4], series_data[5])

    series_data = get_trailer_data(data_tv_series, "Intelligence: S1", 1)
    intelligence_s1 = media.TvShow(series_data[0], series_data[1],
                                   series_data[2], series_data[3],
                                   series_data[4], series_data[5])

    series_data = get_trailer_data(data_tv_series, "Intelligence: S2", 1)
    intelligence_s2 = media.TvShow(series_data[0], series_data[1],
                                   series_data[2], series_data[3],
                                   series_data[4], series_data[5])

    series_data = get_trailer_data(data_tv_series, "Minority Report", 1)
    minority_report = media.TvShow(series_data[0], series_data[1],
                                   series_data[2], series_data[3],
                                   series_data[4], series_data[5])

    series_data = get_trailer_data(data_tv_series, "Almost Human", 1)
    almost_human = media.TvShow(series_data[0], series_data[1],
                                series_data[2], series_data[3],
                                series_data[4], series_data[5])

    # Creating movie trailer website
    fresh_tomatoes.open_movies_page([axl, tau, automata, extinction, stealth,
                                     maze_runner_the_death_cure,
                                     maze_runner_the_scorch_trials,
                                     the_maze_runner, interstellar,
                                     pacific_rim, pacific_rim_uprising,
                                     lucy, prometheus, edge_of_tomorrow,
                                     inception, westworld_s1, westworld_s2,
                                     intelligence_s1, intelligence_s2,
                                     minority_report, almost_human])


if __name__ == '__main__':
    main()
