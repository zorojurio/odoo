# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Hospital Description Summary
        """,

    'description': """
        Long description of module's purpose
    """,
    'sequence': -100,  # this app will be given higher priority
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/website_form.xml',
        'views/patient.xml',
        'views/sale.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True
}
