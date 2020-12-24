# -*- coding: utf-8 -*-
# Copyright 2020 Katia Logas Fonseca
# Part of Odoo. See LICENSE file for full copyright and licensing details.


import csv
import os

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
import logging
import requests
import os, sys, tempfile, traceback
from hashlib import md5
from pysimplesoap.simplexml import SimpleXMLElement
_logger = logging.getLogger(__name__)

class ResCompany(models.Model):
    _inherit = "res.company"

    def importImage(self, save_path):
        with open(save_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            count = 0
            for row in readCSV:
                if readCSV.line_num != 1:
                    print('Importing: ', row[1])
                    try:
                        if len(row[0].split('.')) > 1:
                            models = row[0].split('.')[1]
                        else:
                            models = row[0]
                        if 'product_product' in models:
                            PRODUCT = self.env['product.product']
                            external_ids = self.env['ir.model.data'].sudo().search([('model', '=', 'product.product')], order='id')
                        else:
                            PRODUCT = self.env['product.template']
                            external_ids = self.env['ir.model.data'].sudo().search([('model', '=', 'product.template')], order='id')
                        if external_ids:
                            external_id = external_ids.filtered(lambda x: x.complete_name == row[0])
                            if external_id:
                                PRODUCT.search([('id', '=', external_id.res_id)]).write({
                                    'image_1920': row[1]
                                })
                                if count % 2 == 0:
                                    PRODUCT._cr.commit()
                    except:
                        pass

        raise Warning('Import Done!')



