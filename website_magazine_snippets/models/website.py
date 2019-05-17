# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _

class Website(models.Model):
    _inherit = "website" 
    
    primary_ribbon = fields.Char('Primary Ribbon', size=7, default="Primary")
    success_ribbon= fields.Char('Success Ribbon', size=7, default="Success")
    info_ribbon = fields.Char('Info Ribbon', size=7, default="Info")
    warning_ribbon = fields.Char('Warning Ribbon', size=7, default="Warning")
    danger_ribbon = fields.Char('Danger Ribbon', size=7, default="Danger")
    