from odoo import models, fields

class PropertyType(models.Model):
    _name = "property_tag"

    name = fields.Char(string="Tag",required=True)

    _sql_constraints = [
        ('check_unique','UNIQUE(name)','Tag must be unique')
    ]
    