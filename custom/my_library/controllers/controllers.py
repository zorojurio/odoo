# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Book(http.Controller):
    @http.route('/library/books/', auth='public', website=True)
    def patient_webform(self, **kw):
        books = request.env['library.book'].sudo().search([])
        print('printing books----------------------------', books)
        for book in books:
            print('-----------printing books -----------------', book.name)
        return request.render('my_library.books_list_page', {
            'books': books
        })


# class Hospital(http.Controller):
#     @http.route('/patient/webform/',  website=True, auth='public')
#     def patient_webform(self, **kw):
#         patients = request.env['hosptial.patient'].sudo().search([])
#         print('patients----------', patients)
#         return request.render('om_hospital.patients_page', {
#             'patients': patients
#         })

#     @http.route('/custom/my_library/custom/my_library/objects/<model("custom/my_library.custom/my_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/my_library.object', {
#             'object': obj
#         })
