from odoo import models, fields

class Property(models.Model):
    _name = "estate_property"

    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="PostCode")
    
    date_availability = fields.Date(string="Available Date",copy=False, default=fields.Date.add(fields.Date.today(),months=3))
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price = fields.Float(string="Selling Price",readonly=True,copy=False)

    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")

    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")

    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([('north','North'),('south','South'),('east','East'),('west','West')],string="Garden Orientation")

    state = fields.Selection([('new','New'),('offer_recieved','Offer Recieved'),('offer_accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],string="State",default='new',copy=False,required=True)
    active = fields.Boolean(string="Active", default=True)

    property_type_id = fields.Many2one("property_type",string="Type")
    salesman_id = fields.Many2one("res.users",string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner",string="Buyer", copy=False)
    property_tags_ids = fields.Many2many("property_tag",string="Tags", copy=False)

    # property_offers_ids = fields.Many2one("property_offer", string="Prop-Off m2o")
    property_offers_ids = fields.One2many("property_offer","property_id", string="Property Offers", copy=False)