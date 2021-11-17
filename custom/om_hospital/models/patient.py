from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'  # based on the name table will be created >> postgres table name >>
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer('Age', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
