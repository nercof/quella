# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1475244978.534838
_enable_loop = True
_template_filename = '/home/nercof/Projects/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl'
_template_uri = 'comments_helper_isso.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link_script', 'comment_link', 'comment_form']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id and 'index' in pagekind:
            __M_writer('        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/count.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <a href="')
            __M_writer(str(link))
            __M_writer('#isso-thread">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <div data-title="')
            __M_writer(filters.url_escape(str(title)))
            __M_writer('" id="isso-thread"></div>\n        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/embed.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/home/nercof/Projects/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl", "uri": "comments_helper_isso.tmpl", "line_map": {"67": 2, "68": 3, "69": 4, "70": 4, "71": 4, "72": 5, "73": 5, "74": 5, "75": 5, "16": 0, "81": 75, "21": 7, "22": 13, "23": 20, "29": 16, "35": 16, "36": 17, "37": 18, "38": 18, "39": 18, "40": 18, "41": 18, "47": 9, "52": 9, "53": 10, "54": 11, "55": 11, "56": 11, "62": 2}}
__M_END_METADATA
"""
