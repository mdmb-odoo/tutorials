from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class PropertyOffer(models.Model):
    _name = "property_offer"
    _order = "selling_price desc"
    selling_price = fields.Float(string="Price")

    status = fields.Selection([('offer_accepted','Offer Accepted'),('offer_refused','Offer Refused')],string="Status",copy=False,readonly=True)
    
    property_id = fields.Many2one("estate_property",string="Property", required=True)
    property_type_id = fields.Many2one(related="property_id.property_type_id", string="Property Type")
    buyer_id = fields.Many2one("res.partner",string="Buyer", required=True)

    validity = fields.Integer(string="Validity (Days)", default=7)
    date_deadline = fields.Date(compute="_compute_deadline_date", inverse="_inverse_deadline_date")



    _sql_constraints = [
        ('check_positive_ints','CHECK(selling_price>0)','Number must be greater than 0')
    ]

    @api.depends('validity')
    def _compute_deadline_date(self):
        for record in self:
            if record.create_date:
                record.date_deadline = fields.Date.add(record.create_date,days=record.validity)
            else:
                record.date_deadline = fields.Date.add(fields.Date.today(),days=record.validity)
    
    @api.model
    def create(self, vals):
        props = self.env['estate_property'].browse(vals['property_id'])
        if len(props.property_offers_ids)==0:
            props.state = 'offer_recieved'
        else:
            for offer in props.property_offers_ids:
                if vals['selling_price'] < offer.selling_price:
                    raise ValidationError('Selling price cannot be less than an existing offer')
        return super(PropertyOffer, self).create(vals)


    def _inverse_deadline_date(self):
        for record in self:
            record.validity = (record.date_deadline-fields.Date.to_date(record.create_date)).days
    
    def property_offer_state_change(self):
        if self.env.context.get('type')=='offer_accepted':
            if len(self.property_id.property_offers_ids.filtered(lambda r: r.status == 'offer_accepted')):
                raise UserError('There is an accepted offer')
            self.status = 'offer_accepted'
            self.property_id.buyer_id = self.buyer_id
            self.property_id.selling_price = self.selling_price
            if self.status == 'offer_accepted' and self.property_id.state not in ['sold','canceled']:
                self.property_id.state = 'offer_accepted'
        elif self.env.context.get('type')=='offer_refused':
            if self.status == 'offer_accepted' and self.property_id.state not in ['sold','canceled']:
                self.property_id.state = 'offer_recieved'
            self.status = 'offer_refused'
            self.property_id.buyer_id = ""
            self.property_id.selling_price = 0

    