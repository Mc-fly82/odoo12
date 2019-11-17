# -*- coding: utf-8 -*-

from . import controllers
from odoo import http

class Helloworl(http.Controller):
    @http.route('/home/', auth='public')
    def index(self, **kw):
        return http.request.render('academy.index', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })
