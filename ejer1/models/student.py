# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields

class Student (models.Model):
    _inherit = 'res.partner'

    student = fields.Boolean("Student", default=False)
    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions")


# EOF