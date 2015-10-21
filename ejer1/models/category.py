# -*- coding: utf-8 -*-

from openerp import models, fields

class Category(models.Model):
    _name = 'openacademy.course.category'

    code = fields.Char()
    name = fields.Char()
    description = fields.Text()