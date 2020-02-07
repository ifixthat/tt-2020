# -*- coding: utf-8 -*-
import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class OpenAcademyController(http.Controller):
    
    @http.route('/session', type='http', auth='user', website=True)
    def session(self, **post):
        return request.redirect('/')