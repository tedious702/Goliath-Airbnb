from odoo import models, fields, api


class AirbnbProperty(models.Model):
    _name = 'goliath.property'
    _description = 'Airbnb Property'
    _order = 'name'

    name = fields.Char(string='Property Name', required=True)
    address = fields.Char(string='Address')
    active = fields.Boolean(string='Active', default=True)
    supply_ids = fields.One2many('goliath.supply.item', 'property_id', string='Supplies')
    supply_count = fields.Integer(string='Supplies', compute='_compute_counts')
    low_count = fields.Integer(string='Low Stock', compute='_compute_counts')

    @api.depends('supply_ids.is_low')
    def _compute_counts(self):
        for rec in self:
            rec.supply_count = len(rec.supply_ids)
            rec.low_count = len(rec.supply_ids.filtered(lambda s: s.is_low))
