# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api

class ThemeMagazineFont(models.Model):
    _name = 'theme.magazine.font'
    
    name = fields.Char('Name', required=True)
    family = fields.Selection([('serif','Serif'),('sans-serif','Sans Serif'),('display','Display'),('handwriting','Handwriting'),('monospace','Monospace')], default="sans_serif")
    paring = fields.Char('Paring')

class ThemeMagazine(models.Model):
    _name = 'theme.magazine'
    
    color_alpha = fields.Char(default='#1CC1A9')
    color_beta = fields.Char(default='#875A7B')
    color_gamma = fields.Char(default='#BA3C3D')
    color_delta = fields.Char(default='#0D6759')
    color_epsilon = fields.Char(default='#0B2E59')
    
    gray_darker = fields.Char(default="#222")
    gray_dark = fields.Char(default="#7b8a8b")
    gray = fields.Char(default="#95a5a6")
    gray_light = fields.Char(default="#b4bcc2")
    gray_lighter = fields.Char(default="#ecf0f1")
    
    brand_default = fields.Char(default="#95a5a6")
    brand_primary = fields.Char(default="#2C3E50")
    brand_success = fields.Char(default="#18BC9C")
    brand_info = fields.Char(default="#3498DB")
    brand_warning = fields.Char(default="#F39C12")
    brand_danger = fields.Char(default="#E74C3C")
    brand_color = fields.Char(default="#FFF")
    
    header_bg = fields.Char(default="#FFF")
    body_bg = fields.Char(default="#FFF")
    footer_bg = fields.Char(default='#F8F8F8')
    text_color = fields.Char(default="#2C3E50")
    footer_text_color = fields.Char(default="#2C3E50")
    link_color = fields.Char(default="#18BC9C")
    footer_link_color = fields.Char(default="#18BC9C")
    
    
    navbar_height = fields.Char(default="60px")
    navbar_default_color = fields.Char(default="#777")
    navbar_default_bg = fields.Char(default="#2C3E50")
    navbar_default_border = fields.Char(default="transparent")
    navbar_default_border_width =  fields.Char(default="0px")
    
    breadcrumb_bg = fields.Char(default="#ecf0f1")
    breadcrumb_color = fields.Char(default="#ccc")
    breadcrumb_active_color = fields.Char(default="#95a5a6")
    breadcrumb_separator = fields.Char(default="/")
    
    font_headers = fields.Many2one('theme.magazine.font', string="Font")
    font_base = fields.Many2one('theme.magazine.font', string="Font")
    font_monospace = fields.Many2one('theme.magazine.font', string="Font")
    
    css = fields.Text()
    
    @classmethod
    def _add_shades(cls, color):
        setattr(cls, 'amount_%s_lighter' % color, fields.Integer(
            default=10
        ))

        setattr(cls, 'amount_%s_light' % color, fields.Integer(
            default=5
        ))

        setattr(cls, 'amount_%s_dark' % color, fields.Integer(
            default=5
        ))

        setattr(cls, 'amount_%s_darker' % color, fields.Integer(
            default=10
        ))
    
ThemeMagazine._add_shades('alpha')
ThemeMagazine._add_shades('beta')
ThemeMagazine._add_shades('gamma')
ThemeMagazine._add_shades('delta')
ThemeMagazine._add_shades('epsilon')



    
    
    