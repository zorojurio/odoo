# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Book(http.Controller):
    @http.route('/library/books/', auth='public', website=True)
    def book_list(self, **kw):
        books = request.env['library.book'].sudo().search([])
        print('printing books----------------------------', books)
        for book in books:
            print('-----------printing books -----------------', book.name)
        return request.render('my_library.books_list_page', {
            'books': books
        })

    @http.route('/books/create/', type="http", website=True, auth='public')
    def book_webform(self, **kw):
        return request.render('my_library.create_book', {})

    @http.route('/books/create/action', type="http", website=True, auth='public')
    def library_book_create(self, **kw):
        print('------------print POST data', kw)
        request.env['library.book'].sudo().create(kw)
        books = request.env['library.book'].sudo().search([])
        print('printing books----------------------------', books)
        return request.render('my_library.books_list_page', {
            'books': books
        })
        # return request.render('my_library.book_creation_redirect', {})

# class CreateBook(http.Controller):
#     @http.route('/book/webform/',  website=True, auth='public')
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
