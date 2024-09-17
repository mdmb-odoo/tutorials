from odoo import fields,models

class Users(models.Model):
    _inherit = "res.users"
    
    property_ids = fields.One2many('estate_property','salesman_id',string="Properties", domain= lambda self : [('state', 'in', ['new','offer_recieved'])]) 