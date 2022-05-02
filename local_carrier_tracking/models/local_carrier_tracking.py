# -*- coding: utf-8 -*-

from odoo import models, fields, api


class local_carrier_tracking(models.Model):
    _name = 'stock.picking'
    _description = 'Local Carrier Tracking'
    _inherit = 'stock.picking'
    
    local_carrier = fields.Char('Local carrier')
    tracking_url = fields.Char('Tracking url')