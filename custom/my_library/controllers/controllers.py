# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/myLibrary(http.Controller):
#     @http.route('/custom/my_library/custom/my_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/my_library/custom/my_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/my_library.listing', {
#             'root': '/custom/my_library/custom/my_library',
#             'objects': http.request.env['custom/my_library.custom/my_library'].search([]),
#         })

#     @http.route('/custom/my_library/custom/my_library/objects/<model("custom/my_library.custom/my_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/my_library.object', {
#             'object': obj
#         })
