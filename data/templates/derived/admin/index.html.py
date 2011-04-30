from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1291314673.606297
_template_filename='/home/nandittiku/Desktop/Classes/CS242/Project/myMusic/mymusic/templates/derived/admin/index.html'
_template_uri='/derived/admin/index.html'
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
        __M_writer(u'\n\n<div class="content wrapper">\n    <h2 style="display:inline; margin-right:20px">Connection host IP: ')
        # SOURCE LINE 4
        __M_writer(escape(c.host))
        __M_writer(u'</h2><h7 style="display:inline">(You and your friends connect to this url.Set this is as you canvas and application address when you create the facebook app.</h7>\n  <p>\n    <a href="/music/addmusic/" class="button">Add Music</a>\n  </p>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


