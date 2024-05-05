{
    'name': 'UIC Post',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 1,
    'summary': 'Track leads and close opportunities',
    'description': "UIC Post system",
    'license': "LGPL-3",
    'depends': [
        'base',
        'sale_management',
        'stock',
        'sale_loyalty',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
}
