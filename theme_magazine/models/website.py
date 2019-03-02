# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields


class Website(models.Model):
    _inherit = 'website'

    theme_magazine_id = fields.Many2one(
        comodel_name='theme.magazine'
    )

