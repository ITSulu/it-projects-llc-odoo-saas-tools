from odoo import fields, models


class SaasPortalServer(models.Model):
    _inherit = 'saas_portal.server'

    ip_address = fields.Char('Server IP Address')
