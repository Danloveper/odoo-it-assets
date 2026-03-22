# -*- coding: utf-8 -*-
{
    'name': "IT Assets",

    'summary': "Request IT assets",

    'description': """
    The following module allows you to manage a company's technological
    assets through an internal form and from the website,
    in addition to providing a dynamic report of the request.
    """,

    'author': "William Daniel Vargas Acevedo",
    'website': "https://www.yourcompany.com",


    'category': 'Project',
    'version': '0.1',
    'license': 'LGPL-3',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/asset_request_views.xml',
        'views/asset_request_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

