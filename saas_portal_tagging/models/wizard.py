from odoo import api, fields, models


class SaasTagClient(models.TransientModel):
    _name = 'saas_portal.tag_client'
    _description = 'SaaS Tag Client'

    @api.model
    def _default_categories(self):
        client = self.env['saas_portal.client'].browse(
            self.env.context['active_id'])
        return client.category_ids.ids

    category_ids = fields.Many2many('saas.portal.category',
        string='Tags', default=_default_categories)

    def apply(self):
        self.ensure_one()
        client = self.env['saas_portal.client'].browse(
            self.env.context['active_id'])
        client.write({'category_ids': [(6, 0, self.category_ids.ids)]})
        return True
