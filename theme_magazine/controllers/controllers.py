# -*- coding: utf-8 -*-
from odoo import http

# class ThemeMagazine(http.Controller):
#     @http.route('/theme_magazine/theme_magazine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/theme_magazine/theme_magazine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('theme_magazine.listing', {
#             'root': '/theme_magazine/theme_magazine',
#             'objects': http.request.env['theme_magazine.theme_magazine'].search([]),
#         })

#     @http.route('/theme_magazine/theme_magazine/objects/<model("theme_magazine.theme_magazine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('theme_magazine.object', {
#             'object': obj
#         })