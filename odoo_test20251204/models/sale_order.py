from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_ref = fields.Char(string="Customer Remark")
