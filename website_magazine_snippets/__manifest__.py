# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#

{
    'name': "Website Magazine Snippets",

    'summary': "Snippets for magazine and digital newspapers.",

    'description': """
       
    """,

    'author': "Antonio Fregoso",
    'website': "http://www.antoniofregoso.blog",

    'category': 'Website',
    'version': '12.0.0.0.0',

    'depends': ['website_blog_category_and_author'],

    'data': [
        # 'security/ir.model.access.csv',
       
        'views/snippets.xml',
        'views/templates.xml',
    ],
   
    'demo': [
        'demo/demo.xml',
    ],
}