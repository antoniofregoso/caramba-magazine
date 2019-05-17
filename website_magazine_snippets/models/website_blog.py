# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.addons.http_routing.models.ir_http import slug

class BlogPostStyle(models.Model):
    _name = "blog.post.style"

    name = fields.Char(string='Style Name', required=True)
    html_class = fields.Char(string='HTML Classes')
    
    
class BlogPost(models.Model):
    _inherit = 'blog.post'  
    
    website_size_x = fields.Integer('Size X', default=1)
    website_size_y = fields.Integer('Size Y', default=1)
    website_style_ids = fields.Many2many('blog.post.style', string='Styles')
    website_sequence = fields.Integer('Website Sequence', help="Determine the display order in the snippets",
                                      default=lambda self: self._default_website_sequence())    
    
    def _default_website_sequence(self):
        #self._cr.execute("SELECT MIN(website_sequence) FROM %s" % self._table)
        #min_sequence = self._cr.fetchone()[0]
        #return min_sequence and min_sequence - 1 or 10
        return 100
    
    def set_sequence_top(self):
        self.website_sequence = self.sudo().search([], order='website_sequence desc', limit=1).website_sequence + 1
    
    def set_sequence_bottom(self):
        self.website_sequence = self.sudo().search([], order='website_sequence', limit=1).website_sequence - 1
        
    def set_sequence_up(self):
        previous_blog_post = self.sudo().search(
            [('website_sequence', '>', self.website_sequence), ('website_sequence', '=', self.website_sequence)],
            order='website_sequence', limit=1)
        if previous_blog_post:
            previous_blog_post.website_sequence, self.website_sequence = self.website_sequence, previous_blog_post.website_sequence
        else:
            self.set_sequence_top()  
            
    def set_sequence_down(self):
        next_blog_post = self.search([('website_sequence', '<', self.website_sequence), ('website_sequence', '=', self.website_sequence)], order='website_sequence desc', limit=1)
        if next_blog_post:
            next_blog_post.website_sequence, self.website_sequence = self.website_sequence, next_blog_post.website_sequence
        else:
            return self.set_sequence_bottom()  
        
    def set_sequence_reset(self):
        self.website_sequence = self._default_website_sequence() 
        
    def get_author(self):
        return self.sudo().author_id.name
    
    def get_author_slug(self):
        slug = self.sudo().author_id.name.strip().lower().replace(' ','-') + '-' + str(self.sudo().author_id.id)
        return slug
        
    
class BlogCategory(models.Model):
    _inherit = 'blog.category'
    
    in_cover = fields.Boolean(string='In Cover', help='Show on the cover', default=False)
    order = fields.Integer(string='Order', help='Order of appearance on the cover' )
    opinion_section = fields.Boolean(default=False, help="")    
    