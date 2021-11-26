# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request




class Book(http.Controller):
    @http.route('/books/<model("library.book"):book>/', auth='public', website=True)
    def book_detail(self, book):
        return http.request.render('my_library.book_detail', {
            'book': book
        })
    # /books/edit/{{ slug(book) }}/action/
    @http.route('/books/edit/<model("library.book"):book>/', auth='public', website=True)
    def book_edit(self, book):
        print('==============book=============', book[0])
        return http.request.render('my_library.edit_book', {
            'book': book,
            'id': book.id,
            'name': book.name,
            'age': book.age
        })
        
    @http.route('/books/edit/action/', auth='public', website=True)
    def book_edit_action(self, **kw):
        print('==============book-update-data=============', kw)
        book = request.env['library.book'].browse(kw.get('id'))
        name = kw.get('name')
        age = kw.get('age')
        book.write({'name': name , 'age': age})
        print("+++++++++++++++++book get+++++++++++++++++++++", book)
        return request.render('my_library.edit_book_redirect', {})

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
        # books = request.env['library.book'].sudo().search([])
        # print('printing books----------------------------', books)
        # return request.render('my_library.books_list_page', {
        #     'books': books
        # })
        return request.render('my_library.book_creation_redirect', {})
