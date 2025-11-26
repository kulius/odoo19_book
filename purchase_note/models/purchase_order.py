# -*- coding: utf-8 -*-
from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchase_note = fields.Text(string='採購備註')
