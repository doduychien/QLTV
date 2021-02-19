{
    'name': 'Quản lý thư viện',
    'version': '1.0',
    'category': '',
    'author': 'Đỗ Duy Chiến',
    'sequence': '10',
    'summary': '',
    'depends': [
        'base',
        'report_xlsx',

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/view_sach.xml',
        'views/view_danh_muc_sach.xml',
        'views/view_nhom_sach.xml',
        'views/muon_sach_view.xml',
        'report/muon_sach.xml',
        'report/temp_muon_sach.xml',
        'views/sach_page.xml',
        'report/report_excel.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
