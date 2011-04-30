"""
About page containing information on how to use the software, and can be
personalized to display information you may want to share with your friends
"""
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from mymusic.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AboutController(BaseController):
    """
    Generates the About page
    """
    def index(self):
        return render("/derived/about/about.html")
