# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class newmodule(models.Model):
#     _name = 'newmodule.newmodule'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class nutriBase(models.Model):
    _name = 'nutribase.base'

    name = fields.Char('nome de teste')


class nutriIngredient(models.Model):
    _name = 'nutribase.ingredient'

    ingrediente_id = fields.Many2one('nutribase.ingredient.data',string='Ingrediente')
    quantidade = fields.Float('Quantidade')
    
    proteinas = fields.Float('Proteinas')
    gorduras = fields.Float('Gorduras')
    gorduras_saturadas = fields.Float('Gorduras Saturadas')
    gorduras_trans = fields.Float('Gorduras Trans')
    fibras = fields.Float('Fibras')
    sodio = fields.Float('Sodio')
    carboidratos = fields.Float('Carboidratos')
    receita_id = fields.Many2one('nutribase.receita', 'Receitas')
    
    @api.onchange('quantidade')
    def atualiza_ingrediente(self):
        self.proteinas = (self.quantidade * self.ingrediente_id.proteinas) / 100
        self.gorduras = (self.quantidade * self.ingrediente_id.gorduras) / 100
        self.gorduras_saturadas = (self.quantidade * self.ingrediente_id.gorduras_saturadas) / 100
        self.gorduras_trans = (self.quantidade * self.ingrediente_id.gorduras_trans) / 100
        self.fibras = (self.quantidade * self.ingrediente_id.fibras) / 100
        self.sodio = (self.quantidade * self.ingrediente_id.sodio) / 100
        self.carboidratos = (self.quantidade * self.ingrediente_id.carboidratos) / 100
        self.carboidratos = (self.quantidade * self.ingrediente_id.carboidratos) / 100


class nutriIngredientData(models.Model):
    _name = 'nutribase.ingredient.data'

    name = fields.Char('Ingrediente')
    description = fields.Text('Description')
    proteinas = fields.Float('Proteinas')
    gorduras = fields.Float('Gorduras')
    gorduras_saturadas = fields.Float('Gorduras Saturadas')
    gorduras_trans = fields.Float('Gorduras Trans')
    fibras = fields.Float('Fibras')
    sodio = fields.Float('Sodio')
    carboidratos = fields.Float('Carboidratos')

    
    
class nutriReceita(models.Model):
    _name = 'nutribase.receita'

    name = fields.Char('Nome da Receita')
    porcao = fields.Float('Porcao')
    rendimento = fields.Float('Rendimento')
    proteinas = fields.Float('Proteinas')
    gorduras = fields.Float('Gorduras Totais')
    gorduras_saturadas = fields.Float('Gorduras Saturadas')
    gorduras_trans = fields.Float('Gorduras Trans')
    fibras = fields.Float('Fibras')
    sodio = fields.Float('Sodio')
    carboidratos = fields.Float('Carboidratos')
    total_g = fields.Float('Total em Gramas')
    calorias = fields.Float('Calorias')
    ingredientes_ids = fields.One2many('nutribase.ingredient', 'receita_id', string="Ingredientes")
    customer_id = fields.Many2one('res.partner')
    
    @api.multi
    def atualiza_receita(self):
        self.proteinas = 0
        self.gorduras = 0
        self.gorduras_saturadas = 0
        self.gorduras_trans = 0
        self.fibras = 0
        self.sodio = 0
        self.carboidratos = 0
        self.total_g = 0
        self.calorias = 0
        
        for i in self.ingredientes_ids:
            self.proteinas += (i.proteinas / self.rendimento) * self.porcao
            self.gorduras += (i.gorduras / self.rendimento) * self.porcao
            self.gorduras_saturadas += (i.gorduras_saturadas / self.rendimento) * self.porcao
            self.gorduras_trans += (i.gorduras_trans / self.rendimento) * self.porcao
            self.fibras += (i.fibras / self.rendimento) * self.porcao
            self.sodio += (i.sodio / self.rendimento) * self.porcao
            self.carboidratos += (i.carboidratos / self.rendimento) * self.porcao
            self.total_g += i.quantidade
        self.calorias = (self.proteinas * 4) + (self.carboidratos * 4) + (self.gorduras * 9)
        
        

class res_partner_nutri(models.Model):
    _inherit = 'res.partner'
    
    receita_ids = fields.One2many('nutribase.receita','customer_id', string='Receitas')



