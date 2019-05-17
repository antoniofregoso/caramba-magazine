# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    primary_ribbon = fields.Char('Primary Ribbon', related='website_id.primary_ribbon')
    success_ribbon = fields.Char('Success Ribbon', related='website_id.success_ribbon')
    info_ribbon= fields.Char('Info Ribbon', related='website_id.info_ribbon')
    warning_ribbon = fields.Char('Warning Ribbon', related='website_id.warning_ribbon')
    danger_ribbon = fields.Char('Danger Ribbon', related='website_id.danger_ribbon')
    

        
    
