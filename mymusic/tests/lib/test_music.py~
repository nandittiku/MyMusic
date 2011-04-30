from mymusic.tests import *
from mymusic.lib.lastfm import LastFM


class TestLastfmlib(TestController):
    """
    Testing LastFM lib
    """
    
    def test_gettrackinfo_none(self):
        """
        Get information for a song that does not exists
        Should return None
        """
        lastfm = LastFM()
        song = lastfm.gettrackinfo("this makes no sense", "bloo blah blue")
        assert song == None

    def test_gettrackinfo(self):
        """
        Get song information of a known song
        """
        lastfm = LastFM()
        song = lastfm.gettrackinfo("show me how to live")
        assert song["artist"] == "Audioslave"

    def test_getwiki(self):
        """
        Get wiki information of a know song
        """
        lastfm = LastFM()
        song = lastfm.getwiki("cher", "believe")
        if song == None:
            pass
        else:
            if "summary" in song:
                assert song["summary"]
            if "content" in song:
                assert song["content"]

