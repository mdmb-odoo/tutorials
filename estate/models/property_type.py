from odoo import models, fields, api
from odoo.exceptions import ValidationError
class PropertyType(models.Model):
    _name = "property_type"

    name = fields.Char(string="Type",required=True)
    property_ids = fields.One2many("estate_property","property_type_id",string="Properties")

    _sql_constraints = [
        ('check_unique','UNIQUE(name)','Type must be unique')
    ]


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
        