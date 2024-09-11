from odoo import models, fields

class PropertyOffer(models.Model):
    _name = "property_offer"
    
    selling_price = fields.Float(string="Price")

    status = fields.Selection([('offer_accepted','Offer Accepted'),('offer_refused','Offer Refused')],string="Status",copy=False)
    
    property_id = fields.Many2one("estate_property",string="Property", required=True)
    buyer_id = fields.Many2one("res.partner",string="Buyer", required=True)