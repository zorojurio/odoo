from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Books'
    
    
    name = fields.Char('Title', required=True)
    age = fields.Integer(string='Age')
    
