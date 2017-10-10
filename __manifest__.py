# -*- coding: utf-8 -*-
{
    'name': "Nutrição e Qualidade",

    'summary': """
        Módulo Qualidade e Nutrição""",

    'description': """
        Módulo para controle de qualidade e Gerenciamento de estabelecimentos por profissionais
        de Nutrição
    """,

    'author': "Diogo Berti",
    #'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/nutri_base_view.xml',
        'views/nutri_visit_view.xml',
        'views/res_partner_view.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}