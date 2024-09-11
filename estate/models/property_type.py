from odoo import models, fields

class PropertyType(models.Model):
    _name = "property_type"

    name = fields.Char(string="Type",required=True)
    