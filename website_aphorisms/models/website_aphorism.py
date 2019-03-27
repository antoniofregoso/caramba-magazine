# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api

class WebsiteAphorismAuthor(models.Model):
    _name = 'website.aphorism.author'
    _description = 'Website Aphorism Author'
    _order = 'name'
    
    name = fields.Char(required=True, translate=True)
    
    
class WebsiteAphorism(models.Model):
    _name = 'website.aphorism'
    _description ='Website Aphorism'
    
    name = fields.Char(required=True, translate=True)
    aphorism = fields.Html('Aphorism', required=True, translate=True)    
    source = fields.Char( translate=True)
    author_id = fields.Many2one('website.aphorism.author', string='Author',  required=True)
    

        
        
    