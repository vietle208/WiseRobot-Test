# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class CustomProject(models.Model):
    _inherit = 'project.project'

    date_start = fields.Date(string='Start Date', default=fields.Date.today)
