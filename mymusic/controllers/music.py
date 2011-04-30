"""
Controller for the Music Page and all that it may use.
"""
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import config
from mymusic.lib.base import BaseController, render
import mymusic.lib.music as musicDB
from mymusic.lib.lastfm import LastFM
from mymusic.lib.auth import *
from mymusic.lib.friends import FriendsList
from paste.request import construct_url

import re
import socket

log = logging.getLogger(__name__)

class MusicController(BaseController):
    """
    Generate the page for viewing, listening an adding music
    to the library.
    """

    @authorize(IsLogged(),handler)
    def index(self):
        """
        Home page (view music library)
        """
        return redirect(url(controller="music", action="view"))

    @authorize(IsLogged(),handler)
    def view(self):
        """
        View music library page
        @return rendered page
        """
        c.title = 'Music Collection'
        c.songs = musicDB.findall()
        c.uid = config.get("facebook.uid")
        c.url = construct_url(request.environ, with_query_string=False, with_path_info=False)
        c.isadmin = isadmin()
        if islocalhost():
            c.url = "http://0.0.0.0:"+str(config.get("port"))
        return render('/derived/music/view.html')

    @authorize(IsLogged(),handler)
    def songinfo(self, songID):
        """
        View lastfm info about a song
        @param songID
        """
        c.song = musicDB.findsong(songID)
        return render("/derived/music/lastfm.html")

    @authorize(IsAdmin(),adminhandler)
    def addmusic(self):
        """
        Add music to the library. Provide path to folder
        containing music and all music is added to the library.
        @return rendered page
        """
        folder = request.params.get('folder')
        if folder:
# uncomment to clear DB everything a new folder is added.            
#            musicDB.clear()
            folder = request.params['folder']
            musicDB.add(folder)
            c.message = "Music added"
        else:
            c.message = "Add music"
        return render('/derived/music/addmusic.html')


    @authorize(IsAdmin(),handler)
    def lastfm(self):
        """
        Get lastfm information
        """
        lastfm = LastFM()
        lastfm.all()
        return

#    @authorize(IsLogged(),handler)
    def listen(self, songID):
        """
        Generate a stream for the music that is requested.
        Since the songs are outsite the webservers control area
        we need to load the music into a stream and return the
        stream.
        @param songID - ID of the song to stream.
        @return content - The music stream.
        """
        songID = re.sub('\.mp3$', '', songID)
        path = musicDB.findsong(songID).path
        stream = open(path)
        content = stream.read()
        stream.close()
        response.content_type = "audio/mpeg"
        response.content_length = len(content)
        return content

    @authorize(IsAdmin(), adminhandler)
    def clearDB(self):
        """
        If you want to clear the Database.
        @return 'True' so signal that the process
        is complete
        """
        musicDB.clear()
        return "True"

    @authorize(IsAdmin(), adminhandler)
    def removesong(self, songID):
        """
        If you want to remove a particular song
        @param songID - ID of the song to remove
        @return 'True' to signal that the process
        is complete
        """
        musicDB.remove(songID)
        return "True"
