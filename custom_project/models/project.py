# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _


class CustomProject(models.Model):
    _inherit = 'project.project'

    @api.onchange('date_start', 'date')
    def _onchange_planned_date(self):
        pass
        # if not self.date and self.date_start:
        #     self.date_start = False
        # elif not self.date_start and self.date:
        #     self.date = False
