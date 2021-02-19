from odoo import models


class QLTVxlsx(models.AbstractModel):
    _name = 'report.qltv.report_muon_sach_temp_excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter', })
        sheet = workbook.add_worksheet('Thẻ mượn sách')

        # label
        sheet.write(0, 0, 'Người mượn sách', format1)
        sheet.write(0, 1, 'SĐT', format1)
        sheet.write(0, 2, 'Tên sách', format1)
        # value 1 gia tri
        # sheet.write(1, 0, lines.partner_id.name, format2)
        # sheet.write(1, 1, lines.phone, format2)
        # sheet.write(1, 2, lines.sach_id.name, format2)


