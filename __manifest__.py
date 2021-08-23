# -*- coding: utf-8 -*-
{
    'name': "HR Customization",

    'summary': """HR Customizations for NimaForms and AL-Shiffa""",

    'author': "INTEGRATED PATH",
    'website': "https://www.int-path.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_contract', 'hr_attendance', 'hr_payroll'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_views.xml',
        'views/hr_payslip_views.xml',
    ],

}
