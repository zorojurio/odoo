from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'  # based on the name table will be created >> postgres table name >>
    _description = 'Hospital Patient'

    sale_description = fields.Char(string='Sale Description')


