# -*- coding: utf-8 -*-
from odoo import http

# class NewModule2(http.Controller):
#     @http.route('/new_module2/new_module2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_module2/new_module2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_module2.listing', {
#             'root': '/new_module2/new_module2',
#             'objects': http.request.env['new_module2.new_module2'].search([]),
#         })

#     @http.route('/new_module2/new_module2/objects/<model("new_module2.new_module2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_module2.object', {
#             'object': obj
#         })