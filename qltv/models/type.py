from odoo import fields,api,models

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

class DanhMucSach(models.Model):

    _name = 'danh.muc.sach'

    name = fields.Char('Tên sách')
    ma = fields.Char('Mã sách')
    nhom_sach_id = fields.Many2one('nhom.sach', string='Nhóm sách')
    chung_loai_id = fields.Many2one('chung.loai.sach',string='Chủng loại sách',
                                    domain="[('nhom_sach_id','=',nhom_sach_id)]")

