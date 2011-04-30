from mymusic.tests import *
from mymusic.model import meta, music
from pylons import request, response, session, tmpl_context as c, url
from mymusic.lib.music import findsong

class TestMusicController(TestController):

    def test_view(self):
        response = self.app.get(url(controller='music', action='view'))
        assert 'dave' in response.c.songs.artist
        assert 'audioslave' in response.c.songs.artist
        assert 'gasoline' in response.c.songs.title

    def test_songinfo(self):
        response = self.app.get(url(controller='music', action='view', songID=1))
        assert response.c.song.title == "Dave"

    def test_removesong(self):
        id = 1
        response = self.app.get(url(controller='music', action='removesong', songID=id))
        assert response == "True"
        assert songinfo(id) == None
    
