from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291618349.294008
_template_filename='/home/nandittiku/Desktop/Classes/CS242/Project/myMusic/mymusic/templates/base/index.html'
_template_uri='/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['header', 'head', 'footer', 'title']


# SOURCE LINE 17

from pylons import config
webname = config.get("website")
appid = config.get("facebook.appid")


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n\n<html>\n\n  <head>\n    <title>')
        # SOURCE LINE 6
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    ')
        # SOURCE LINE 7
        __M_writer(escape(self.head()))
        __M_writer(u'\n  </head>\n\n  <body>\n    ')
        # SOURCE LINE 11
        __M_writer(escape(self.header()))
        __M_writer(u'\n    ')
        # SOURCE LINE 12
        __M_writer(escape(next.body()))
        __M_writer(u'\n    ')
        # SOURCE LINE 13
        __M_writer(escape(self.footer()))
        __M_writer(u'\n  </body>\n\n</html>\n')
        # SOURCE LINE 21
        __M_writer(u'\n\n')
        # SOURCE LINE 25
        __M_writer(u'\n\n')
        # SOURCE LINE 50
        __M_writer(u'\n\n')
        # SOURCE LINE 90
        __M_writer(u'\n\n\n')
        # SOURCE LINE 103
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 52
        __M_writer(u'\n<div class="header">\n  <div class="wrapper">\n    <h1>\n      <span><a href="/">')
        # SOURCE LINE 56
        __M_writer(escape(webname))
        __M_writer(u'</a></span>\n    </h1>\n\n')
        # SOURCE LINE 59
        if "/music/view" in request.url:
            # SOURCE LINE 60
            __M_writer(u'       <div id="search">\n\t <input type="text" name="search" value="" id="searchinput" onkeyup="search()"/>\n\t <input type="submit" name="submit" value="search" onClick="search()" class="button" />\n\t <span id="searchdone"></span>\n\t <input type="submit" name="submit" value="All" onClick="viewall()"  class="button" />\n       </div>\n')
        # SOURCE LINE 67
        __M_writer(u'\n\n    <span id="controls">\n      <div id="fb-root" style="display:inline"></div>\n      <fb:login-button autologoutlink="true"></fb:login-button>\n      <script src="http://connect.facebook.net/en_US/all.js"></script>\n      <script>\n\tFB.init({appId: \'')
        # SOURCE LINE 74
        __M_writer(escape(appid))
        __M_writer(u"', status: true, cookie: true, xfbml: true});\n\tFB.Event.subscribe('auth.sessionChange', function(response) {\n\tif (response.session) {\n\t// A user has logged in, and a new cookie has been saved\n\t\n\t} else {\n\t// The user has logged out, and the cookie has been cleared\n\t}\n\t});\n      </script>\n      \n      ")
        # SOURCE LINE 85
        __M_writer(escape(h.link_to('Settings', url(controller='admin', action='index',))))
        __M_writer(u' &nbsp;\n\n    </span>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n  ')
        # SOURCE LINE 28
        __M_writer(escape(h.stylesheet_link(url('/css/style.css'))))
        __M_writer(u'\n  ')
        # SOURCE LINE 29
        __M_writer(escape(h.stylesheet_link(url('/css/jScrollPane.css'))))
        __M_writer(u'\n  <script type="text/javascript" src="http://mediaplayer.yahoo.com/js"></script>\n  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>\n  <script type="text/javascript" src="')
        # SOURCE LINE 32
        __M_writer(escape(url('/js/jScrollPane.js')))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        # SOURCE LINE 33
        __M_writer(escape(url('/js/jquery.em.js')))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        # SOURCE LINE 34
        __M_writer(escape(url('/js/jquery.mousewheel.js')))
        __M_writer(u'"></script>\n\n  <!-- Track seek -->\n  <script type="text/javascript" src="http://www.danceatthepostoffice.com/js/trackseek.js"></script>\n  <script type="text/javascript" src="http://www.danceatthepostoffice.com/js/trackresume.js"></script>\n  <script type="text/javascript" src="http://www.danceatthepostoffice.com/js/ef.ymp.utilities.js"></script>\n  <script type="text/javascript" src="http://www.danceatthepostoffice.com/js/trackfocus.js"></script>\n  <!-- /Track seek -->\n\n  <script>\n\n    $(function()\n    {\n      $(\'.scroll-pane\').jScrollPane();\n    });\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 93
        __M_writer(u'\n<div class="footer">\n  <div class="wrapper footnote">\n    <ul>\n      <li>MyMusic - written and maintained by Nandit Tiku</li>\n      <li>Powered by Pylons</li>\n      <li>')
        # SOURCE LINE 99
        __M_writer(escape(h.link_to('About', url(controller='about', action='index',))))
        __M_writer(u'</li>\n    </ul>\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 23
        __M_writer(u'\n\t')
        # SOURCE LINE 24
        __M_writer(escape(webname))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


