from odoo import models, fields, api
from odoo.exceptions import UserError

class PropertyOffer(models.Model):
    _name = "property_offer"
    
    selling_price = fields.Float(string="Price")

    status = fields.Selection([('offer_accepted','Offer Accepted'),('offer_refused','Offer Refused')],string="Status",copy=False)
    
    property_id = fields.Many2one("estate_property",string="Property", required=True)
    buyer_id = fields.Many2one("res.partner",string="Buyer", required=True)

    validity = fields.Integer(string="Validity (Days)", default=7)
    date_deadline = fields.Date(compute="_compute_deadline_date", inverse="_inverse_deadline_date")

    @api.depends('validity')
    def _compute_deadline_date(self):
        for record in self:
            if record.create_date:
                record.date_deadline = fields.Date.add(record.create_date,days=record.validity)
            else:
                record.date_deadline = fields.Date.add(fields.Date.today(),days=record.validity)
    
    def _inverse_deadline_date(self):
        for record in self:
            record.validity = (record.date_deadline-fields.Date.to_date(record.create_date)).days

    def property_offer_state_change(self):
        if self.env.context.get('type')=='offer_accepted':
            for offer in self.property_id.property_offers_ids:
                if offer.status=='offer_accepted':
                    raise UserError('There is an accepted offer')
            self.status = 'offer_accepted'
            self.property_id.buyer_id = self.buyer_id
            self.property_id.selling_price = self.selling_price
        elif self.env.context.get('type')=='offer_refused':
            self.status = 'offer_refused'
            self.property_id.buyer_id = ""
            self.property_id.selling_price = 0