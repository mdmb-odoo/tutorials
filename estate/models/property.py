from odoo import models, fields

class Property(models.Model):
    _name = "estate_property"
    _log_access = False


    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    
    date_availability = fields.Date(string="Available Date",copy=False, default=fields.Date.add(fields.Date.today(),months=3))
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price = fields.Float(string="Selling Price",readonly=True,copy=False)

    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")

    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")

    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')],string="Garden Orientation")

    state = fields.Selection([('new','New'),('offer_recieved','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],string="State",default='new',copy=False,required=True)
    active = fields.Boolean(string="Active", default=True)