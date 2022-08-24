# -*- coding: utf-8 -*-
{
    'name': "Employee Contract Lines",
    'summary': """ For allowances and deductions per employee regarding strcuture """,
    'author': "MohammedSaeb@IntegratedPath",
    'website': "https://www.int-path.com",
    'category': 'HR',
    'version': '13.1',
    'depends': ['base', 'hr', 'hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_views.xml',
        'views/hr_payslip_views.xml',
    ],

    'license': 'Other proprietary',

}
