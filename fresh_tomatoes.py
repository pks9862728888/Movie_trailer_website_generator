import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Trailers!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
    
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background: #00081c;
            margin-bottom: -7%;
        }
        #boxshadow {
        position: relative;
        box-shadow: 1px 2px 4px rgba(0, 0, 0, .5);
        padding: 2px;
        background: #f2ff00;
        }
        #boxshadow img {
        width: 100%;
        border: 1px solid #0f014c;
        border-style: inset;
        }
        #boxshadow::after {
        content: '';
        position: absolute;
        z-index: -1; /* hide shadow behind image */
        box-shadow: 0 15px 20px rgba(9, 3, 3, 0.3);
        width: 70%;
        left: 15%; /* one half of the remaining 30% */
        height: 100px;
        bottom: 0;
        }
        #trailer .modal-dialog {
            margin-top: 120px;
            width: 700px;
            height: 500px;
            vertical-align: middle;
        } 
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 5px;
            padding-top: 10px;
            color: #4ddbff;
        }
        .movie-tile:hover {
            background-color: #43587a;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 60%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movies and Tv Series Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <footer style="background-color:#141419; color:#5c5c70;">
        <div class="container text-center">
            <div class="rights">copyright &copy; 2019 Pran Kumar Sarkar</div>
            <div class="rights">licensed under <a href="https://choosealicense.com/licenses/mit/" target="_blank">CC BY MIT</a></div>
            <div class="rights">Contact Us:</div>
            <div class="rights"><a href="https://www.linkedin.com/in/pran-kumar-sarkar-282b10151/">LinkedIn</a></div>
            <div class="rights">pks9862728888@gmail.com</div>
            <div>&bull; &bull; &bull;</div>
            <div class="disclaimer">All webpages appearing in this work are fictitious and for project purposes only. Any resemblance to real websites, living or dead, is purely coincidental.</div>
        </div>  
    </footer>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 match-my-cols movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="200" height="300" id="boxshadow">
    <h4><b><font color="red">{movie_title}</font></b></h4>
    <p style="font-size:13px"><b>Release Date: </b>{release_date}</p>
    <p style="font-size:13px">{movie_story_line}</p>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.you_tube_trailer_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.you_tube_trailer_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_story_line=movie.story_line,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            release_date=movie.release_date
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('webpage.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
