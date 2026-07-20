from odoo import models, fields, api


class SupplyItem(models.Model):
    _name = 'goliath.supply.item'
    _description = 'Airbnb Supply Item'
    _order = 'property_id, name'

    name = fields.Char(string='Item', required=True)
    property_id = fields.Many2one('goliath.property', string='Property',
                                  required=True, ondelete='cascade')
    quantity = fields.Float(string='On Hand', default=0.0)
    unit = fields.Char(string='Unit', default='units')
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
