{
    'name': 'Mi Módulo Personalizado',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Módulo para realizar los ejercicios solicitados',
    'depends': ['base', 'point_of_sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_client_inherit.xml',
        'views/pos_payment_screen_inherit.xml',
        'views/account_move_form.xml',
        'views/report_invoice.xml',
        'data/sales_channel_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
