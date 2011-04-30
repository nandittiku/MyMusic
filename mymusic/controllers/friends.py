import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from mymusic.lib.base import BaseController, render
from mymusic.lib.friends import FriendsList

log = logging.getLogger(__name__)

class FriendsController(BaseController):
    """
    Controller which connects to the Facebook API and checks your friends list
    and verifies if the logged in user is your facebook friend.
    """
    def index(self):
        """
        Returns true if the admin and logged in user
        are facebook friends
        """
        friends = FriendsList()
        return str(friends.are_friends())


