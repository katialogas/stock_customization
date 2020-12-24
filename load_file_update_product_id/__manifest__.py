# -*- coding: utf-8 -*-
# Copyright 2020 Katia Logas Fonseca
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Import file with product images',
    'version': '0.0.1',
    'author': 'Katia Logas Fonseca',
    'license': '',
    'category': '',
    'website': '',
    'depends': ['base','web', 'product'],
    'data': [
             'views/load_file_update_product_id_view.xml',
             'views/large_file_record_view.xml',
             'views/load_file_update_product_id_menu.xml'],
    'qweb': [
             'static/src/xml/large_file_load.xml'],
    'installable': True,
    'auto_install': True,
}
