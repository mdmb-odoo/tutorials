from odoo import models, fields, api, tools
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_is_zero, float_compare

class Property(models.Model):
    _name = "estate_property"
    _order = "id desc"

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

    _sql_constraints = [
        ('check_positive_ints','CHECK(expected_price >= 0 AND selling_price>=0)','Number must be positive')
    ]

    @api.depends('living_area','garden_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('property_offers_ids.selling_price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.property_offers_ids.mapped("selling_price"),default=0)

    @api.onchange('property_offers_ids')
    def _offer_recieve(self):
        if self.state=='new' and len(self.property_offers_ids)>0:
            self.state = 'offer_recieved'
        elif self.state not in ['sold','canceled'] and (len(self.property_offers_ids)==0 or len(self.property_offers_ids.filtered(lambda r: r.status == 'offer_accepted'))==0):
            if len(self.property_offers_ids)==0:
                self.state = 'new'
            else:
                self.state = 'offer_recieved'
        


    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = ""

    @api.constrains('selling_price')
    def _check_selling_price(self):
        if float_compare(self.selling_price, self.expected_price,4)==-1:
            if self.selling_price / self.expected_price < 0.9 and self.env.context.get('type')=="offer_accepted":
                raise ValidationError("Selling price is low")
            
    @api.constrains('expected_price')
    # @api.onchange('expected_price')
    def _check_exepected_price(self):
        if not float_is_zero(self.selling_price, 4):
            if float_compare(self.selling_price, self.expected_price,4)==-1:
                if self.selling_price / self.expected_price < 0.9:
                    self.property_offers_ids.filtered(lambda r: r.status == 'offer_accepted').status='offer_refused'
                    self.buyer_id = ""
                    self.selling_price = 0
                    # return {
                    #             'warning': {'title': "Warning", 'message': "What is this?", 'type': 'notification'},
                    #         }         

    def property_state_change(self):
        if self.env.context.get('type')=='sold':
            if self.state in ['canceled','sold']:
                raise UserError("Canceled or Sold house cannot be sold again")
            self.state = 'sold'
        elif self.env.context.get('type')=='cancel':
            if self.state in ['canceled','sold']:
                raise UserError("Canceled or Sold house cannot be canceled again")
            self.state = 'canceled'

        
# return {
#         'type': 'ir.actions.client',
#         'tag': 'display_notification',
#         'params': {
#             'title': _('Success'),
#             'message': _('Your signature request has been sent.'),
#             'sticky': False,
#         }
#     }


