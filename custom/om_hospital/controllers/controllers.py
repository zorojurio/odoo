# -*- coding: utf-8 -*-
from odoo import http


class Hospital(http.Controller):
    @http.route('/patient_webform', type="http", auth='public', website=True)
    def patient_webform(self, **kw):
        return http.request.render('om_hospital.create_patient', {})

# class Custom/omHospital(http.Controller):
#     @http.route('/custom/om_hospital/custom/om_hospital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/om_hospital/custom/om_hospital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/om_hospital.listing', {
#             'root': '/custom/om_hospital/custom/om_hospital',
#             'objects': http.request.env['custom/om_hospital.custom/om_hospital'].search([]),
#         })

#     @http.route('/custom/om_hospital/custom/om_hospital/objects/<model("custom/om_hospital.custom/om_hospital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/om_hospital.object', {
#             'object': obj
#         })
