from mymusic.tests import *
from routes import url_for
from mymusic.model import meta
from urlparse import urlparse


class TestSearchController(TestController):
    """
    Testing controller Search
    """
    
    def test_index(self):
        response = self.app.get(
            url=url_for(controller='search', action='index'),
            params={
                'search': 'audioslave',
                },
            status = 200
            )
    
