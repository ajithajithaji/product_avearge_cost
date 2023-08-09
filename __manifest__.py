{
    'name': 'Product Average Cost',
    'version': '16.0.1.0.0',
    'author': 'Ajit',
    'category': 'product',
    'sequence': 15,
    'depends': ['base_setup', 'sale', 'purchase', 'stock'],
    'data': [
        'views/product_average_cost_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
