# -*- coding: utf-8 -*-
{
    'name': "Microfinancing - Base",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Cuburt R. Balanon",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_setup'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/blcl.xml',
        'views/lists.xml',
        'views/system.xml',
        'views/transactions.xml',
        'views/lists/accounting.xml',
        'views/lists/loans.xml',
        'views/lists/references.xml',
        'views/lists/savings.xml',
        'views/reports/accounting.xml',
        'views/reports/daily_reports.xml',
        'views/reports/loan.xml',
        'views/reports/savings.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}