from odoo import models, fields

class LimsOrder(models.Model):
    _inherit = 'lims.order'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order', index=True)
    sale_order_line_id = fields.Many2one('sale.order.line', string='Sale Order Line', index=True)
    sale_origin = fields.Char(string='Sale Origin', help='Original sale reference')
