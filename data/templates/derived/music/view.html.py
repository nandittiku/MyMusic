from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291618393.3200531
_template_filename='/home/nandittiku/Desktop/Classes/CS242/Project/myMusic/mymusic/templates/derived/music/view.html'
_template_uri='/derived/music/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


# SOURCE LINE 3

from pylons import config
fbappid = config.get("facebook.appid")


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
        Exception = context.get('Exception', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n<script>\nfunction lastfm(id)\n{\n\n    $.ajax({\n      type: "POST",\n      url: "/music/songinfo/"+id,\n      data: "",\n      success: function(response)\n                 {\n                    $("#Lastfm").html(response);\n                    var pane = $(\'.Lastfm\')\n \t            pane.jScrollPane();\n                 }\n    });\n}\n\nfunction search()\n{\n\n  var runningRequest = false;\n  var request;\n\n  var searchterm = $("#searchinput").val();\n  if (!searchterm)\n  {\n      viewall();\n      return;\n  }\n\n\n  // Abort opened requests to speed it up\n  if(runningRequest){\n    request.abort();\n  }\n\n  $("#searchdone").html("<img src=\'/ajax-loader.gif\' alt=\'Searching.\' />");\n  runningRequest = true;\n  request =  $.ajax({\n      type: "POST",\n      url: "/search/",\n      data: "search="+searchterm,\n      success: function(response)\n                 {\n                      hideall();\n                      var list = response.split(\',\');\n                      $.each( list, function(index, item){\n                           var id = item;\n                           $("#songid"+id).show();\n                      });\n\n                 },\n      error: function()\n                 {\n                      alert("Something went wrong.");\n                 }\n    });\n  $("#searchdone").html("");\n}\n\nfunction viewall()\n{\n    $(".songdiv").show();\n}\n\nfunction hideall()\n{\n    $(".songdiv").hide();\n}\n\nfunction removesong(id_)\n{\n      $.ajax({\n      type: "POST",\n      url: "/music/removesong/"+id_,\n      data: "",\n      success: function(response)\n                 {\n                      $("#songid"+id_).remove();\n                 },\n      error: function()\n                 {\n                      alert("Something went wrong.");\n                 }\n    });\n}\n\n</script>\n\n\n<div class="content wrapper">\n  <div class="left">\n    <span id="error"></span>\n    <div class="music-list scroll-pane" id="music-list">\n')
        # SOURCE LINE 102
        for song in c.songs:
            # SOURCE LINE 103
            __M_writer(u'        <div class="songdiv" onclick="lastfm(')
            __M_writer(escape(song.id))
            __M_writer(u')" id="songid')
            __M_writer(escape(song.id))
            __M_writer(u'">\n\t  <a class="songlink" href="')
            # SOURCE LINE 104
            __M_writer(escape(c.url))
            __M_writer(u'/music/listen/')
            __M_writer(escape(song.id))
            __M_writer(u'.mp3" title="')
            __M_writer(escape(song.title))
            __M_writer(u'" type="audio/mpeg" onclick="lastfm(')
            __M_writer(escape(song.id))
            __M_writer(u')">\n')
            # SOURCE LINE 105
            if song.albumart.isspace():
                # SOURCE LINE 106
                __M_writer(u'\t      <img src="/albumart.jpg" alt="" class="albumart"/>\n')
                # SOURCE LINE 107
            else:
                # SOURCE LINE 108
                __M_writer(u'\t      <img src="')
                __M_writer(escape(song.albumart))
                __M_writer(u'" alt="" class="albumart"/>\n')
            # SOURCE LINE 110
            __M_writer(u'\t    ')
            __M_writer(escape(song.artist))
            __M_writer(u' - ')
            __M_writer(escape(song.title))
            __M_writer(u'\n\t  </a>\n')
            # SOURCE LINE 112
            if c.isadmin:
                # SOURCE LINE 113
                __M_writer(u'\t  <span class="remove"><img src="/remove.png" alt="remove" class="removeimg" onclick="$(\'#confirmremove')
                __M_writer(escape(song.id))
                __M_writer(u'\').show();"/>\n\t    <span id="confirmremove')
                # SOURCE LINE 114
                __M_writer(escape(song.id))
                __M_writer(u'" class="confirmremove">\n\t      <span>Confirm: </span>\n\t      <span class="confirmopt" onclick="removesong(')
                # SOURCE LINE 116
                __M_writer(escape(song.id))
                __M_writer(u');">Y</span>\n\t      <span class="confirmopt" onclick="$(\'#confirmremove')
                # SOURCE LINE 117
                __M_writer(escape(song.id))
                __M_writer(u'\').hide();">N</span>\n\t    </span>\n\t  </span>\n')
            # SOURCE LINE 121
            __M_writer(u'\t</div>\n')
        # SOURCE LINE 123
        __M_writer(u'      \n      <br> \n    </div>\n  </div>\n\n  <div class="right">\n    <div class="Lastfm scroll-pane">\n      <div id="Lastfm">\n')
        # SOURCE LINE 131
        try:
            # SOURCE LINE 132
            if c.songs[0]:
                # SOURCE LINE 133
                __M_writer(u'\t<img src="')
                __M_writer(escape(c.songs[0].albumart))
                __M_writer(u'" class="albumart" alt="" />\n\t<span class="songname">\n\t  ')
                # SOURCE LINE 135
                __M_writer(escape(c.songs[0].artist))
                __M_writer(u' - ')
                __M_writer(escape(c.songs[0].title))
                __M_writer(u'\n\t</span>\n\t<div class="info">\n\t  ')
                # SOURCE LINE 138

                context.write(c.songs[0].content)
                          
                
                # SOURCE LINE 140
                __M_writer(u'\n\t</div>\n')
            # SOURCE LINE 143
        except Exception:
            # SOURCE LINE 144
            __M_writer(u'\t<p>No songs have been uploaded yet.</p>\n')
        # SOURCE LINE 146
        __M_writer(u'      </div>\n    </div>\n    <div class="friends">\n\t<div id="fb-root"></div><script src="http://connect.facebook.net/en_US/all.js#appId=')
        # SOURCE LINE 149
        __M_writer(escape(fbappid))
        __M_writer(u'&amp;xfbml=1"></script><fb:facepile href=""></fb:facepile>\n\t<script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script><fb:like layout="button_count"></fb:like>\n    </div>\n  </div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


