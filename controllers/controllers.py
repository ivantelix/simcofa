# -*- coding: utf-8 -*-
from odoo import http

# class Simcofa-coop(http.Controller):
#     @http.route('/simcofa-coop/simcofa-coop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simcofa-coop/simcofa-coop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simcofa-coop.listing', {
#             'root': '/simcofa-coop/simcofa-coop',
#             'objects': http.request.env['simcofa-coop.simcofa-coop'].search([]),
#         })

#     @http.route('/simcofa-coop/simcofa-coop/objects/<model("simcofa-coop.simcofa-coop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simcofa-coop.object', {
#             'object': obj
#         })