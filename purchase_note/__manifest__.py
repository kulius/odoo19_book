{
    'name': 'Purchase Order Note',
    'version': '19.0.1.0.0',
    'summary': 'Adds a purchase note field to purchase orders.',
    'description': 'Adds a text note field to purchase orders for additional remarks.',
    'author': 'Your Company',
    'license': 'LGPL-3',
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
