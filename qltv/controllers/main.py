from odoo import http
from odoo.http import request
import json

class MuonSach(http.Controller):

    @http.route('/danh_muc_sach', type='http', auth='public', website=True)
    def muon_sach(self, **kwargs):
        ms = request.env['danh.muc.sach'].sudo().search([])
        return request.render('qltv.sach_page', {'ms': ms})

    # @http.route('/json_sach', type='json', auth="public")
    # def json_sach_1(self, type=''):
    #     return request.env['danh.muc.sach'].sudo().search([])