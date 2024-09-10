from odoo import models, fields

class Property(models.Model):
    _name = "estate_property"

    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    
    date_availability = fields.Date(string="Available Date")
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price = fields.Float(string="Selling Price")

    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")

    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")

    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('North','North'),('South','South'),('East','East'),('West','West')])
