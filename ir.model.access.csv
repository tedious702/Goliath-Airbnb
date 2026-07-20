from odoo import models, fields


class PropertyListing(models.Model):
    _name = 'goliath.airbnb.listing'
    _description = 'Goliath Airbnb Property Listing'

    name = fields.Char(string='Listing Name', required=True)
    address = fields.Char(string='Address')
    nightly_rate = fields.Float(string='Nightly Rate')
    bedrooms = fields.Integer(string='Bedrooms')
    active = fields.Boolean(string='Active', default=True)
    notes = fields.Text(string='Notes')
