from decorator import decorator
import mymusic.lib.facebook as facebook
from pylons import request, config, url
from pylons.controllers.util import redirect
from mymusic.lib.friends import *
from mymusic.lib import helpers as h
from paste.request import construct_url
from paste.deploy.converters import asbool


def authorize(valid, handler):
    """
    Checks if the user is authorized to view page
    """
    def validate(func, self, *args, **kwargs):
        try:
            valid.check()
        except NotValidAuth, e:
            return handler(e)
        return func(self, *args, **kwargs)
    return decorator(validate)

class NotValidAuth(Exception):
    pass

class IsLogged(object):
    """
    Checks if the user is logged in
    """
    
    def __init__(self, *args):
        self.args = args
    
    def check(self):
        """
        Checks if the user is authorized to view page
        """
        if islocalhost():
                return True
        if ispublic():
            return True
        try:
            friendslist = FriendsList()
        except:
            raise NotValidAuth("You are not logged in.")

        are_friends = friendslist.are_friends()
        if are_friends:
            return True
        else:
            raise NotValidAuth("You are not friends with the user")


class IsAdmin(object):
    """
    Checks to see if the user is logged in and then to see if
    the facebook id data matches the data in the
    setup files for the admin user.
    """
    
    def __init__(self, *args):
        self.args = args
    
    def check(self):
        """
        Checks if the user is authorized to view page. Needs to be admin
        """
        if islocalhost():
                return True
        try:
            Cookie = facebook.is_connected(request.cookies)
            if "access_token" in Cookie:
                graph = facebook.GraphAPI(Cookie["access_token"])
                user = graph.get_object("me")
                if user["id"] == config.get("facebook.uid"):
                    return True
                else:
                    raise NotValidAuth("not logged in ma boi!")
            else:
                raise NotValidAuth("not logged in ma boi!")
        except:
            raise NotValidAuth("No admin cookies set")


def handler(message):
    """
    Handler if the user is not logged in.
    """
    h.flash("You can not access that page. Make sure you are logged in. You need to be facebook friends with "+config.get("name")+" to listen to music.")
    redirect(url(controller='about', action='index'))

def adminhandler(message):
    """
    Handler if the user is not admin.
    """
    h.flash("You need to be the admin to change settings.")
    redirect(url(controller='about', action='index'))


def islocalhost():
    """
    Checks to see if the user is accessing the page locally.
    @return True if user is on localhost
    @return False if user is not on localhost
    """
    URL = construct_url(request.environ, with_query_string=False, with_path_info=False)
    return ( URL.find("localhost") > -1 )

def isadmin():
    """
    Checks to see if the user is the admin.
    If the user is on localhost or is authed by facebook
    as the owner of the app, then the user is admin
    @return True if the user is the admin
    @return False if the user is not the admin
    """
    if islocalhost():
        return True
    try:
        Cookie = facebook.is_connected(request.cookies)
        if Cookie is None:
            return False
        if "access_token" in Cookie:
            graph = facebook.GraphAPI(Cookie["access_token"])
            user = graph.get_object("me")
            if user["id"] == config.get("facebook.uid"):
                return True
    except:
        pass
    return False

def ispublic():
    return asbool(config.get("public"))
