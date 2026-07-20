from odoo import models, fields, api


class ChocolateProduct(models.Model):
    _name = 'goliath.chocolate'
    _description = 'Chocolate Product Stock'
    _order = 'name'

    name = fields.Char(string='Product', required=True)
    sku = fields.Char(string='SKU')
    quantity = fields.Float(string='In Stock', default=0.0)
    unit = fields.Char(string='Unit', default='bars')
    reorder_point = fields.Float(string='Reorder At', default=0.0)
    is_low = fields.Boolean(string='Low Stock', compute='_compute_is_low', store=True)
    status = fields.Selection([('ok', 'OK'), ('low', 'Reorder')],
                              string='Status', compute='_compute_is_low', store=True)

    @api.depends('quantity', 'reorder_point')
    def _compute_is_low(self):
        for rec in self:
            low = rec.quantity <= rec.reorder_point
            rec.is_low = low
            rec.status = 'low' if low else 'ok'
