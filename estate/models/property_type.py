from odoo import models, fields, api
from odoo.exceptions import ValidationError
class PropertyType(models.Model):
    _name = "property_type"
    _order = "sequence, name"

    name = fields.Char(string="Type",required=True)
    property_ids = fields.One2many("estate_property","property_type_id",string="Properties")
    property_offer_ids = fields.One2many(related="property_ids.property_offers_ids", string="Offers IDs")

    offer_count = fields.Integer(compute="_compute_offers", string="Offers")

    sequence = fields.Integer(string='Sequence', default=1)

    _sql_constraints = [
        ('check_unique','UNIQUE(name)','Type must be unique')
    ]

    @api.depends('property_offer_ids')
    def _compute_offers(self):
        for record in self:
            record.offer_count = len(record.mapped('property_offer_ids'))

    @api.depends('offer_count')
    def show_offers(self):
        action = {
            'name': ('Property Type Offers'),
            'type': 'ir.actions.act_window',
            'res_model': 'property_offer'
        }
        offer_ids = self.property_offer_ids
        action['view_mode'] = 'tree,form'
        action['domain'] = [('id', 'in', offer_ids.mapped('id'))]
        return action
    # @api.constrains('name')
    # def check_unique(self):
    #     self.env.cr.execute(" SELECT CASE " \
    #                         "WHEN NOT EXISTS ( "\
    #                                 "SELECT 1 "\
    #                                 "FROM property_type "\
    #                                 "WHERE LOWER(name) = LOWER(%s) "\
    #                             ") THEN TRUE "\
    #                             "ELSE FALSE "\
    #                         "END AS name_does_not_exist;"\
    #                         ,[self.name])
    #     if not self.env.cr.fetchall()[0][0]:
    #         raise ValidationError("Name already exists")
        