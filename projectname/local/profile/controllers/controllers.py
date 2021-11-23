# -*- coding: utf-8 -*-
# from odoo import http


# class Profile(http.Controller):
#     @http.route('/profile/profile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/profile/profile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('profile.listing', {
#             'root': '/profile/profile',
#             'objects': http.request.env['profile.profile'].search([]),
#         })

#     @http.route('/profile/profile/objects/<model("profile.profile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('profile.object', {
#             'object': obj
#         })
