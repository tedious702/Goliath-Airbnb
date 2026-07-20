{
    'name': 'Goliath Airbnb & Stock',
    'version': '19.0.1.0.0',
    'summary': 'Consumables tracking for Airbnb properties and chocolate product stock',
    'description': 'Lightweight inventory tracker with two sections: Airbnb property supplies and chocolate product stock, with low-stock reorder flagging and a combined reorder overview.',
    'author': 'Goliath',
    'category': 'Inventory',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/supply_views.xml',
        'views/chocolate_views.xml',
        'views/reorder_views.xml',
        'views/menus.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'application': True,
    'installable': True,
}
