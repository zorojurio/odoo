# -*- coding: utf-8 -*-
from odoo import http


class LibraryBookView(http.Controller):
    @http.route('/library/books/', auth='public', website=True)
    def patient_webform(self, **kw):
        return http.request.render('my_library.create_patient', {})


#     @http.route('/custom/my_library/custom/my_library/objects/<model("custom/my_library.custom/my_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/my_library.object', {
#             'object': obj
#         })
