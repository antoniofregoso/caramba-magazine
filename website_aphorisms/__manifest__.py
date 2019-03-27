# -*- coding: utf-8 -*-
{
    'name': "Quotes and Aphorisms",

    'summary': 'Generate citations and aphorism.',

    'description': 'Generate citations and aphorisms in a random way to be used in the snippets aphorism or to be called by other modules.',

    'author': "Antonio Fregoso",
    'website': "http://antoniofregoso.blog",


    'category': 'website',
    'version': '12.0.0.0.0',

    'depends': ['website_blog'],


    'data': [
        'security/ir.model.access.csv',
        'views/website_aphorisms_views.xml',
        'views/snippets.xml'
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    
    'license': 'AGPL-3',
}