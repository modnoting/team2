# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HolidaysTypeInherit(models.Model):
    _inherit = "hr.leave.type"

    is_unpaid = fields.Boolean(string='Is Unpaid')
