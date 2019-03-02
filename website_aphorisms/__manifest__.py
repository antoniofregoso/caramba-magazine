# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': "Quotes and Aphorisms",

    'summary': """
        Generate citations and aphorisms in a random way to be used in the snippets aphorism or to be called by other modules.""",

    'description': """
       
    """,

    'author': "Antonio Fregoso",
    'website': "http://antoniofregoso.blog",

   
    'category': 'website',
    'version': '11.0.0.0.1',

    'depends': ['website_blog'],

    'data': [
        'security/ir.model.access.csv',
	'demo/demo.xml',
        'views/website_aphorisms_views.xml',
        'views/snippets.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    
    'license': 'AGPL-3',
}
