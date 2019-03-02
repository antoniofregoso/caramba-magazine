# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

IMG_STYLES = [('ic_none', 'None'), 
              ('ic_bw', 'Black & Wite'), 
              ('ic_opacity', 'Opacity'), 
              ('ic_blur', 'Blur'), 
              ('ic_sepia', 'Sepia'), 
              ('ic_zoom', 'Zoom')]

IMG_OVER_STYLES = [('ic_hnone', 'None'), 
              ('ic_hbw', 'Black & Wite'), 
              ('ic_hopacity', 'Opacity'), 
              ('ic_hblur', 'Blur'), 
              ('ic_hsepia', 'Sepia'), 
              ('ic_hzoom', 'Zoom'),
              ('ic_hzoom_c', 'Zoom Clean')]



class Website(models.Model):
    _inherit = "website" 
    
    primary_ribbon = fields.Char('Ribbon 1', size=7, default="Primary")
    success_ribbon= fields.Char('Ribbon 2', size=7, default="Success")
    info_ribbon = fields.Char('Ribbon 3', size=7, default="Info")
    warning_ribbon = fields.Char('Ribbon 4', size=7, default="Warning")
    danger_ribbon = fields.Char('Ribbon 5', size=7, default="Danger")
    style = fields.Selection(IMG_STYLES, default="ic_none")
    over_style = fields.Selection(IMG_OVER_STYLES, default="ic_hnone")
    frosted_glass = fields.Boolean('Frosted Glass', default=True)
    author = fields.Boolean('Author', default=True)
    ppg = fields.Integer("Posts per Page", help="Post shown by page", default=20)
    ppr = fields.Selection([(2,'2'),(3,'3'),(4,'4')], help="Post shown by row", default=4)
    pagination = fields.Boolean('Pagination', default=False)
    opinion = fields.Boolean('Opinion', defaut=False)
    carousel = fields.Boolean('Carousel', default=False)
    carousel_size = fields.Integer('Carousels Size', default=10)
    
    @api.one
    def get_category_carousels(self):
        categories = self.env['blog.category'].search([('blog_id','=', self.search_blog_id.id),('in_cover', '=', True)])
        carousels = {}
        if len(categories) > 0:
            for category in categories:
                items = {}
                items['name'] = category.name
                items['color'] = category.color
                posts=[]
                i = 0
                limit = self.carousel_size 
                for article in category.all_post_ids:
                    post = {}
                    post['name'] = article.name
                    post['image'] = '/website_blog/static/src/img/bp_sld_' + str(article.id) +  '.jpg'
                    post['url'] = "/blog/%s/post/%s" % (slug(article.blog_id), slug(article))
                    post['cover'] = article.get_cover()
                    post['published'] = datetime.strptime(article.published_date, '%Y-%m-%d %H:%M:%S').strftime('%B %d %Y %H:%M hrs.')
                    posts.append(post)
                    i += 1
                    if i == limit:
                        break
                items['posts'] = posts
                carousels[category.order] = items
                sorted_carousels = {k: carousels[k] for k in sorted(carousels)}
        else:
            sorted_carousels = None        
        return sorted_carousels
    
    @api.one
    def get_opinion(self):
        params = self.env['blog.category'].search([('opinion_section', '=', True)])
        if len(params)>0:
            sql_query = """SELECT author_id,  MAX(id) AS id,  MAX(published_date) AS last
                            FROM blog_post
                            WHERE website_category_id = %s AND author_id IN (SELECT DISTINCT  author_id   FROM blog_post WHERE  published_date >=  NOW() - INTERVAL '30 DAY') AND published_date >=  NOW() - INTERVAL '30 DAY'
                            GROUP BY author_id ORDER BY last DESC"""
            self.env.cr.execute(sql_query, [params[0].id])
            posts = self.env.cr.fetchall()
            posts_ids = []
            for post in posts:
                posts_ids.append(post[1])         
            items = self.env['blog.post'].sudo().browse(posts_ids) 
            res = []
            for article in items:
                post = {}
                post['name'] = article.name
                post['subtitle'] = article.subtitle
                post['url'] = "/blog/%s/post/%s" % (slug(article.blog_id), slug(article))
                post['published'] = datetime.strptime(article.published_date, '%Y-%m-%d %H:%M:%S').strftime('%B %d %Y %H:%M hrs.')
                post['author'] = article.author_id.name
                post['author_url'] = "/blog/%s/author/%s" % (slug(article.blog_id), slug(article.author_id))
                post['avatar'] = article.author_id.image
                res.append(post)
                return res    
            else:
                res = False
            
        
    

            
        
    
    