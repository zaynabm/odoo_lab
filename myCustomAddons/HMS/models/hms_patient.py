from odoo import models, fields


class HmsPatient(models.Model):
    _name = "hms.patient"
    _description = "HMS patient"
    first_name = fields.Char()
    last_name = fields.Char()
    birth_data = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('O+','O+'),
    ('O-','O-')
    ])
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    age = fields.Integer()
