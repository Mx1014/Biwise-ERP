# -*- coding: utf-8 -*-
{
    'name': "local_carrier_tracking",

    'summary': """
        Customized features for carrier tracking,
        for local carriers like Paquetexpress or
        Mailboxes.
        """,

    'description': """
        Local carrier URL Tracking and Tracking Number
    """,

    'author': "Biwise",
    'website': "http://www.biwise.com.mx",
    'category': 'Inventory',
    'version': '14.0.1',
    'depends': ['delivery', 'mail'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/local_carrier_tracking.xml',
        #'views/product_pricing_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
