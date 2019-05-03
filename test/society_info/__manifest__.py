# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.
{
    'name': 'society info',
    'author': 'ketul',
    'version': '1.1',
    'sequence': 30,
    'description': """
society info app
    """,
    'category': 'accounting',
    'data': ['view/society_info_view.xml','view/society_floor_view.xml','view/society_amienities_view.xml'],
    'depends': ['base'],
    'installable': True,
    'application': False,
    'auto_install': False,
}