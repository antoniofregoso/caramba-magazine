# # -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).#
from odoo import http, tools, _    
from odoo.http import request
from odoo.addons.website.controllers.main import Website

class Website(Website):
    
    
    def _get_search_domain(self, search):
        domain = [("website_published","=",True)]
        if search:
            for srch in search.split(" "):
                domain += [
                    '|', '|', '|', ('name', 'ilike', srch), ('subtitle', 'ilike', srch),
                    ('content', 'ilike', srch), ('tag_ids.name', 'ilike', srch)]
        return domain
    
    @http.route(['/change_styles'], type='json', auth="public")
    def change_styles(self, id, style_id):
        blog_post = request.env['blog.post'].browse(id)
        remove = []
        active = False
        style_id = int(style_id)
        for style in blog_post.website_style_ids:
            if style.id == style_id:
                remove.append(style.id)
                active = True
                break
        style = request.env['blog.post.style'].browse(style_id)
        if remove:
            blog_post.write({'website_style_ids': [(3, rid) for rid in remove]})
        if not active:
            blog_post.write({'website_style_ids': [(4, style.id)]})
        return not active

    @http.route(['/change_sequence'], type='json', auth="public")
    def change_sequence(self, id, sequence):
        blog_post = request.env['blog.post'].browse(id)
        if sequence == "top":
            blog_post.set_sequence_top()
        elif sequence == "bottom":
            blog_post.set_sequence_bottom()
        elif sequence == "up":
            blog_post.set_sequence_up()
        elif sequence == "down":
            blog_post.set_sequence_down()
        elif sequence == "reset":
            blog_post.set_sequence_reset()

    @http.route(['/change_size'], type='json', auth="public")
    def change_size(self, id, x, y):
        blog_post = request.env['blog.post'].browse(id)
        return blog_post.write({'website_size_x': x, 'website_size_y': y})
       