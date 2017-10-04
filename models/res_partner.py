# -*- coding: utf-8 -*-

from odoo import models, fields, api


class res_partner_nutri(models.Model):
    _inherit = 'res.partner'
    receita_ids = fields.One2many('nutribase.receita', 'customer_id', string='Receitas')




