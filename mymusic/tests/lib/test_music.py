from mymusic.tests import *
from mymusic.lib.music import *


class TestMusicLib(TestController):
    """
    Testing Music lib
    """
       
    def test_addsong(self):
        """
        Test the add song to DB function
        """
        song = {"title":"Test Song", "artist":"Test artist", "name":"Test name"}
        self.music = addsong(song)

    def test_findwhere(self):
        """
        Test the find where function. Search for a song in the DB
        """
        query = "test song"
        result = findwhere(query)
        for row in result:
            assert row["artist"] == "Test artist"

    def test_update(self):
        """
        Test the update a song in DB function. Add or update features
        for a song in the DB
        """
        query = "test song"
        song = {"title":"Test Song", "artist":"Test artist", "name":"Test name"}
        self.music = addsong(song)
        
        newsong = {"albumart":"art.png"}
        update(self.music, newsong)
        result = findwhere(query).first()
        result["albumart"] == "art.png"
        
    def test_remove(self):
        """
        Test the remove function. Remove certain songs from DB.
        This is a also a cleanup for this test class.
        """
        query = "Test Artist"
        result = findwhere(query)
        for row in result:
            remove(row["id"])
        query = "Test Song"
        result = findwhere(query)
        for row in result:
            remove(row["id"])
            
        
