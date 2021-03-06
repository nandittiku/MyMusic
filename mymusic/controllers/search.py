import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mymusic.lib.base import BaseController, render

import mymusic.lib.music as musicDB
from mymusic.lib.lastfm import LastFM
from mymusic.lib.auth import *

log = logging.getLogger(__name__)

class SearchController(BaseController):
    """
    Search page for searching songs via ajax.
    """

    @authorize(IsLogged(), handler)
    def index(self):
        """
        Returns string of ids of songs that match
        the search request.
        """
        query = request.params.get('search')
        c.songsid = musicDB.findstringwhere(query)
        return c.songsid
