# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api
import random
from random import randrange


class Website(models.Model):
    _inherit = "website" 
    
    @api.one
    def get_aphorism(self):
        aphorisms = self.env['website.aphorism'].search([])
        i=  random.randint(0, len(aphorisms) -1)
        raffle = aphorisms[i]
        return {'aphorism':raffle.aphorism, 'author':raffle.author_id.name, 'source':raffle.source}
        