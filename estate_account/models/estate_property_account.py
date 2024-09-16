from odoo import models, Command

class PropertyAccounting(models.Model):
    _inherit = "estate_property"

    def property_state_change(self):
        if self.env.context.get('type')=='sold':
            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': self.buyer_id.id,
                'invoice_origin': self.name,
                'invoice_line_ids': [
                    Command.create({
                        "name": "Initial Payment",
                        "quantity": 1,
                        "price_unit":self.selling_price*0.06
                    }),
                    Command.create({
                        "name": "Admin Fees",
                        "quantity": 1,
                        "price_unit":100
                    })
                ]
            }
            self.env["account.move"].create(invoice_vals)
        return super().property_state_change()
    

    