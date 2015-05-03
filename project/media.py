"""
  author: H. Kin Fung
  dates: 20140406,0504
"""
import urllib
import json
from string import replace
from re import sub

class Movie():
    """ 
      construct a movie instance to contain info. of the movie
      including its title, brief storyline, poster image url, 
      and url of trailer on youtube  
    """
    def __init__(self, title, year=None, genre=None, image_url=None, video_url=None, storyline=None): 

        # auto-complete some arguements if they are no filled
        print("fetching data for " + title + " ...")
        ## get data from omdbapi
        omdb_data = json.loads( urllib.urlopen(
            "http://www.omdbapi.com/?t=" + title + " &y=&plot=short&r=json&tomatoes=true").read() )
        ## get data from youtube
        ##  ref: http://stackoverflow.com/questions/12859260/search-youtube-and-return-json
        youtube_data = json.loads( urllib.urlopen(
            "https://www.googleapis.com/youtube/v3/search?key=AIzaSyDhVnNw2DyX6110ttzSODiMjdzDfEBadYU&part=snippet&q=" + \
            replace(title, ' ', '+') + "+trailer" \
            ).read() )
        ## implement 
        if omdb_data: 
            year = year or omdb_data['Year'] 
            genre = genre or omdb_data['Genre'] 
            image_url = image_url or omdb_data['Poster'] 
            storyline = storyline or omdb_data['Plot']   
            tomato_meter = omdb_data['tomatoMeter']
        if youtube_data:
            video_url = video_url or ("http://www.youtube.com/watch?v=" + youtube_data['items'][0]['id']['videoId'])

        # set instance attributes
        self.title = sub(r": Or.*$", "", title)
        self.year = (u'' + year).encode('utf-8')
        self.genre = (u'' + genre).encode('utf-8')
        self.poster_image_url = image_url
        self.trailer_youtube_url = video_url 
        self.storyline = (u'' + storyline).encode('utf-8')
        self.tomato_meter = tomato_meter 
