# -*- coding: utf-8 -*-

from odoo import models, fields

    
class OpenAcademySession(models.Model):
    _name = 'openacademy.session'
    _description =  'OpenAcademy Sessions'
    _order = 'id, expire_date desc'
    
    name = fields.Char(string='Name', required=True, 
                        index=True, help='Enter your course title on this field.')
    active = fields.Boolean(string='Active', default=True)
    avail_seat_per = fields.Float(string='Avaliable Seats (%)')
    max_seats = fields.Integer(string='Maximum Seats')
    
    
    insructor_id = fields.Many2one(comodel_name='res.partner', required=True,
                        string='Instructor', ondelete='restrict', copy=False)
    
    tag_ids = fields.Many2many(comodel_name='openacademy.tags', relation='rel_course_tags',
                            column1='course_id', column2='tag_id', string='Tags')