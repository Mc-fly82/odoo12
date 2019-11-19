# -*- coding: utf-8 -*-
from odoo import http

class Helloworld(http.Controller):
    @http.route('/helloworld/helloworld/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/helloworld/helloworld/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helloworld.listing', {
#             'root': '/helloworld/helloworld',
#             'objects': http.request.env['helloworld.helloworld'].search([]),
#         })

#     @http.route('/helloworld/helloworld/objects/<model("helloworld.helloworld"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helloworld.object', {
#             'object': obj
#         })
