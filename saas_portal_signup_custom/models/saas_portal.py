from odoo import fields, models


class SaasPortalPlan(models.Model):
    _inherit = 'saas_portal.plan'

    dbname_prefix = fields.Char('DB Names prefix',
                                help='specify this field if you want to create several databases at once using saas_portal_signup module',
                                placeholder='test-')
