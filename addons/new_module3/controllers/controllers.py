# -*- coding: utf-8 -*-
from odoo import http

# class NewModule3(http.Controller):
#     @http.route('/new_module3/new_module3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_module3/new_module3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_module3.listing', {
#             'root': '/new_module3/new_module3',
#             'objects': http.request.env['new_module3.new_module3'].search([]),
#         })

#     @http.route('/new_module3/new_module3/objects/<model("new_module3.new_module3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_module3.object', {
#             'object': obj
#         })