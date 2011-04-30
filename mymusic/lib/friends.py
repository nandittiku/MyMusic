from pylons import request
from mymusic.lib import facebook
from mymusic.lib.auth import *
from pylons import config


class FriendsList():
    """
    Class to handle Facebook Graph API for friends list
    """

    def __init__(self):
        """
        Initialize Facebook Graph API and check for cookies
        """
        try:
            access_token = facebook.is_connected(request.cookies)["access_token"]
        except:
            raise Exception("Not authed.")
        self.graph = facebook.GraphAPI(access_token)
        self.user = self.graph.get_object("me")


    def get_list(self):
        """
        Get list of friends for the logged in user.
        @return list of dictionaries containing all the friends
        """
        friends = self.graph.get_connections("me", "friends")
        return friends["data"]

    def are_friends(self):
        """
        Check if the logged in user and the admin of the webserver
        are friends
        @return bool True/False
        """
        uid = config.get("facebook.uid")
        # check if is self - Facebook doesnt consider you to be
        # friends with yourself.
        if "id" in self.user:
            if uid == self.user["id"]:
                return True
            
        return self.graph.arefriends(self.user["id"], uid)
        
