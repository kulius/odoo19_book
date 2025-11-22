from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_123 = fields.Char(string='客戶備註')
