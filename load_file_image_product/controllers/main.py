# -*- coding: utf-8 -*-
# Copyright 2020 Katia Logas Fonseca
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, http, _
from odoo.http import request
from pathlib import Path
import os
import logging


_logger = logging.getLogger(__name__)



class LargeFileController(http.Controller):

    @http.route('/large/file/upload', type='http', auth="user", methods=['POST'], csrf=False)
    def restore(self, large_file):
        try:
            _logger.info(_('Start'))
            if not os.path.isdir('/tmp/update_product'):
                os.mkdir('/tmp/update_product')
            folder_to_clear = '/tmp/update_product'
            save_path = os.path.join(folder_to_clear, large_file.filename)

            [f.unlink() for f in Path(folder_to_clear).glob('*') if f.is_file()]
            
            data_file = large_file.read()
            _logger.info(_('Open File'))
            file_obj = open(save_path, "wb")
            _logger.info(_('Load file'))
            file_obj.write(data_file)
            file_obj.close()
            _logger.info(_('Save File'))
            res = request.env.user.company_id.importImage(save_path)
            _logger.info(_('Finish Process'))
            return res
        except Exception as e:
            _logger.exception(str(e) or repr(e))
            return str(e) or repr(e)
        finally:
            # if data_file:
            #     os.unlink(large_file.stream.name)
            return _("The update imagen product was loaded correctly. You only need to wait for the imagen to be updated.")




