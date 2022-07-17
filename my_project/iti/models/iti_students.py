from odoo import models, fields


class Itistudents(models.Model):
    _name = "iti.student"
    _description = "desc: iti student"
    name = fields.Char()
    age = fields.Integer()
    birth_data = fields.Float()
    grnder = fields.Selection([
        ('m','male'),
        ('f','fmale')
    ])
    cv=fields.Binary()
    image=fields.Binary()
    info = fields.Text()
    accepted = fields.Boolean()
    date = fields.Datetime()
