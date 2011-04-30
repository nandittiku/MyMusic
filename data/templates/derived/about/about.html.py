from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291314643.7811699
_template_filename='/home/nandittiku/Desktop/Classes/CS242/Project/myMusic/mymusic/templates/derived/about/about.html'
_template_uri='/derived/about/about.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<div class="content wrapper about">\n\n  ')
        # SOURCE LINE 5
        messages = h.flash.pop_messages() 
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['messages'] if __M_key in __M_locals_builtin()]))
        __M_writer(u'\n')
        # SOURCE LINE 6
        if messages:
            # SOURCE LINE 7
            __M_writer(u'  <ul id="failure-flash-messages">\n')
            # SOURCE LINE 8
            for message in messages:
                # SOURCE LINE 9
                __M_writer(u'    <li>')
                __M_writer(escape(message))
                __M_writer(u'</li>\n')
            # SOURCE LINE 11
            __M_writer(u'  </ul>\n')
        # SOURCE LINE 13
        __M_writer(u'\n  <p>\n    MyMusic is a free Open Source Decentralized P2P music streaming server.<br>\n    You can share your music with anyone you like via the internet.<br>\n    Just set up the server on your machine with your music and connect to your computer to listen to your songs.\n  </p>\n  <br>\n  <p>\n    <h3>Setting-Up:</h3>\n    <ol>\n      <li>\n\t<p>\n\t  Register your Application with facebook <a href="http://www.facebook.com/developers/apps.php">here</a>.\n\t  MyMusic relies on facebook for authentication.\n\t  Make sure that the information in the setup files are correct.\n\t  If you are in localhost, you are the admin. You can get your IP on your ')
        # SOURCE LINE 28
        __M_writer(escape(h.link_to('settings page', url(controller='admin', action='index',))))
        __M_writer(u'\n\t</p>\n      </li>\n      <li>\n\t<p>\n\t  Once your application has been set up with facebook, you need to add\n\t  songs to your music library. Go to the ')
        # SOURCE LINE 34
        __M_writer(escape(h.link_to('admin page', url(controller='admin', action='index',))))
        __M_writer(u'\n\t  and add your music.\n\t  You can also get information and albumart from Lastfm.\n\t</p>\n      </li>\n      <li>\n\t<p>\n\t  Thats it! You are now ready to share your music with your friends.\n\t</p>\n      </li>\n    </ol>\n  </p>\n  <br><br>\n  <p>MyMusic - written and maintained by Nandit Tiku</p>\n  <p>Contact: nandittiku AT gmail d0t com</p>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


