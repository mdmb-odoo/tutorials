from odoo import models, fields, api
from odoo.exceptions import UserError

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

    total_area = fields.Float(compute="_compute_total")
    best_price = fields.Float(compute="_compute_best_price")

    @api.depends('living_area','garden_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('property_offers_ids.selling_price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.property_offers_ids.mapped("selling_price"),default=0)

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""

    def property_state_change(self):
        if self.env.context.get('type')=='sold':
            if self.state in ['canceled','sold']:
                raise UserError("Canceled or Sold house cannot be sold again")
            self.state = 'sold'
        elif self.env.context.get('type')=='cancel':
            if self.state in ['canceled','sold']:
                raise UserError("Canceled or Sold house cannot be canceled again")
            self.state = 'canceled'

        



