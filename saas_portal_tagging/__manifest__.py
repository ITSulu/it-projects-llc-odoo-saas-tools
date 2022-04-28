{
    'name': 'SaaS Portal Tagging',
    'summary': "Ability to tag client databases",
    'version': '13.0.1.0.0',
    'author': 'Salton Massally <salton.massally@gmail.com>, Nicolas JEUDY',
    'license': 'GPL-3',
    'category': 'SaaS',
    'website': 'idtlabs.sl',
    'depends': [
        'saas_portal',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/saas_portal_tagging_views.xml',
        'views/wizard.xml'
    ],
    'installable': False,
}
