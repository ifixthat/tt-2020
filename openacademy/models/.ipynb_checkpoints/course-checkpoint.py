# -*- coding: utf-8 -*-

from odoo import models, fields

class OpenAcademyCourse(models.Model):
    _name = 'openacademy.course'
    _description =  'OpenAcademy Course'
    
    
    name = fields.Char(string='Course Title', required=True, 
                        index=True, help='Enter your course title on this field.')
    description = fields.Html(string='Description')
    banner = fields.Binary(string='Banner')