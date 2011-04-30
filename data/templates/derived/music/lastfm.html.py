from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291314664.5363619
_template_filename='/home/nandittiku/Desktop/Classes/CS242/Project/myMusic/mymusic/templates/derived/music/lastfm.html'
_template_uri='/derived/music/lastfm.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        if c.song.albumart.isspace():
            # SOURCE LINE 2
            __M_writer(u'<img src="/albumart.jpg" alt="" class="albumart"/>\n')
            # SOURCE LINE 3
        else:
            # SOURCE LINE 4
            __M_writer(u'<img src="')
            __M_writer(escape(c.song.albumart))
            __M_writer(u'" alt="" class="albumart"/>\n')
        # SOURCE LINE 6
        __M_writer(u'\n<span class="songname">\n  ')
        # SOURCE LINE 8
        __M_writer(escape(c.song.artist))
        __M_writer(u' - ')
        __M_writer(escape(c.song.title))
        __M_writer(u'\n</span>\n<div class="info scroll-pane">\n  ')
        # SOURCE LINE 11

        context.write(c.song.content)
        
        
        # SOURCE LINE 13
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


