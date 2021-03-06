"""
Used mainly by the Music Controller to access the Music DB,
get and store information about the  music.
"""

import mymusic.model.music as model
from sqlalchemy import orm
from sqlalchemy import create_engine
from sqlalchemy.sql import select, delete, update
from sqlalchemy.sql import and_, or_, not_
import os
import sys
from UserDict import UserDict

# Create an engine and create all the tables we need
engine = create_engine("sqlite:///musicDB.db")
connection = engine.connect()
model.metadata.bind = engine
model.metadata.create_all()
# Set up the session
sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,
                      expire_on_commit=True)
session = orm.scoped_session(sm)



def stripnulls(data):
    """
    Source: http://diveintopython.org/object_oriented_framework/index.html
    strip whitespace and nulls
    @param data - data to strip nulls from
    @return data after remove nulls
    """
    return data.replace("\00", "").strip()

class FileInfo(UserDict):
    """
    Source: http://diveintopython.org/object_oriented_framework/index.html
    store file metadata
    @param UserDict - To store info in
    """
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename

class MP3FileInfo(FileInfo):
    """
    Source: http://diveintopython.org/object_oriented_framework/index.html
    store ID3v1.0 MP3 tags
    @param FileInfo
    """
    tagDataMap = {"title"   : (  3,  33, stripnulls),
                  "artist"  : ( 33,  63, stripnulls),
                  "album"   : ( 63,  93, stripnulls),
                  "year"    : ( 93,  97, stripnulls),
                  "comment" : ( 97, 126, stripnulls),
                  "genre"   : (127, 128, ord)}

    def __parse(self, filename):
        """
        parse ID3v1.0 tags from MP3 file
        @param filename - Song to get ID3 tags of.
        """
        try:                               
            fsock = open(filename, "rb", 0)
            try:                           
                fsock.seek(-128, 2)        
                tagdata = fsock.read(128)  
            finally:                       
                fsock.close()              
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])               
        except IOError:                    
            pass                           

    def __setitem__(self, key, item):
        """
        Set the item info
        @param key - The key
        @param item - The attribute
        """
        if key == "name" and item:
            self.__parse(item)
        FileInfo.__setitem__(self, key, item)


def listDirectory(directory):
    """
    Given a folder, find all songs recursively and return a list of songs with ID3tag info.
    This is used to add music to the library
    @param folder - Folder containing music
    @return songs - list of songs and ID3 tag info in directory
    """
    import fnmatch
    import os

    rootPath = directory
    pattern = '*.mp3'

    ## find all songs in directory
    fileList = []
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print filename
            fileList.append(os.path.join(root, filename))

    ## get song info (ID3 tag)
    ## Source: http://diveintopython.org/object_oriented_framework/index.html
    def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):      
        "get file info class from filename extension"                             
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]       
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo

    
    return [getFileInfoClass(f)(f) for f in fileList]                  


def findsongs(folder):
    """
    Given a folder, find all songs recursively and return a list of songs with ID3tag info.
    This is used to add music to the library
    @param folder - Folder containing music
    @return songs - list of songs and ID3 tag info in directory
    """
    songs = []
    for info in listDirectory(folder):
        songs.append(info)
    return songs


def add(folder):
    """
    The API function call to be used to add music to the
    library and DB given the path to the folder.
    @param folder - Folder contaiing the music on the webserver machine.
    """
    songs = findsongs(folder)
    for song in songs:
        addsong(song)
        
def addsong(song):
    """
    Add a song to the database
    @param song - The song to add to the database
    """
    music = model.Music()
    if "title" in song:
        music.title = song["title"].encode('utf-8')
    if "artist" in song:
        music.artist = song["artist"].encode('utf-8')
    music.path = song["name"].encode('utf-8')
    session.add(music)
    session.commit()
    return music
    
        

def findall():
    """
    Wrapper around the SQL calls to find all the music
    in the library.
    @return songs - List of songs and all their corresponding information
    """
    songslist = session.query(model.Music)
    return songslist


def findwhere(query):
    """
    Search for songs which match the query.
    @param query - The song to search for
    @return songs - List of songs that match the query
    """
    sql = "select * from music where title LIKE '%"+query+"%' OR artist LIKE '%"+query+"%'"
    result = session.execute(sql)
    return result

def findstringwhere(query):
    """
    Search for songs which match the query.
    @param query - The song to search for
    @return songs - List of songs that match the query
    """
    result = findwhere(query)
    list = []
    for row in result:
        list.append(str(row["id"])+",");
    return list

    
def findsong(songID):
    """
    Wrapper around the SQL calls to find a particular song
    by ID present in the library.
    @param songID - ID of the song to search for
    @return song - associative array with information about the song
    returns None on failure
    """
    song = session.query(model.Music).filter_by(id=songID).first()
    return song

def update(song, newsong={}):
    # if "artist" in newsong:
    #     song.artist = newsong["artist"]
    # if "title" in newsong:
    #     song.title = newsong["track"]
    if "albumart" in newsong:
        song.albumart = newsong["albumart"]
    if "summary" in newsong:
        song.summary = newsong["summary"]
    if "content" in newsong:
        song.content = newsong["content"]
        
    session.add(song)
    session.commit()
    
def remove(songID):
    """
    Wrapper around the SQL call to remove a song entry
    """
    try:
        session.query(model.Music).filter_by(id=songID).delete()
        session.commit()
    except:
        pass
    
    
def clear():
    """
    Wrapper around the SQL call to clear the DB entry for
    music so the library can be clean for new input or a fresh start.
    """
    try:
        session.query(model.Music).delete()
        session.commit()
    except:
        pass
