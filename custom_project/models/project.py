# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class RegisterPayment(models.Model):
    _inherit = 'project.task'

    user_ids = fields.Many2many(
      'hr.employee',
      string = "Assignees",
    )

