# -*- coding: utf-8 -*-

from openerp import models, fields

class Category(models.Model):
    _name = 'openacademy.course.category'

    code = fields.Char(required=True)
    name = fields.Char(required=True)
    description = fields.Text()
    
    
    _sql_constraints = [           
        ('code_unique',
         'UNIQUE(code)',
         "The code must be unique"),
                        
        ('name_unique',
         'UNIQUE(name)',
         "The name must be unique"), 
    ]
    
 