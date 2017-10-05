# -*- coding: utf-8 -*-

from odoo import models, fields, api


class res_partner_nutri(models.Model):
    _inherit = 'res.partner'

    receita_ids = fields.One2many('nutribase.receita', 'customer_id', string='Receitas')
    visit_ids = fields.One2many('nutribase.visit', 'partner_id', string='Visitas')

    @api.multi
    def open_visits(self):
        pass



