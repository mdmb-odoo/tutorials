from odoo import models, fields

class PropertyType(models.Model):
    _name = "property_tag"
    _order = "name"

    name = fields.Char(string="Tag",required=True)
    color = fields.Integer(string="Color")
    _sql_constraints = [
        ('check_unique','UNIQUE(name)','Tag must be unique')
    ]
    