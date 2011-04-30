from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291314675.8611469
_template_filename='/home/nandittiku/Desktop/Classes/CS242/Project/myMusic/mymusic/templates/derived/music/addmusic.html'
_template_uri='/derived/music/addmusic.html'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<script>\n/* Make request to get LastFM information via Ajax  */\nfunction lastfm()\n{\n  $("#lastfmdone").html("<img src=\'/ajax-loader.gif\' alt=\'Getting information. This may take a while.\' />");\n    $.ajax({\n      type: "POST",\n      url: "/music/lastfm/",\n      data: "",\n      success: function(response){  $("#lastfmdone").html("<img src=\'/check.gif\' alt=\'Done\' />");}\n    });\n}\n\n/* Make request to clear the music database via Ajax  */\nfunction cleardb()\n{\n  $("#cleardbdone").html("<img src=\'/ajax-loader.gif\' alt=\'Getting information. This may take a while.\' />");\n    $.ajax({\n      type: "POST",\n      url: "/music/clearDB/",\n      data: "",\n      success: function(response){  $("#cleardbdone").html("<img src=\'/check.gif\' alt=\'Done\' />");}\n    });\n}\n</script>\n\n<div class="content wrapper">\n  <div style="padding:10px">\n    <p class="message">')
        # SOURCE LINE 31
        __M_writer(escape(c.message))
        __M_writer(u'</p>\n    <form name="test" method="post" action="/music/addmusic/">\n      <h4>Music Folder: </h4><input type="text" name="folder" />\n      <input type="submit" name="submit" value="Submit" class="button"/>\n    </form>\n  </div>\n\n  <div style="padding:10px">\n    <h4>Get LastFM Data: </h4><input id="lastfm" type="button" onclick="lastfm()" value="Get LastFM Info" class="button"/>\n    <span id="lastfmdone"></span>\n  </div>\n\n  <div style="padding:10px">\n    <h4>Remove all songs: </h4> <input id="cleardb" type="button" onclick="cleardb()" value="Clear DB" class="button"/>\n    <span id="cleardbdone"></span>\n  </div>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


