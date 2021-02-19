from odoo import fields, api, models
from odoo.exceptions import ValidationError


class ChungLoaiSach(models.Model):
    _name = 'chung.loai.sach'

    _sql_constraints = [
        ('uniq_ma_chung_loai', 'unique(ma)',
         'Mã chủng loại đã có !!'),
    ]

    name = fields.Char('Tên loại')
    ma = fields.Char('Mã loại')
    ghi_chu = fields.Text('Ghi chú')
    nhom_sach_id = fields.Many2one('nhom.sach', string='Nhóm sách')


class NhomSach(models.Model):
    _name = 'nhom.sach'

    name = fields.Char('Nhóm sách')
    ma = fields.Char('Mã nhóm')
    chung_loai_ids = fields.One2many('chung.loai.sach', 'nhom_sach_id', string='Chủng loại sách')
    ghi_chu = fields.Text('Ghi chú')

    _sql_constraints = [
        ('uniq_ma_nhom_sach', 'unique(ma)',
         'Mã nhóm đã tồn tại !!'),
    ]


class DanhMucSach(models.Model):
    _name = 'danh.muc.sach'

    name = fields.Char('Tên sách')
    ma = fields.Char('Mã sách')
    nhom_sach_id = fields.Many2one('nhom.sach', string='Nhóm sách')
    chung_loai_id = fields.Many2one('chung.loai.sach', string='Chủng loại sách',
                                    domain="[('nhom_sach_id','=',nhom_sach_id)]")
    ghi_chu = fields.Text('Ghi chú')

    _sql_constraints = [
        ('uniq_ma_sach', 'unique(ma)',
         'Mã sách đã tồn tại !!'),
    ]
    so_luong_ban_dau = fields.Integer('Số lượng ban đầu')
    so_luong_thuc_te = fields.Integer('Số lượng thực tế', compute='set_so_luong_thuc_te')
    so_luong_da_cho_muon = fields.Integer('Số lượng đã cho mượn', compute='set_so_luong_cho_muon')
    muon_sach_ids = fields.One2many('muon.sach', 'sach_id', string='Mượn sách')

    @api.depends('muon_sach_ids')
    def set_so_luong_cho_muon(self):
        for rec in self:
            rec.so_luong_da_cho_muon = sum(rec.muon_sach_ids.mapped('so_luong_muon'))

    @api.depends('so_luong_ban_dau', 'so_luong_da_cho_muon')
    def set_so_luong_thuc_te(self):
        for rec in self:
            rec.so_luong_thuc_te = rec.so_luong_ban_dau - rec.so_luong_da_cho_muon


class MuonSach(models.Model):
    _name = 'muon.sach'

    name = fields.Char('Lí do mượn sách')
    partner_id = fields.Many2one('res.partner', string='Người mượn')
    phone = fields.Char('Số điện thoại', related='partner_id.phone')
    so_luong_muon = fields.Integer('Số lượng mượn')
    sach_id = fields.Many2one("danh.muc.sach", string='Sách')

    @api.constrains('so_luong_muon')
    def check_so_luong_muon(self):
        for rec in self:
            if rec.sach_id and rec.so_luong_muon >= rec.sach_id.so_luong_thuc_te:
                raise ValidationError('Số lượng thực tế không đủ để đáp ứng !!!')
