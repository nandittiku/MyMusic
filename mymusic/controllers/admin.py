import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from mymusic.lib.base import BaseController, render
from mymusic.lib.auth import *
from paste.request import construct_url
from mymusic.lib.helpers import getIP
from pylons import config
from paste.deploy.converters import asbool

log = logging.getLogger(__name__)

class AdminController(BaseController):
    """
    For rendering the admin Page
    """

    @authorize(IsAdmin(), adminhandler)
    def index(self):
        """
        Render admin page
        """
        c.host = getIP()
        return render("/derived/admin/index.html")
