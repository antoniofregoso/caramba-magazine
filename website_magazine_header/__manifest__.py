# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Magazine Header",

    'summary': "Header for digital magazine",


    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",


    'category': 'Website',
    'version': '11.0.0.0.1',


    'depends': ['website_blog_category_and_author', 'website_aphorisms',],


    'data': [
        # 'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/templates.xml',
    ],
    
    'license': 'AGPL-3',
}