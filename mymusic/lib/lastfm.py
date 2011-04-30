from BeautifulSoup import BeautifulStoneSoup
import mymusic.lib.music as musicDB
import urllib
from pylons import config

class LastFM():
    """
    Simple LastFM API class
    """
    
    def __init__(self):
        """
        initialize object if urls and API key
        """
        API_KEY = str(config.get("lastfm.apikey"))
        self.trackurl = "http://ws.audioscrobbler.com/2.0/?method=track.search&api_key="+API_KEY
        self.wikiurl = "http://ws.audioscrobbler.com/2.0/?method=track.getinfo&api_key="+API_KEY
        

    def gettrackinfo(self, track="", artist=""):
        """
        getinfo - Get info from Lastfm about a particular song
        @param track - Track name and other information we may have
        @return song - Return the song information on success
                       else return None on failure
        """
        track = track.replace("&", "and")
        artist = artist.replace("&", "and")
        url = self.trackurl+"&track="+track.encode('ascii')+"&artist="+artist.encode('ascii')
        try:
            file = urllib.urlopen(url)
            page = BeautifulStoneSoup(file.read())
            file.close()
            
            info = page.find("track")
            song = {}
            song["track"] = info.find("name").next
            song["artist"] = info.find("artist").next
            song["albumart"] = info.findAll("image")[0].next
        except Exception as e:
            print e
            return None

        return song

    def getwiki(self, artist, track):
        # now you can use that object every where
        url = self.wikiurl+"&track="+track.encode('ascii')+"&artist="+artist.encode('ascii')
        song = {}
        try:
            file = urllib.urlopen(url)
            page = BeautifulStoneSoup(file.read())
            file.close()
            song["summary"] = page.find("wiki").summary.next
            song["content"] = page.find("wiki").content.next
        except:
            return None
         
        return song
         

    def all(self):
        """
        all - Get info from LastFM of all songs in the DB
              and store the new info in the DB
        """
        songs = musicDB.findall()
        for s in songs:
            updatedata = self.gettrackinfo(s.title, s.artist)
            if updatedata:
                musicDB.update( s, updatedata )
            wikidata = self.getwiki(s.artist, s.title)
            if wikidata:
                musicDB.update( s, wikidata )
