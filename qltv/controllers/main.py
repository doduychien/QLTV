from odoo import http
from odoo.http import request


class MuonSach(http.Controller):

    @http.route('/danh_muc_sach', type='http', auth='public', website=True)
    def muon_sach(self, **kwargs):
        ms = request.env['danh.muc.sach'].search([])
        return request.render('qltv.sach_page', {'ms': ms})
