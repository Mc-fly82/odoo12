# -*- coding: utf-8 -*-
from odoo import http

class Helloworl(http.Controller):
    @http.route('/home/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/guess/', auth='public')
    def employee(self,**kw):
        return http.request.render('helloworl.index', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })

#     @http.route('/helloworl/helloworl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helloworl.listing', {
#             'root': '/helloworl/helloworl',
#             'objects': http.request.env['helloworl.helloworl'].search([]),
#         })

#     @http.route('/helloworl/helloworl/objects/<model("helloworl.helloworl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helloworl.object', {
#             'object': obj
#         })
