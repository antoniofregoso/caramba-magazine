# -*- coding: utf-8 -*-
{
    'name': "Theme Magazine",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    

    'author': "Antonio Fregoso",
    'website': "http://antoniofregoso.blog",


    'category': 'Theme',
    'version': '11.0.0.0.0',

    'depends': ['website_magazine'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/theme_magazine_data.xml',
        'data/website_data.xml',
        'data/theme_magazine_font_data.xml',
        'views/magazine_templates.xml',
        'views/website_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}