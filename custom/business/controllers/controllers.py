# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/business(http.Controller):
#     @http.route('/custom/business/custom/business/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/business/custom/business/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/business.listing', {
#             'root': '/custom/business/custom/business',
#             'objects': http.request.env['custom/business.custom/business'].search([]),
#         })

#     @http.route('/custom/business/custom/business/objects/<model("custom/business.custom/business"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/business.object', {
#             'object': obj
#         })
