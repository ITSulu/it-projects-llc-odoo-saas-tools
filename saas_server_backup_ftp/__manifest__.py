{
    'name': "SaaS Server Backup FTP",
    'author': "IT-Projects LLC, Ildar Nasyrov, Nicolas JEUDY",
    'license': 'GPL-3',
    "support": "apps@it-projects.info",
    'website': "https://twitter.com/nasyrov_ildar",
    'category': 'SaaS',
    'version': '13.0.1.0.0',
    'depends': [
        'saas_server',
    ],
    "external_dependencies": {"python": ['pysftp'], "bin": []},
    'data': [
        'views/res_config.xml',
        'data/ir_cron.xml',
    ],
    'installable': True,
}
