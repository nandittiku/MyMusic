"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
from webhelpers.html.tags import *
from webhelpers.date import *
from webhelpers.text import *
from webhelpers.html.converters import *
from webhelpers.html.tools import *
from webhelpers.util import *
from webhelpers.pylonslib import Flash as _Flash
from routes import url_for
from urllib2 import urlopen

from webhelpers import *

import urllib

"""
For flash messages displayed.
The information is stored in session variables
that are cleared when a new page is requested, or
the page is refreshed.
"""
flash = _Flash()



def getIP():
    """
    Get the IP of the current user.
    IP obtained from http://www.whatismyip.com/automation/n09230945.asp
    @return IP address of the current user
    """
    try:
        page = urlopen("http://www.whatismyip.com/automation/n09230945.asp")
        IP = page.read()
        page.close()
        return IP
    except:
        return "Could not retrieve the IP address."
